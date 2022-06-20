from django.conf import settings
from dbfread import DBF
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import datetime

from hospital.models import (Load_1c,temp_oper, temp_sluch, Sluchay, Oper, Le_trv, Le_Vr, Patient, B_diag, B_prot,
    Disability, Cons, Ksg_kpg, Napr, Onk_sl, Onk_usl, Onmk_li, Onmk_sp, Vb_a, Vb_s, Vds, Oslo, Manpy, Patient_P)


from okb2.models import (F003, Vrzb, otde, V012, Ds, T006, V014, Trs, V001, PY, Vra, F008, V010, Skom, T003, Trvnas,
    V020, V005, F011, Oksm, CJ, V_LGOTY, T004, Rab_Ner, Ws ,MyUser,Statistics_type)

class Insert_temp():
    def __init__(self,user):
        self.user = user
        self.OPER = None
        self.SLUCH = None
        self.rez = dict()
        self.ws_1 = Statistics_type.objects.get(id=2)
        self.ws_2 = Statistics_type.objects.get(id=1)
    def get_dirs(self,user):
        f_oper, f_sluch = list(Load_1c.objects.values_list('oper', 'sluch').filter(user=user))[0]
        dir_oper = settings.MEDIA_ROOT + '/' + f_oper if f_oper != None and f_oper != '' else None
        dir_sluch = settings.MEDIA_ROOT + '/' + f_sluch if f_sluch != None and f_sluch != '' else None
        return (dir_oper, dir_sluch)
    
    def delete_temp_oper(self, user):
        temp_oper.objects.filter(user=user).all().delete()

    def delete_temp_sluch(self, user):
        temp_sluch.objects.filter(user=user).all().delete()
    
    def insert_oper(self, file,user):
        if file is not None:
            self.rez['OPER'] = True
            for rec in DBF(file, char_decode_errors="ignore", encoding="cp866", lowernames=True):
                dict_rec_r = dict(rec)
                kodan = str(dict_rec_r['kodan']).strip(' ')
                kodan = ''.join(kodan)
                try:
                    temp_oper.objects.create(
                        kod_op=dict_rec_r['kod_op'],
                        dato=dict_rec_r['dato'],
                        goc_o=dict_rec_r['goc_o'],
                        py=dict_rec_r['py'],
                        kodx=dict_rec_r['kodx'],
                        kodxa=dict_rec_r['kodxa'],
                        kodxa1=dict_rec_r['kodxa1'],
                        obz=dict_rec_r['obz'],
                        kodan=kodan,
                        pr_osob=dict_rec_r['pr_osob'],
                        k_mm=dict_rec_r['k_mm'],
                        nib=dict_rec_r['nib'],
                        user=user
                    )
                except KeyError:
                    self.rez['OPER'] = False
                    break
    
    def insert_sluch(self, file,user):
   
        self.rez['SLUCH'] = True
        for rec in DBF(file, char_decode_errors="ignore", encoding="cp866", lowernames=True):
            dict_rec_r = dict(rec)
            try:
                tm_let = dict_rec_r['tm_let'] if dict_rec_r['tm_let'] != '' else None
                temp_sluch.objects.create(
                    fam=dict_rec_r['fam'],
                    im=dict_rec_r['im'],
                    ot=dict_rec_r['ot'],
                    pol=dict_rec_r['pol'],
                    datr=dict_rec_r['datr'],
                    udl=dict_rec_r['udl'],
                    s_pasp=dict_rec_r['s_pasp'],
                    n_pasp=dict_rec_r['n_pasp'],
                    ss=dict_rec_r['ss'],
                    c_oksm=dict_rec_r['c_oksm'],
                    adr=dict_rec_r['adr'],
                    m_roj=dict_rec_r['m_roj'],
                    cod_adr=dict_rec_r['cod_adr'],
                    cj=dict_rec_r['cj'],
                    v_lgoty=dict_rec_r['v_lgoty'],
                    in_t=dict_rec_r['in_t'],
                    rab=dict_rec_r['rab'],
                    r_n=dict_rec_r['r_n'],
                    prof=dict_rec_r['prof'],
                    vec=dict_rec_r['vec'],
                    nib=dict_rec_r['nib'],
                    datp=dict_rec_r['datp'],
                    datv=dict_rec_r['datv'],
                    goc=dict_rec_r['goc'],
                    prpg=dict_rec_r['prpg'],
                    vrez=dict_rec_r['vrez'],
                    lpy=dict_rec_r['lpy'],
                    ws=dict_rec_r['ws'],
                    tm_otd=dict_rec_r['tm_otd'],
                    otd=dict_rec_r['otd'],
                    prof_k=dict_rec_r['prof_k'],
                    icx=dict_rec_r['icx'],
                    dsny=dict_rec_r['dsny'],
                    dsk=dict_rec_r['dsk'],
                    dskz=dict_rec_r['dskz'],
                    dsc=dict_rec_r['dsc'],
                    ds_osl=dict_rec_r['ds_osl'],
                    dson=dict_rec_r['dson'],
                    ksg_osn=dict_rec_r['ksg_osn'],
                    ksg_sop=dict_rec_r['ksg_sop'],
                    vid_hmp=dict_rec_r['vid_hmp'],
                    metod_hmp=dict_rec_r['metod_hmp'],
                    trs=dict_rec_r['trs'],
                    tm_let=tm_let,
                    pri=dict_rec_r['pri'],
                    ds_let=dict_rec_r['ds_let'],
                    wskr=dict_rec_r['wskr'],
                    dspat=dict_rec_r['dspat'],
                    rasxp=dict_rec_r['rasxp'],
                    otd_y=dict_rec_r['otd_y'],
                    vds=dict_rec_r['vds'],
                    sctp=dict_rec_r['sctp'],
                    nctp=dict_rec_r['nctp'],
                    t_pol=dict_rec_r['t_pol'],
                    ctkom=dict_rec_r['ctkom'],
                    ksg_ts=dict_rec_r['ksg_ts'],
                    t_trv=dict_rec_r['t_trv'],
                    details=dict_rec_r['details'],
                    trav_ns=dict_rec_r['trav_ns'],
                    pmg=dict_rec_r['pmg'],
                    user=user)
            except KeyError:
                self.rez['SLUCH'] = False
                break

