import copy

from hospital.models import *
from okb2.models import *
import uuid
from  datetime import datetime

import dbf
from  django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.mail import EmailMessage
from services.hospital.patient import PatientsData
from abc import  ABC
from collections import OrderedDict
from itertools import zip_longest
import copy
from collections import Counter
from services.hospital.history import History
from services.hospital.prot_reestr import ProtReestrHosp
from django import db

class CreateReestr(ABC):
    def __init__(self, user, date_1, date_2,type_reestr,his):
        self.user = MyUser.objects.get(user_id=user)
        self.date_1 = date_1
        self.date_2 = date_2
        self.his = his
        self.temp_dir = 'temp'
        self.dir = '/'.join([settings.MEDIA_ROOT,self.temp_dir,str(user),''])
        self.type_reestr = type_reestr
        self.date_creat = datetime.now()
        self.user_group_name = 'hospital_createreestr_%s' % user
    def create(self):
        pass

class Create(CreateReestr):
    def __init__(self, user, date_1, date_2,type_reestr,his):
        super().__init__(user, date_1, date_2,type_reestr,his)
    @staticmethod
    def func_chunk_itertools(lst):
        i_ = iter(lst)
        return list(zip_longest(i_, i_, i_, i_,i_, i_, i_, i_,i_, i_))
    def create(self):
        temp = []
        if (self.type_reestr == '' or self.type_reestr == 'kard') and self.his == '':
            self.patients = PatientsData(self.date_1, self.date_2, self.user)
            self.patients.sluchays()
            for t in self.patients.patients:
                if self.type_reestr == 'kard':
                    if t.sluchay.otd and t.sluchay.otd.naim in ['КАРДИОЛОГИЧЕСКОЕ']:
                        temp.append(t)
                else:
                    temp.append(t)
        else:
            his = [h.strip() for h in self.his.split(',') if h != '' and len(h.strip()) == 10]
            his = [h['id'] for h in Sluchay.objects.values('id').filter(nib__in=his)]
            print(his)
            self.patients = PatientsData(self.date_1, self.date_2, self.user)
            for h in his:
                self.patients.get_data(h)
            for patient in self.patients.patients:
                temp.append(patient)

        if len(temp) > 0:
            self.reestr = []
            count_1 = 100 / len(temp)
            sm = 0
            self.err_list = []
            for n, pat in enumerate(temp):
                self.insert(pat, n)
                sm += count_1
                async_to_sync(get_channel_layer().group_send)(self.user_group_name,{'type': 'progress', 'text': sm})
            else:
                self.create_dbf()
                ProtReestrHosp()
                ProtReestrHosp.prot(self.date_1, self.date_2, self.user, self.err_list)
                async_to_sync(get_channel_layer().group_send)(self.user_group_name,
                                                              {'type': 'progress', 'text': sm})
            # chunk = self.func_chunk_itertools(temp)
            # self.count_1 = 100 / len(chunk)
            #
            # threads = []
            # self.sm = 0
            # self.err_list = []
            # for n, pat in enumerate(chunk, 1):
            #     self.sm += self.count_1
            #     t = Thread(target=self.chunk_threads, args=(pat,n))
            #     threads.append(t)
            #     t.start()
            #     async_to_sync(get_channel_layer().group_send)(self.user_group_name,
            #                                                   {'type': 'progress', 'text': self.sm})
            # for t in threads:
            #     t.join()
            # else:
            #     # db.close_old_connections()
            #     self.create_dbf()
            #     ProtReestrHosp()
            #     ProtReestrHosp.prot(self.date_1,self.date_2,self.user,self.err_list)
            #     async_to_sync(get_channel_layer().group_send)(self.user_group_name, {'type': 'progress', 'text': self.sm})


    # def chunk_threads(self, sluchay_list,n):
    #     for sluch in sluchay_list:
    #         if sluch:
    #             self.insert(sluch,n)
    def oper_pop(self,pat):
        pop = pat.sluchay.oper.filter(pop=True) if pat.sluchay.oper != None else 0
        if pop.count() > 0:
            return pop[0]
        return None
    def tarif_sp(self,pat):
        if pat.sluchay.tip_oms == '1':
            if pat.sluchay.code_usl != None:
                try:
                    return Tarif.objects.get(Code_usl=pat.sluchay.code_usl.kod,Ur='3.0',KOEF_D='1.10500',dateend=None)
                except:
                    return None
            else:
                t003 = None
                try:
                    t003 = T003.objects.get(vidpom=1,usl_ok=1,dateend=None,code_usl_kz=pat.sluchay.ksg_osn.code_usl_kz)
                    # self.err['ksg_o'] = self.p
                    # self.nib = pat.sluchay.nib
                except:
                    t003 = None

                if t003 != None:
                    return Tarif.objects.get(Code_usl=t003.kod,Ur='3.0',KOEF_D='1.10500',dateend=None)
                return None
        return None

    def inv_sp(self,inv):
        if inv == 81:
            return 1
        elif inv == 82:
            return 2
        elif inv == 83:
            return 3
        return 0
    def novor_sp(self,pat):
        if (pat.sluchay.vds != None and pat.sluchay.vds.ctkom != None and pat.sluchay.vds.ctkom.kod == 888) and (
                pat.patient.nvs == 'Д' and (pat.sluchay.datp - pat.patient.datr).days < 28):
            novor = str(pat.patient.pol.id_pol) if pat.patient.pol != None else ''
            novor += str(pat.patient.datr.day()) if pat.patient.datr != None else ''
            novor += str(pat.patient.datr.month()) if pat.patient.datr != None else ''
            novor += str(pat.patient.datr.year())[2:3] if pat.patient.datr != None else ''
            novor += '01'
            return novor
        return None
    def vidpom_sp(self,pat):
        if pat.sluchay.le_vr != None and pat.sluchay.le_vr.kod != None:

            if pat.vds != None and pat.vds.vds:
                if pat.vds.vds.kod in ['5','7','Д']:
                    return 32
                return 31
            else:
                return 31
        return 31
    def for_pom_sp(self,pat):
        if pat.sluchay.code_usl != None and pat.sluchay.code_usl.kod == '1.1.3.150':
            return 2
        else:
            if pat.sluchay.goc != None:
                return pat.sluchay.goc.id_tip
            return None
    def det_sp(self,pat):
        if pat.le_vr != None and pat.le_vr.kod != None:
            v002 = int(pat.le_vr.kod.v002) if pat.le_vr.kod.v002 != None and pat.le_vr.kod.v002 != '' else 0
            if (v002 >= 17 and v002 <= 21) or (v002 == 86) or (v002 == 55):
                return 1
            return 0
        return
    def idsp_sp(self,pat):
        idsp = 33
        if pat.vds != None and pat.vds.vds != None:
            kod = pat.vds.vds.kod
            if kod in ['5','7','Д']:
                idsp = 32
            elif kod in ['0','']:
                idsp = 33
        return idsp
    def comentsl_sp(self,pat):
        comentsl = None
        if pat.sluchay.code_usl != None:
            if pat.sluchay.code_usl.kod == '1.1.3.150':
                comentsl = '4'
        if pat.le_trv and pat.le_trv.trav_ns == True:
            comentsl = '11'
        return comentsl
    def v_tp_sp(self,pat):

        if pat.sluchay.tip_oms == '1':
            if pat.sluchay.code_usl != None:
                return int(str(pat.sluchay.code_usl.kod)[0])
            else:
                try:
                    t003 = T003.objects.get(vidpom=1, usl_ok=1, dateend=None,code_usl_kz=pat.sluchay.ksg_osn.code_usl_kz)
                except:
                    t003 = None
                if t003:
                    return int(str(t003.kod)[0])
        elif pat.sluchay.tip_oms == '2':
            if pat.sluchay.code_usl_vt != None:
                return int(str(pat.sluchay.code_usl_vt.kod)[0])
        return None

    def npl_sp(self,pat,kd):
        if pat.sluchay.rslt != None:
            if pat.sluchay.rslt.id_tip in [101,102,104,105,106,110]:
                return 3
            elif pat.sluchay.rslt.id_tip == 107:
                return 1
            elif pat.sluchay.rslt.id_tip == 108:
                return 2
        elif pat.sluchay.ksg_osn != None:
            if pat.sluchay.ksg_osn.ksg == 'st36.004':
                return 3
        elif pat.sluchay.le_vr != None:
            return 3 if pat.le_vr != None and kd <= 3 else None
        return None
    def comentu_sp(self,pat,kd):

        ksg_list = ['st02.001','st02.002','st02.003','st02.004','st02.010','st02.011','st03.022','st05.008',
                    'st08.001','st08.002','st08.003','st12.010','st12.011','st14.002','st15.008','st15.009',
                    'st16.005','st19.007','st19.038','st19.105','st19.106','st19.107','st19.108','st19.109',
                    'st19.110','st19.111','st19.112','st19.113','st19.114','st19.115','st19.116','st19.117',
                    'st19.118','st19.119','st19.120','st19.121','st19.082','st19.090','st19.094','st19.097',
                    'st19.100','st20.005','st20.006','st20.010','st21.001','st21.002','st21.003','st21.004',
                    'st21.005','st21.006','st25.004','st27.012','st30.006','st30.010','st30.011','st30.012',
                    'st30.014','st31.017','st32.002','st32.012','st32.016','st34.002','st36.001','st36.007',
                    'st36.009','st36.010','st36.011','st36.016','st36.017','st36.018','st36.019']


        com = ''
        if pat.sluchay.tip_oms == '1':
            # if pat.sluchay.code_usl != None and int(str(pat.sluchay.code_usl)[6]) == 1 and pat.sluchay.rslt and pat.sluchay.rslt.id_tip != 101:
            if pat.sluchay.code_usl != None and int(str(pat.sluchay.code_usl)[6]) == 1:
                if pat.le_vr != None and kd <= 3:
                    com = '0.5'
                elif pat.le_vr != None and kd > 3 and pat.sluchay.rslt and pat.sluchay.rslt.id_tip != 101:
                    com = '0.8'
            # elif pat.sluchay.code_usl != None and int(str(pat.sluchay.code_usl)[6]) == 2 and pat.sluchay.rslt and pat.sluchay.rslt.id_tip != 101:
            elif pat.sluchay.code_usl != None and int(str(pat.sluchay.code_usl)[6]) in [2,3]:
                if pat.le_vr != None and  kd <= 3:
                    com = '0.9'
                elif pat.le_vr != None and kd > 3 and pat.sluchay.rslt and pat.sluchay.rslt.id_tip != 101:
                    com = '1.0'


        if pat.sluchay.tip_oms == '1':
            if pat.sluchay.rslt and pat.sluchay.rslt.id_tip in [102,104,105,107,110]:
                if pat.sluchay.ksg_osn and pat.sluchay.ksg_osn.ksg in ksg_list:
                    com = '1.0'
            else:
                if pat.le_vr != None and kd <= 3:
                    if pat.sluchay.ksg_osn and pat.sluchay.ksg_osn.ksg in ksg_list:
                        com = '1.0'
        return com
    def vb_p_sp(self,pat):

        if pat.vb_s:
            for v in pat.vb_s:
                if v.potd:
                    return 1
        return None
    def cons_sp(self,pat):
        if pat.cons:
            p = pat.cons.pr_cons.id_cons if pat.cons.pr_cons else 0
            d = pat.cons.dt_cons.strftime('%d.%m.%Y') if pat.cons.dt_cons else 0
            return f'{p}/{d}'
        return None
    def icx_sp(self,pat):
        if pat.sluchay.icx:
            if pat.sluchay.icx.id_iz in [105,106]:
                return 104
            return pat.sluchay.icx.id_iz
        return None
    def smo_ok_sp(self,pat):
        if pat.vds != None and pat.vds.ctkom != None and pat.vds.ctkom.smo_okato != None:
            smo_okato = pat.vds.ctkom.smo_okato.split(".")[0]
            if len(smo_okato) == 5:
                return smo_okato
            elif len(smo_okato) == 4:
                return f'0{smo_okato}'
            elif len(smo_okato) == 3:
                return f'00{smo_okato}'
        return ''
    def lpu_1_sp(self,pat):
        if pat.sluchay.otd != None and pat.sluchay.otd.t007 != None and pat.sluchay.otd.t007 != 'nan' and pat.sluchay.otd.t007 != '':
            lpu_1 = pat.sluchay.otd.t007.split(".")[0]
            if len(lpu_1) == 6:
                return f'00{lpu_1}'
            return f'{lpu_1}'
        return ''
    def iddokt_sp(self,pat):
        if pat.sluchay.iddokt != None:
            try:
                return  f'720002 {pat.sluchay.iddokt.kod.t005}'
            except AttributeError:
                return  f'720002 '
        else:
            if pat.le_vr and pat.le_vr.kod:
                return f'720002 {pat.le_vr.kod.t005}'
            return ''
    def ds1_sp(self,pat):
        if pat.sluchay.dskz2 != None:
            return  pat.sluchay.dskz2.kod
        else:
            if pat.sluchay.dskz != None:
                return pat.sluchay.dskz.kod
            return ''
    def med_dev_sp(self,pat):
        if len(pat.med_dev) > 0:
            return pat.med_dev[0]
        return None
    def insert(self,pat,n):
        err = dict()
        p = pat
        resdict_S = OrderedDict()
        pac = uuid.uuid1()
        pop = self.oper_pop(pat)
        tarif = self.tarif_sp(pat)
        med_dev = self.med_dev_sp(pat)

        if pat.sluchay.datv != pat.sluchay.datp:
            kd = int(str(pat.sluchay.datv - pat.sluchay.datp).split(' ')[0])
        else:
            kd = 1
        try:
            if len(p.sluchay.err_text) > 0:
                err['err_text'] = p
        except TypeError:
            pass

        comentu = self.comentu_sp(pat,kd)
        resdict_S['BLOCK_CD'] = 'S'
        resdict_S['CODE_MO'] = '720002'
        resdict_S['FAM'] = pat.patient.fam.upper() if pat.patient.fam != '' else None
        resdict_S['IM'] = pat.patient.im.upper() if pat.patient.im != '' else None
        resdict_S['OT'] = pat.patient.ot.upper() if pat.patient.ot != '' else None
        resdict_S['W'] = pat.patient.pol.id_pol if pat.patient.pol != None else None
        resdict_S['DR'] = pat.patient.datr if pat.patient.datr != '' else None
        resdict_S['DOST'] = None
        resdict_S['TEL'] = pat.patient.tel if pat.patient.tel != '' else None
        resdict_S['ID_PAC'] = f'{pac}'
        resdict_S['VPOLIS'] = pat.vds.t_pol.id_tip if pat.vds != None and pat.vds.t_pol != None else None
        resdict_S['SPOLIS'] = pat.vds.sctp if pat.vds != None and pat.vds.sctp != None else None
        resdict_S['NPOLIS'] = pat.vds.nctp if pat.vds != None and pat.vds.nctp != None else None
        resdict_S['ST_OKATO'] = f'{pat.vds.ctkom.smo_okato.split(".")[0]}' if pat.vds != None and pat.vds.t_pol != None and pat.vds.t_pol.id_tip == 1 and \
                                     pat.vds.ctkom != None and pat.vds.ctkom.smo_okato != None else None
        resdict_S['SMO'] = f'{pat.vds.ctkom.smo.split(".")[0]}' if pat.vds != None and pat.vds.ctkom != None and \
                                                          pat.vds.ctkom.smo != None else None
        resdict_S['SMO_OGRN'] = f'{pat.vds.ctkom.ogrn.split(".")[0]}' if pat.vds != None and pat.vds.ctkom != None and \
                                         pat.vds.ctkom.ogrn != None else None

        resdict_S['SMO_OK'] = self.smo_ok_sp(pat)
        resdict_S['SMO_NAM'] = pat.vds.ctkom.naim_n if pat.vds != None and pat.vds.ctkom != None else None
        resdict_S['INV'] = self.inv_sp(pat.patient.in_t.kod) if pat.patient.in_t != None else 0
        resdict_S['NOVOR'] = self.novor_sp(pat)
        resdict_S['VNOV_D'] =  int(pat.patient.vec) if pat.patient.vec != None and pat.patient.vec != 'None' and  pat.patient.vec != '' else None
        resdict_S['IDCASE'] = n
        resdict_S['USL_OK'] = 1
        resdict_S['VIDPOM'] = self.vidpom_sp(pat)
        resdict_S['FOR_POM'] = self.for_pom_sp(pat)

        if pat.sluchay.tip_oms == '2':
            if pat.sluchay.metod_hmp != '':
                resdict_S['VID_HMP'] = pat.sluchay.metod_hmp
            else:
                resdict_S['VID_HMP'] = ''
            if pat.sluchay.vid_hmp != '':
                resdict_S['METOD_HMP'] = pat.sluchay.vid_hmp
            else:
                resdict_S['METOD_HMP'] = ''
        else:
            resdict_S['VID_HMP'] = ''
            resdict_S['METOD_HMP'] = ''

        resdict_S['NPR_MO'] = pat.sluchay.lpy.mo if pat.sluchay.lpy != None else None
        resdict_S['LPU'] = '720002'
        resdict_S['LPU_1'] = self.lpu_1_sp(pat)
        resdict_S['PODR'] = f'{pat.sluchay.otd.t013.split(".")[0]}' if pat.sluchay.otd != None and pat.sluchay.otd.t013 != None and \
                                                         pat.sluchay.otd.t013 != 'nan' and pat.sluchay.otd.t013 != '' else None

        resdict_S['PROFIL'] = pat.le_vr.kod.v002 if pat.le_vr != None and pat.le_vr.kod != None else None
        resdict_S['DET'] = self.det_sp(pat)

        resdict_S['TAL_D'] = pat.sluchay.npr_date if pat.sluchay.npr_date != None and pat.sluchay.npr_date != '' else None
        resdict_S['TAL_P'] = pat.sluchay.npr_date if pat.sluchay.npr_date != None and pat.sluchay.npr_date != '' else None

        resdict_S['TAL_NUM'] = None
        resdict_S['NHISTORY'] = pat.sluchay.nib
        resdict_S['P_PER'] = pat.sluchay.p_per.kod if pat.sluchay.p_per != None else None
        resdict_S['EXTR'] = pat.sluchay.goc.id_tip if pat.sluchay.goc != None else None
        resdict_S['PRIV'] = pat.patient.in_t.kod if pat.patient.in_t != None else None
        resdict_S['DATE_1'] = pat.sluchay.datp
        resdict_S['DATE_2'] = pat.sluchay.datv
        resdict_S['DS0'] = pat.sluchay.ds_0.kod if pat.sluchay.ds_0 != None else None
        # resdict_S['DS1'] = pat.sluchay.dskz.kod if pat.sluchay.dskz != None else None
        resdict_S['DS1'] = self.ds1_sp(pat)
        resdict_S['DS2'] = pat.sluchay.dsc.kod if pat.sluchay.dsc != None else None
        resdict_S['DS3'] = pat.sluchay.dson.kod if pat.sluchay.dson != None else None
        resdict_S['VNOV_M'] = pat.patient.vec if pat.patient.vec != None and \
                                                 pat.patient.vec != '0' and pat.patient.vec != '' else None
        if pat.sluchay.tip_oms == '1':
            resdict_S['CODE_MES1'] = pat.sluchay.ksg_osn.ksg if pat.sluchay.ksg_osn != None else None
        else:
            resdict_S['CODE_MES1'] = ''
        resdict_S['CODE_MES2'] = pat.sluchay.ksg_sop.ksg if pat.sluchay.ksg_sop != None else None
        resdict_S['RSLT'] = pat.sluchay.rslt.id_tip if pat.sluchay.rslt != None else None
        # resdict_S['ISHOD'] = pat.sluchay.icx.id_iz if pat.sluchay.icx != None else None
        resdict_S['ISHOD'] = self.icx_sp(pat)
        resdict_S['PRVS'] = int(pat.le_vr.kod.v021) if pat.le_vr != None and pat.le_vr.kod != None  and pat.le_vr.kod.v021 != '' else None

        # resdict_S['IDDOKT'] = f'720002 {pat.le_vr.kod.t005}' if pat.le_vr != None and pat.le_vr.kod != None else ''
        resdict_S['IDDOKT'] = self.iddokt_sp(pat)

        if pop != None and pop.kodx != None:
            if pop.kodx.t005 == '':
                err['t005p'] = p
            resdict_S['CODE_MD'] = f'720002 {pop.kodx.t005}'
        else:
            resdict_S['CODE_MD'] = ''

        resdict_S['OS_SLUCH'] = None
        resdict_S['IDSP'] = self.idsp_sp(pat)
        resdict_S['ED_COL'] = 1
        resdict_S['KOL_USL'] = 1

        resdict_S['KD'] = kd
        resdict_S['KD_Z'] = kd

        if pat.sluchay.tip_oms == '1':
            if tarif:
                resdict_S['TARIF'] = tarif.Tarif
                # if tarif.Tarif == None or tarif.Tarif == '':
                #     self.err['tarif'] = self.p
            else:
                resdict_S['TARIF'] = None
                # self.err['tarif'] = self.p

            if tarif:
                resdict_S['SUMV'] = tarif.Tarif

            else:
                resdict_S['SUMV'] = None
                # self.err['tarif'] = self.p

        else:
            if pat.sluchay.code_usl_vt and pat.sluchay.code_usl_vt.tarif:
                resdict_S['TARIF'] = pat.sluchay.code_usl_vt.tarif
                # if pat.sluchay.code_usl_vt.tarif == None or pat.sluchay.code_usl_vt.tarif == '':
                #     self.err['tarif'] = self.p
            else:
                resdict_S['TARIF'] = None
                # self.err['tarif'] = self.p

            if pat.sluchay.code_usl_vt and pat.sluchay.code_usl_vt.tarif:
                resdict_S['SUMV'] = pat.sluchay.code_usl_vt.tarif
                # if pat.sluchay.code_usl_vt.tarif == None or pat.sluchay.code_usl_vt.tarif == '':
                #     # self.err['sumv'] = self.p
            else:
                resdict_S['SUMV'] = None

            # resdict_S['SUMV'] = pat.sluchay.code_usl_vt.tarif if pat.sluchay.code_usl_vt else None
        # self.err['tarif'] = self.p

        resdict_S['COMENTSL'] = self.comentsl_sp(pat)
        vid_vme = ''
        if pat.sluchay.tip_oms == '1':
            if pat.sluchay.code_usl != None:
                if int(pat.sluchay.code_usl.kod[6]) == 1:
                    resdict_S['VID_VME'] = ''
                else:
                    resdict_S['VID_VME'] = pop.kod_op.kod if pop and pop.kod_op != None else ''
                    vid_vme = pop.kod_op.kod if pop and pop.kod_op != None else ''
        else:
            resdict_S['VID_VME'] = pop.kod_op.kod if pop and pop.kod_op != None else ''
            vid_vme = pop.kod_op.kod if pop and pop.kod_op != None else ''
        code = ''
        if pat.sluchay.tip_oms == '1':
            if pat.sluchay.code_usl != None:
                resdict_S['CODE_USL'] = pat.sluchay.code_usl.kod
                code = pat.sluchay.code_usl.kod
            else:
                # self.err['ksg_o'] = self.p
                try:
                    t003 = T003.objects.get(vidpom=1,usl_ok=1,dateend=None,code_usl_kz=pat.sluchay.ksg_osn.code_usl_kz)
                except:
                    t003 = None
                if t003:
                    resdict_S['CODE_USL'] = t003.kod
                    code = t003.kod
                else:
                    resdict_S['CODE_USL'] = ''

        else:
            if pat.sluchay.code_usl_vt:
                resdict_S['CODE_USL'] = pat.sluchay.code_usl_vt.kod
            else:
                resdict_S['CODE_USL'] = ''
                # self.err['ksg_v'] = self.p
            code = pat.sluchay.code_usl_vt.kod if pat.sluchay.code_usl_vt else ''

        resdict_S['FAM_P'] = pat.patient_p.fam_p if pat.patient_p != None else None
        resdict_S['IM_P'] = pat.patient_p.im_p if pat.patient_p != None else None
        resdict_S['OT_P'] = pat.patient_p.ot_p if pat.patient_p != None else None
        resdict_S['W_P'] = pat.patient_p.pol.id_pol if pat.patient_p != None and pat.patient_p.pol != None else None
        resdict_S['DR_P'] = pat.patient_p.datr if pat.patient_p != None else None
        resdict_S['DOST_P'] = None
        resdict_S['MR'] = pat.patient.m_roj
        resdict_S['DOCTYPE'] = str(pat.patient.udl.id_doc) if pat.patient.udl != None else None
        resdict_S['DOCSER'] = pat.patient.s_pasp
        resdict_S['DOCNUM'] = pat.patient.n_pasp
        resdict_S['DOCDATE'] = pat.patient.docdate
        resdict_S['DOCORG'] = pat.patient.docorg
        resdict_S['SNILS'] = pat.patient.ss
        resdict_S['OKATOG'] = str(pat.patient.okatog[:11]) if pat.patient.okatog != None else None
        resdict_S['OKATOP'] = str(pat.patient.okatop[:11]) if pat.patient.okatop != None else None
        resdict_S['YEAR'] = datetime.now().year
        resdict_S['MONTH'] = datetime.now().month
        resdict_S['NSCHET'] = None
        resdict_S['DSCHET'] = None
        resdict_S['PLAT'] = '72'
        resdict_S['V_TP'] = self.v_tp_sp(pat)
        resdict_S['PR_NOV'] = None
        resdict_S['NAZ_V'] = None
        resdict_S['NAPR_USL'] = pat.napr.napr_usl.kod if pat.napr != None and pat.napr.napr_usl != None else None
        resdict_S['NAPR_DATE'] = pat.napr.naprdate if pat.napr != None else None
        resdict_S['NAPR_MO'] = pat.napr.napr_mo.mo if pat.napr != None and pat.napr.napr_mo != None else None
        resdict_S['NAPR_V'] = pat.napr.napr_v.id_vn if pat.napr != None and pat.napr.napr_v != None else None
        if comentu != '':
            resdict_S['NPL'] = self.npl_sp(pat,kd)
        else:
            resdict_S['NPL'] = None
        resdict_S['NPL_CF'] = None
        # resdict_S['COMENTU'] = self.comentu_sp(pat)
        resdict_S['COMENTU'] = comentu
        resdict_S['SL_ID'] = str(n)
        resdict_S['IDSERV'] = str(n)
        resdict_S['MSE'] = None
        resdict_S['NPR_DATE'] = pat.sluchay.npr_date if pat.sluchay.npr_date else None
        resdict_S['PROFIL_K'] = pat.le_vr.prof_k.idk_pr if pat.le_vr and pat.le_vr.prof_k else None
        resdict_S['P_CEL'] = '2.6' if pat.sluchay.code_usl and pat.sluchay.code_usl.kod == '1.1.3.150' else None
        resdict_S['DN'] = None
        resdict_S['REAB'] = 1 if pat.sluchay.code_usl and str(pat.sluchay.code_usl.kod)[:6] == '4' else None
        resdict_S['VB_P'] = self.vb_p_sp(pat)

        if pat.sluchay.tip_oms == '1':
            resdict_S['N_KSG'] = pat.sluchay.ksg_osn.ksg if pat.sluchay.ksg_osn else ''
        else:
            resdict_S['N_KSG'] = ''

        resdict_S['VER_KSG'] = self.date_creat.year
        resdict_S['KSG_PG'] = None
        resdict_S['KOEF_Z'] = tarif.KOEF_Z if tarif else None
        resdict_S['KOEF_UP'] = tarif.Koef_Up if tarif else None
        resdict_S['BZTSZ'] = tarif.BZTSZ if tarif else None
        resdict_S['KOEF_D'] = tarif.KOEF_D if tarif else None
        resdict_S['KOEF_U'] = tarif.KOEF_U if tarif else None
        resdict_S['CRIT'] = pat.sluchay.oopkk.kod if pat.sluchay.oopkk else None
        resdict_S['SL_K'] = 0
        resdict_S['C_ZAB'] = pat.sluchay.c_zab.id_cz if pat.sluchay.c_zab else None
        resdict_S['DS_ONK'] = 0
        resdict_S['ONK_SL'] = 1 if pat.sluchay.dskz and str(pat.sluchay.dskz.kod)[:1] == 'C' else 0
        resdict_S['DS1_T'] = pat.onk_sl.ds1_t.id_reas if pat.onk_sl and pat.onk_sl.ds1_t else None
        resdict_S['STAD'] = pat.onk_sl.stad.id_st if pat.onk_sl and pat.onk_sl.stad else None
        resdict_S['ONK_T'] = pat.onk_sl.onk_t.kod_t if pat.onk_sl and pat.onk_sl.onk_t else None
        resdict_S['ONK_N'] = pat.onk_sl.onk_n.kod_n if pat.onk_sl and pat.onk_sl.onk_n else None
        resdict_S['ONK_M'] = pat.onk_sl.onk_m.kod_m if pat.onk_sl and pat.onk_sl.onk_m else None
        resdict_S['MTSTZ'] = pat.onk_sl.mtstz if pat.onk_sl and pat.onk_sl.mtstz != '' else None
        resdict_S['SOD'] = None
        resdict_S['K_FR'] = None
        resdict_S['WEI'] = None
        resdict_S['HEI'] = None
        resdict_S['BSA'] = None
        resdict_S['B_DIAG'] = None
        resdict_S['B_PROT'] = None
        resdict_S['CONS'] = self.cons_sp(pat)
        resdict_S['ONKUSL_ID'] = None
        resdict_S['USL_TIP'] = pat.onk_usl.usl_tip.id_tlech if pat.onk_usl and pat.onk_usl.usl_tip else None
        resdict_S['HIR_TIP'] = pat.onk_usl.hir_tip.id_thir if pat.onk_usl and pat.onk_usl.hir_tip else None
        resdict_S['LEK_TIP_L'] = None
        resdict_S['LEK_TIP_V'] = None
        resdict_S['LUCH_TIP'] = None
        resdict_S['PPTR'] = None
        resdict_S['REGNUM'] = None
        resdict_S['CODE_SH'] = None
        resdict_S['DATE_INJ'] = None
        resdict_S['DATE_IN'] = pat.sluchay.datp if pat.sluchay.datp else None
        resdict_S['DATE_OUT'] = pat.sluchay.datv if pat.sluchay.datv else None
        resdict_S['PRSCSDTBEG'] = None
        resdict_S['ADRES'] = pat.patient.adr
        resdict_S['DATE_MED'] = med_dev.date if med_dev and med_dev.date else None
        resdict_S['CODE_MEDDE'] = int(med_dev.code.rzn) if med_dev  and med_dev.code else None
        resdict_S['NUMBER_SER'] = med_dev.number_ser if med_dev else ''

        if len(resdict_S['CODE_USL']) == 0:
            if pat.sluchay.tip_oms == '1':
                err['ksg_o'] = p
            elif pat.sluchay.tip_oms == '2':
                err['ksg_v'] = p

        if resdict_S['TARIF'] == None:
            err['tarif'] = p

        if pat.sluchay.tip_oms == '2':
            if resdict_S['VID_HMP'] == '':
                err['vid_hmp'] = p
            if resdict_S['METOD_HMP'] == '':
                err['metod_hmp']=p
        if len(resdict_S['IDDOKT']) == 7:
            err['t005'] = p

        if resdict_S['NPR_MO'] != None:
            if resdict_S['NPR_DATE'] == None:
                resdict_S['NPR_DATE'] = pat.sluchay.datp


        self.reestr.append(resdict_S)

        if code[:7] == '1.1.1.1' and vid_vme != '':
            resdict_U = copy.deepcopy(resdict_S)
            resdict_U['BLOCK_CD'] = 'U'
            self.reestr.append(resdict_U)

        ds = self.ds1_sp(pat)
        if ds != '' and ds[0] == 'C':
            resdict_O = copy.deepcopy(resdict_S)
            resdict_N = copy.deepcopy(resdict_S)
            resdict_O['BLOCK_CD'] = 'O'
            resdict_N['BLOCK_CD'] = 'N'
            self.reestr.append(resdict_O)
            self.reestr.append(resdict_N)

        if len(err) > 0:
            self.err_list.append(err)

        ###Нужно допилить блоки U,I,O,N
    def create_dbf(self):
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
        self.dir += 'reestr_'+ str(self.user.user.id)
        table = dbf.Table('{0}.dbf'.format(self.dir),
                          'BLOCK_CD C(1);'
                          'CODE_MO C(6);'
                          'FAM C(40);'
                          'IM C(40);'
                          'OT C(40);'
                          'W N(1,0);'
                          'DR D;'
                          'DOST C(48);'
                          'TEL C(40);'
                          'ID_PAC C(36);'
                          'VPOLIS N(1,0);'
                          'SPOLIS C(20);'
                          'NPOLIS C(20);'
                          'ST_OKATO C(5);'
                          'SMO C(5);'
                          'SMO_OGRN C(15);'
                          'SMO_OK C(5);'
                          'SMO_NAM C(100);'
                          'INV N(1,0);'
                          'NOVOR C(9);'
                          'VNOV_D N(4,0);'
                          'IDCASE N(11,0);'
                          'USL_OK N(2,0);'
                          'VIDPOM N(4,0);'
                          'FOR_POM N(1,0);'
                          'VID_HMP C(20);'
                          'METOD_HMP C(20);'
                          'NPR_MO C(20);'
                          'LPU C(6);'
                          'LPU_1 C(8);'
                          'PODR C(12);'
                          'PROFIL N(3,0);'
                          'DET N(1,0);'
                          'TAL_D D;'
                          'TAL_P D;'
                          'TAL_NUM C(20);'
                          'NHISTORY C(50);'
                          'P_PER N(1,0);'
                          'EXTR N(1,0);'
                          'PRIV N(3,0);'
                          'DATE_1 D;'
                          'DATE_2 D;'
                          'DS0 C(10);'
                          'DS1 C(10);'
                          'DS2 C(100);'
                          'DS3 C(100);'
                          'VNOV_M C(32);'
                          'CODE_MES1 C(20);'
                          'CODE_MES2 C(20);'
                          'RSLT N(3,0);'
                          'ISHOD N(3,0);'
                          'PRVS N(4,0);'
                          'IDDOKT C(25);'
                          'CODE_MD C(25);'
                          'OS_SLUCH C(20);'
                          'IDSP N(2,0);'
                          'ED_COL N(5,2);'
                          'KOL_USL N(6,2);'
                          'KD N(6,2);'
                          'KD_Z N(6,2);'
                          'TARIF N(15,2);'
                          'SUMV N(15,2);'
                          'COMENTSL C(100);'
                          'VID_VME C(15);'
                          'CODE_USL C(20);'
                          'FAM_P C(40);'
                          'IM_P C(40);'
                          'OT_P C(40);'
                          'W_P N(1,0);'
                          'DR_P D;'
                          'DOST_P C(48);'
                          'MR C(200);'
                          'DOCTYPE C(2);'
                          'DOCSER C(10);'
                          'DOCNUM C(20);'
                          'DOCDATE D;'
                          'DOCORG C(100);'
                          'SNILS C(14);'
                          'OKATOG C(11);'
                          'OKATOP C(11);'
                          'YEAR N(4,0);'
                          'MONTH N(2,0);'
                          'NSCHET C(15);'
                          'DSCHET D;'
                          'PLAT C(5);'
                          'V_TP N(1,0);'
                          'PR_NOV N(1,0);'
                          'NAZ_V N(1,0);'
                          'NAPR_USL C(15);'
                          'NAPR_DATE D;'
                          'NAPR_MO C(6);'
                          'NAPR_V N(1,0);'
                          'NPL N(1,0);'
                          'NPL_CF N(6,2);'
                          'COMENTU C(20);'
                          'SL_ID C(36);'
                          'IDSERV C(36);'
                          'MSE N(1,0);'
                          'NPR_DATE D;'
                          'PROFIL_K N(3,0);'
                          'P_CEL C(3);'
                          'DN N(1,0);'
                          'REAB N(1,0);'
                          'VB_P N(1,0);'
                          'N_KSG C(20);'
                          'VER_KSG N(4,0);'
                          'KSG_PG N(1,0);'
                          'KOEF_Z N(8,5);'
                          'KOEF_UP N(8,5);'
                          'BZTSZ N(10,2);'
                          'KOEF_D N(8,5);'
                          'KOEF_U N(8,5);'
                          'CRIT C(10);'
                          'SL_K N(1,0);'
                          'C_ZAB N(1,0);'
                          'DS_ONK N(1,0);'
                          'ONK_SL N(1,0);'
                          'DS1_T N(1,0);'
                          'STAD N(3,0);'
                          'ONK_T N(3,0);'
                          'ONK_N N(3,0);'
                          'ONK_M N(3,0);'
                          'MTSTZ N(1,0);'
                          'SOD N(5,2);'
                          'K_FR N(2,0);'
                          'WEI N(5,1);'
                          'HEI N(3,0);'
                          'BSA N(4,2);'
                          'B_DIAG C(254);'
                          'B_PROT C(254);'
                          'CONS C(254);'
                          'ONKUSL_ID N(4,0);'
                          'USL_TIP N(1,0);'
                          'HIR_TIP N(1,0);'
                          'LEK_TIP_L N(1,0);'
                          'LEK_TIP_V N(1,0);'
                          'LUCH_TIP N(1,0);'
                          'PPTR N(1,0);'
                          'REGNUM C(6);'
                          'CODE_SH C(10);'
                          'DATE_INJ C(254);'
                          'DATE_IN D;'
                          'DATE_OUT D;'
                          'PRSCSDTBEG D;'
                          'ADRES C(200);'
                          'DATE_MED D;'
                          'CODE_MEDDE N(6,0);'
                          'NUMBER_SER C(100);'
                          ,codepage="cp866")
        table.open(mode=dbf.READ_WRITE)

        for r in self.reestr:
            table.append(r)
        table.close()
        async_to_sync(get_channel_layer().group_send)(self.user_group_name, {'type': 'download', 'text': '{0}.dbf'.format(self.dir)})
        async_to_sync(get_channel_layer().group_send)(self.user_group_name, {'type': 'report_data', 'text': ''})