class Load_md():
    def __init__(self,user):
        self.user_group_name = 'hospital_exportfrom1c_%s' % user
        self.user = MyUser.objects.get(id=user)
        self.insert_temp = Insert_temp(self.user.user)
        self.insert_temp.delete_temp_oper(user=user)
        self.insert_temp.delete_temp_sluch(user=user)
        self.dir_oper, self.dir_sluch = self.insert_temp.get_dirs(user=user)
        self.insert_temp.insert_oper(self.dir_oper,user)
        self.insert_temp.insert_sluch(self.dir_sluch,user)


    def load_data(self,user):
        self.sluchay = Sluchay()
        self.YEAR = datetime.datetime.now()
        self.ICX = dict()
        self.ICX[1] = 101
        self.ICX[2] = 303
        self.ICX[3] = 203
        self.ICX[4] = 305
        temp_sluch_list = temp_sluch.objects.values('fam', 'im', 'ot', 'pol', 'datr', 'udl', 's_pasp', 'n_pasp', 'ss', 'c_oksm', 'adr',
                                         'm_roj', 'cod_adr', 'cj', 'v_lgoty', 'in_t', 'rab', 'r_n', 'prof', 'vec', 'nib', 'datp',
                                         'datv', 'goc', 'prpg', 'vrez', 'lpy', 'ws', 'tm_otd', 'otd', 'prof_k', 'icx', 'dsny',
                                         'dsk', 'dskz', 'dsc', 'ds_osl', 'dson', 'ksg_osn', 'ksg_sop', 'vid_hmp', 'metod_hmp', 'trs',
                                         'tm_let', 'pri', 'ds_let', 'wskr', 'dspat', 'rasxp', 'otd_y', 'vds', 'sctp', 'nctp', 't_pol',
                                         'ctkom', 'ksg_ts', 't_trv', 'details', 'trav_ns', 'pmg').filter(user=user).all()

        count_1 = 100/len(temp_sluch_list)
        sm = 0
        for n,s in enumerate(temp_sluch_list):
            sm += count_1
            nib = s['nib']
            datp = datetime.datetime.strptime(str(s['datp']),'%d.%m.%Y')
            if len(Sluchay.objects.filter(nib=nib,datp=datp.date())) == 0:
                oper_data = temp_oper.objects.values('kod_op', 'dato', 'goc_o', 'py', 'kodx', 'kodxa','kodxa1', 'obz', 'kodan', 'pr_osob', 'k_mm', 'nib').filter(nib=s['nib'],user=user)
                sluchay = self.load_data_sluchay(sluchay=s,user=self.user)
                self.load_data_opers(oper_data,sluchay)
                self.load_data_vds(s,sluchay)
                self.load_data_le_trv(s,sluchay)
                self.load_data_le_vr(s,sluchay)
                self.load_data_patient(s,sluchay)
                sluchay.save()
            async_to_sync(get_channel_layer().group_send)(self.user_group_name,
                                                          {'type': 'progress', 'text': sm})
        else:
            async_to_sync(get_channel_layer().group_send)(self.user_group_name,
                                                          {'type': 'report_data', 'text': 'Экспорт из 1с завершён'})

    def load_data_sluchay(self,sluchay,user):
        if sluchay['pmg'] != '':
            try:
                id_pmg = F003.objects.get(kod=sluchay['pmg'])
            except F003.DoesNotExist:
                id_pmg = None
            except F003.MultipleObjectsReturned:
                id_pmg = None
        else:
            id_pmg = None

        if sluchay['lpy'] != '':
            try:
                id_lpy = F003.objects.get(kod=sluchay['lpy'])
            except F003.DoesNotExist:
                id_lpy = None
            except F003.MultipleObjectsReturned:
                id_lpy = None
        else:
            id_lpy = None

        if len(sluchay['datp']) > 0:
            date1 = str(sluchay['datp']).replace(".", "-")
            date1 = datetime.datetime.strptime(date1, "%d-%m-%Y").date()
        else:
            date1 = None
        
        if len(sluchay['datv']) > 0:
            date2 = str(sluchay['datv']).replace(".", "-")
            date2 = datetime.datetime.strptime(date2, "%d-%m-%Y").date()
        else:
            date2 = None
        
        if sluchay['vrez'] != '':
            try:
                id_vrez = Vrzb.objects.get(kod=sluchay['vrez'])
            except Vrzb.DoesNotExist:
                id_vrez = None
            except Vrzb.MultipleObjectsReturned:
                id_vrez = None
        else:
            id_vrez = None
        
        if sluchay['ws'] != '':
            try:
                id_ws = Ws.objects.get(kod=sluchay['ws'])
            except Ws.DoesNotExist:
                id_ws = None
            except Ws.MultipleObjectsReturned:
                id_ws = None
            except:
                id_ws = None
        else:
            id_ws = None
        
        if sluchay['otd'] != '':
            try:
                id_otd = otde.objects.get(kod=sluchay['otd'])
            except otde.DoesNotExist:
                id_otd = None
            except otde.MultipleObjectsReturned:
                otdel = otde.objects.values('id').filter(kod=sluchay['otd'])[0]['id']
                id_otd = otde.objects.get(id=otdel)
        else:
            id_otd = None
        
        if len(sluchay['icx']) > 0:
            try:
                id_iz = self.ICX[int(sluchay['icx'])]
                get_id_ishod = V012.objects.get(id_iz=id_iz)
            except (V012.DoesNotExist, KeyError):
                get_id_ishod = None
            except V012.MultipleObjectsReturned:
                get_id_ishod = None
        else:
            get_id_ishod = None
        
        if sluchay['dsny'] != '':
            try:
                id_dsny = Ds.objects.get(kod=sluchay['dsny'])
            except Ds.DoesNotExist:
                id_dsny = None
            except Ds.MultipleObjectsReturned:
                id_dsny = None
        else:
            id_dsny = None
        
        if sluchay['dsk'] != '':
            try:
                id_dsk = Ds.objects.get(kod=sluchay['dsk'])
            except Ds.DoesNotExist:
                id_dsk = None
            except Ds.MultipleObjectsReturned:
                id_dsk = None
        else:
            id_dsk = None
        
        if sluchay['dskz'] != '':
            try:
                id_dskz = Ds.objects.get(kod=sluchay['dskz'])
            except Ds.DoesNotExist:
                id_dskz = None
            except Ds.MultipleObjectsReturned:
                id_dskz = None
        else:
            id_dskz = None
        
        if sluchay['dsc'] != '':
            try:
                id_dsc = Ds.objects.get(kod=sluchay['dsc'])
            except Ds.DoesNotExist:
                id_dsc = None
            except Ds.MultipleObjectsReturned:
                id_dsc = None
        else:
            id_dsc = None
        
        if sluchay['ds_osl'] != '':
            try:
                id_ds_osl = Ds.objects.get(kod=sluchay['ds_osl'])
            except Ds.DoesNotExist:
                id_ds_osl = None
            except Ds.MultipleObjectsReturned:
                id_ds_osl = None
        else:
            id_ds_osl = None
        
        if sluchay['dson'] != '':
            try:
                id_dson = Ds.objects.get(kod=sluchay['dson'])
            except Ds.DoesNotExist:
                id_dson = None
            except Ds.MultipleObjectsReturned:
                id_dson = None
        else:
            id_dson = None
        
        if sluchay['ksg_osn'] != '':
            try:
                id_ksg_osn = T006.objects.get(code_usl=sluchay['ksg_osn'])
            except T006.DoesNotExist:
                id_ksg_osn = None
            except T006.MultipleObjectsReturned:
                id_ksg_osn = None
        else:
            id_ksg_osn = None
        
        if sluchay['ksg_sop'] != '':
            try:
                id_ksg_sop = T006.objects.get(code_usl=sluchay['ksg_sop'])
            except T006.DoesNotExist:
                id_ksg_sop = None
            except T006.MultipleObjectsReturned:
                id_ksg_sop = None
        else:
            id_ksg_sop = None
        
        if sluchay['goc'] != '':
            try:
                id_goc = V014.objects.get(id_tip=sluchay['goc'])
            except V014.DoesNotExist:
                id_goc = None
            except V014.MultipleObjectsReturned:
                id_goc = None
        else:
            id_goc = None
        
        if sluchay['trs'] != '':
            try:
                id_trs = Trs.objects.get(kod=sluchay['trs'])
            except Trs.DoesNotExist:
                id_trs = None
            except Trs.MultipleObjectsReturned:
                id_trs = None
        else:
            id_trs = None
        
        if sluchay['ds_let'] !='':
            try:
                id_ds_let = Ds.objects.get(kod=sluchay['ds_let'])
            except Ds.DoesNotExist:
                id_ds_let = None
            except Ds.MultipleObjectsReturned:
                id_ds_let = None
        else:
            id_ds_let = None
        
        if sluchay['dspat'] !='':
            try:
                id_dspat = Ds.objects.get(kod=sluchay['dspat'])
            except Ds.DoesNotExist:
                id_dspat = None
            except Ds.MultipleObjectsReturned:
                id_dspat = None
        else:
            id_dspat = None
        
        if sluchay['otd_y'] != '':
            try:
                id_otd_y = otde.objects.get(kod=sluchay['otd_y'])
            except otde.DoesNotExist:
                id_otd_y = None
            except otdel.MultipleObjectsReturned:
                otdel_y = otde.objects.values('id').filter(kod=sluchay['otd_y'])[0]['id']
                id_otd_y = otde.objects.get(id=otdel_y)
        else:
            id_otd_y = None
        
        sluchay_md =  Sluchay.objects.create(
                pmg=id_pmg,
                lpy=id_lpy,
                nib=sluchay['nib'],
                datp=date1,
                datv=date2,
                vrez=id_vrez,
                ws=id_ws,
                tm_otd=sluchay['tm_otd'],
                otd=id_otd,
                icx=get_id_ishod,
                dsny=id_dsny,
                dsk=id_dsk,
                dskz=id_dskz,
                dsc=id_dsc,
                ds_osl=id_ds_osl,
                dson=id_dson,
                ksg_osn=id_ksg_osn,
                ksg_sop=id_ksg_sop,
                vid_hmp=sluchay['vid_hmp'],
                metod_hmp=sluchay['metod_hmp'],
                tm_let=sluchay['tm_let'],
                ds_let=id_ds_let,
                wskr=sluchay['wskr'],
                dspat=id_dspat,
                rasxp=sluchay['rasxp'],
                otd_y=id_otd_y,
                goc=id_goc,
                trs=id_trs,
                )

        if str(sluchay['nib'])[2:4] == '01':
            sluchay_md.statistics_type = self.insert_temp.ws_1
        elif str(sluchay['nib'])[2:4] == '02':
            sluchay_md.statistics_type = self.insert_temp.ws_2
        else:
            sluchay_md.statistics_type = None
        # if id_ws != None and id_ws.kod == 1:
        #     sluchay_md.statistics_type = self.insert_temp.ws_1
        # elif id_ws != None and id_ws.kod == 2 :
        #     sluchay_md.statistics_type = self.insert_temp.ws_2
        # else:
        #     sluchay_md.statistics_type = None

        return sluchay_md
    def load_data_opers(self,oper,sluchay):
        for o in oper:

            if o['kod_op'] != '':
                try:
                    id_kod_op = V001.objects.get(kod=o['kod_op'])
                except V001.DoesNotExist:
                    id_kod_op = None
                except V001.MultipleObjectsReturned:
                    id_kod_op = None
            else:
                id_kod_op = None
            
            if o['obz'] != '':
                try:
                    id_obz = V001.objects.get(kod=o['obz'])
                except V001.DoesNotExist:
                    id_obz = None
                except V001.MultipleObjectsReturned:
                    id_obz = None
            else:
                id_obz = None

            if len(o['dato']) > 0:
                date = str(o['dato']).replace(".", "-")
                date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
            else:
                date = None
            
            if o['py'] != '':
                try:
                    id_py = PY.objects.get(kod=o['py'])
                except PY.DoesNotExist:
                    id_py = None
                except PY.MultipleObjectsReturned:
                    id_py = None
            else:
                id_py = None

            if o['kodx'] != '':
                try:
                    kodx = self._jon(o['kodx'])
                    top_1 = Vra.objects.filter(kod=kodx).values_list('id')[:1]
                    try:
                        id_kodx = Vra.objects.get(id=top_1[0][0])
                    except IndexError:
                        id_kodx = None
                except Vra.DoesNotExist:
                    id_kodx = None
            else:
                id_kodx = None

            if  o['kodxa'] != '':
                        try:
                            kodxa = self._jon(o['kodxa'])
                            top_1 = Vra.objects.filter(kod=kodxa).values_list('id')[:1]
                            try:
                                id_kodxa = Vra.objects.get(id=top_1[0][0])
                            except IndexError:
                                id_kodxa = None
                        except Vra.DoesNotExist:
                            id_kodxa = None
            else:
                id_kodxa = None
            
            if  o['kodxa1'] != '':
                try:
                    kodxa1 = self._jon(o['kodxa1'])
                    top_1 = Vra.objects.filter(kod=kodxa1).values_list('id')[:1]
                    try:
                        id_kodxa1 = Vra.objects.get(id=top_1[0][0])
                    except IndexError:
                        id_kodxa1 = None
                except Vra.DoesNotExist:
                    id_kodxa1 = None
            else:
                id_kodxa1 = None
            
            if o['kodan'] != '':
                try:
                    kodan = self._jon(o['kodan'])
                    top_1 = Vra.objects.filter(kod=kodan).values_list('id')[:1]
                    try:
                        id_kodan = Vra.objects.get(id=top_1[0][0])
                    except IndexError:
                        id_kodan = None
                except Vra.DoesNotExist:
                    id_kodan = None
            else:
                id_kodan = None
            
            if  o['goc_o'] != '':
                try:
                    id_goc = V014.objects.get(id_tip=o['goc_o'])
                except V014.DoesNotExist:
                    id_goc = None
                except V014.MultipleObjectsReturned:
                    id_goc = None
            else:
                id_goc = None
            
            oper_md=Oper.objects.create(
                kod_op=id_kod_op,
                dato=date,
                py=id_py,
                kodx=id_kodx,
                kodxa=id_kodxa,
                kodxa1=id_kodxa1,
                obz=id_obz,
                kodan=id_kodan,
                goc=id_goc)

            sluchay.oper.add(oper_md)
    def load_data_vds(self,vds,sluchay):

        if vds['t_pol'] != '':
            try:
                id_t_pol = F008.objects.get(id_tip=vds['t_pol'])
            except F008.DoesNotExist:
                id_t_pol = None
            except F008.MultipleObjectsReturned:
                id_t_pol = None
        else:
            id_t_pol = None

        if vds['vds'] != '':
            try:
                id_vds = V010.objects.get(spname=vds['vds'])
            except V010.DoesNotExist:
                id_vds = None
            except V010.MultipleObjectsReturned:
                id_vds = None
        else:
            id_vds = None
        
        if vds['ctkom'] != '':
            try:
                id_ctkom = Skom.objects.get(kod=vds['ctkom'])
            except Skom.DoesNotExist:
                id_ctkom = None
            except Skom.MultipleObjectsReturned:
                id_ctkom = None
        else:
            id_ctkom = None
        
        if vds['ksg_ts'] != '':
            try:
                id_ksg_ts = T003.objects.get(kod=vds['ksg_ts'])
            except T003.DoesNotExist:
                id_ksg_ts = None
            except T003.MultipleObjectsReturned:
                id_ksg_ts = None
        else:
            id_ksg_ts = None
        
        vds_md = Vds.objects.create(
            t_pol=id_t_pol,
            vds=id_vds,
            ctkom=id_ctkom,
            sctp=vds['sctp'],
            nctp=vds['nctp'],
            ksg_ts=id_ksg_ts)
        
        sluchay.vds = vds_md  
    def load_data_le_trv(self,le_trv,sluchay):

        if le_trv['t_trv'] != '':
            try:
                id_t_trv = Ds.objects.get(kod=le_trv['t_trv'])
            except Ds.DoesNotExist:
                id_t_trv = None
            except Ds.MultipleObjectsReturned:
                id_t_trv = None
        else:
            id_t_trv = None
        
        if le_trv['details'] != '':
            try:
                id_details = Ds.objects.get(kod=le_trv['details'])
            except Ds.DoesNotExist:
                id_details = None
            except Ds.MultipleObjectsReturned:
                id_details = None
        else:
            id_details = None
        
        if le_trv['trav_ns'] != '' and le_trv['trav_ns'] != None:
            try:
                id_trav_ns = Trvnas.objects.get(kod=le_trv['trav_ns'])
            except Trvnas.DoesNotExist:
                id_trav_ns = None
            except Trvnas.MultipleObjectsReturned:
                id_trav_ns = None
        else:
            id_trav_ns = None
        

        le_trv_md = Le_trv.objects.create(
            t_trv=id_t_trv,
            details=id_details,
            )
        sluchay.le_trv = le_trv_md
    def load_data_le_vr(self,le_vr,sluchay):
        if le_vr['prof_k'] != '':
            try:
                id_prof_k = V020.objects.get(idk_pr=le_vr['prof_k'])
            except V020.DoesNotExist:
                id_prof_k = None
            except V020.MultipleObjectsReturned:
                id_prof_k = None
        else:
            id_prof_k = None
        
        le_vr_md =  Le_Vr.objects.create(
        prof_k=id_prof_k
        )
        sluchay.le_vr = le_vr_md
    def load_data_patient(self,patient,sluchay):
        
        if len(patient['datr']) > 0:
            date = str(patient['datr']).replace(".", "-")
            date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
        else:
            date = None

        if date != None:
            if self.YEAR.year > date.year:
                vs = self.YEAR.year - date.year
                nvs = 'Л'
            elif self.YEAR.year == date.year:
                if int(date.month) < int(self.YEAR.month):
                    vs = self.YEAR.month - date.month
                    nvs = 'М'
                else:
                    vs = self.YEAR.day - date.day
                    nvs = 'Д'
            else:
                vs = None
                nvs = None
        else:
            vs = None
            nvs = None

        try:
            id_pol = V005.objects.get(id_pol=patient['pol'])
        except V005.DoesNotExist:
            id_pol = None
        except V005.MultipleObjectsReturned:
            id_pol = None

        if patient['udl'] != '':
            try:
                id_udl = F011.objects.get(id_doc=patient['udl'])
            except F011.DoesNotExist:
                id_udl = None
            except F011.MultipleObjectsReturned:
                id_udl = None
        else:
            id_udl = None

        if patient['c_oksm'] != '':
            try:
                id_c_oksm = Oksm.objects.get(kod=patient['c_oksm'])
            except Oksm.DoesNotExist:
                id_c_oksm = None
            except Oksm.MultipleObjectsReturned:
                id_c_oksm = None
        else:
            id_c_oksm = None
        
        if patient['cj'] != '':
            try:
                id_cj = CJ.objects.get(kod=patient['cj'])
            except CJ.DoesNotExist:
                id_cj = None
            except CJ.MultipleObjectsReturned:
                id_cj = None
        else:
            id_cj = None

        if patient['v_lgoty'] != '':
            try:
                id_v_lgoty = V_LGOTY.objects.get(kod=patient['v_lgoty'])
            except V_LGOTY.DoesNotExist:
                id_v_lgoty = None
            except V_LGOTY.MultipleObjectsReturned:
                id_v_lgoty = None
        else:
            id_v_lgoty = None
        
        if patient['in_t'] != '':
            try:
                id_in_t = T004.objects.get(kod=patient['in_t'])
            except T004.DoesNotExist:
                id_in_t = None
            except T004.MultipleObjectsReturned:
                id_in_t = None
        else:
            id_in_t = None

        if patient['r_n'] != '':
            try:
                id_r_n = Rab_Ner.objects.get(kod=patient['r_n'])
            except Rab_Ner.DoesNotExist:
                id_r_n = None
            except Rab_Ner.MultipleObjectsReturned:
                id_r_n = None
        else:
            id_r_n = None
        
        if patient['vec'] == '':
            vec = 0
        else:
            vec = patient['vec']

        patient_md = Patient.objects.create(
                fam=patient['fam'],
                im=patient['im'],
                ot=patient['ot'],
                pol=id_pol,
                datr=date,
                vs=vs,
                nvs=nvs,
                udl=id_udl,
                s_pasp=patient['s_pasp'],
                n_pasp=patient['n_pasp'],
                ss=patient['ss'],
                cod_adr=patient['cod_adr'],
                c_oksm=id_c_oksm,
                adr=patient['adr'],
                m_roj=patient['m_roj'],
                cj=id_cj,
                v_lgoty=id_v_lgoty,
                in_t=id_in_t,
                rab=patient['rab'],
                r_n=id_r_n,
                prof=patient['prof'],
                vec=vec
                )
        patient_md.sluchay.add(sluchay)
        patient_md.save()
        # patient_md = Patient()
        # patient_md.fam=patient['fam']
        # patient_md.im=patient['im']
        # patient_md.ot=patient['ot']
        # patient_md.pol=id_pol
        # patient_md.datr=date
        # patient_md.vs=vs
        # patient_md.nvs=nvs
        # patient_md.udl=id_udl
        # patient_md.s_pasp=patient['s_pasp']
        # patient_md.n_pasp=patient['n_pasp']
        # patient_md.ss=patient['ss']
        # patient_md.cod_adr=patient['cod_adr']
        # patient_md.c_oksm=id_c_oksm
        # patient_md.adr=patient['adr']
        # patient_md.m_roj=patient['m_roj']
        # patient_md.cj=id_cj
        # patient_md.v_lgoty=id_v_lgoty
        # patient_md.in_t=id_in_t
        # patient_md.rab=patient['rab']
        # patient_md.r_n=id_r_n
        # patient_md.prof=patient['prof']
        # patient_md.vec=vec
        # patient_md.sluchay.add(sluchay)
        # patient_md.save()

    def _jon(self, s):
        l = str(s).split()
        j = ''.join(l)
        return j

    def clear_md(self):
        B_diag.objects.all().delete()
        B_prot.objects.all().delete()
        Disability.objects.all().delete()        
        Cons.objects.all().delete()
        Ksg_kpg.objects.all().delete()
        Napr.objects.all().delete()
        Onk_sl.objects.all().delete()
        Onk_usl.objects.all().delete()
        Onmk_li.objects.all().delete()
        Onmk_sp.objects.all().delete()
        Vb_a.objects.all().delete()
        Vb_s.objects.all().delete()
        Sluchay.objects.all().delete()
        Vds.objects.all().delete()
        Le_Vr.objects.all().delete()
        Le_trv.objects.all().delete()
        Oper.objects.all().delete()
        Oslo.objects.all().delete()
        Manpy.objects.all().delete()
        Disability.objects.all().delete()
        Patient_P.objects.all().delete()
        Patient.objects.all().delete()