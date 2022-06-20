from django.conf import settings
from dbfread import DBF
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import datetime

from hospital.models import *
from okb2.models import *
from services.hospital.save_oper_sluch import Insert_temp


class Load_md():
    debug_is_1c = False
    def __init__(self,user):
        self.user_group_name = 'hospital_exportfrom1c_%s' % user
        self.user = MyUser.objects.get(id=user)
        self.insert_temp = Insert_temp(self.user.user)
        # self.insert_temp.delete_temp_oper(user=user)
        # self.insert_temp.delete_temp_sluch(user=user)
        self.delete_temp_monitoring_res()
        # self.delete_temp_monitoring_res_10()
        self.dir_oper, self.dir_sluch = self.insert_temp.get_dirs(user=self.user.user)
        self.dir_sluch_10 = self.get_dirs(user=self.user.user)
        self.insert_temp_monitoring()
        # self.insert_temp.insert_oper(self.dir_oper, user)
        # self.insert_monitoring_res(self.dir_sluch,self.dir_oper,self.user.user)

        self.ICX = dict()
        self.ICX[1] = 101
        self.ICX[2] = 303
        self.ICX[3] = 203
        self.ICX[4] = 305
        #Пометка на удоления тестовых записей
        # self.debug_is_1c = True


    def delete_temp_monitoring_res(self):
        temp_monitoring_res.objects.filter(user=self.user.user).all().delete()

    def delete_temp_monitoring_res_10(self):
        temp_monitoring_res_10.objects.filter(user=self.user.user).all().delete()

    def get_dirs(self, user):
        f_sluch_10 = list(Load_1c.objects.values_list('sluch_10').filter(user=user))[0]
        dir_sluch_10 = settings.MEDIA_ROOT + '/' + f_sluch_10[0] if f_sluch_10[0] != None and f_sluch_10[0] != '' else None
        return dir_sluch_10

    def insert_monitoring_res(self,file_sl,user,oper,load):
        if load:
            for rec in DBF(file_sl, char_decode_errors="ignore", encoding="cp866", lowernames=True):
                rec.update({'user': user})
                temp_monitoring_res.objects.create(**rec)
            # temp_monitoring_res_10.objects.create(**rec)
        if oper:
            if self.user.ws.kod == 1:
                sluchs = temp_sluch.objects.values('id').filter(nib__istartswith='0201',user=self.user.user)
            elif self.user.ws.kod == 2:
                sluchs = temp_sluch.objects.values('id').filter(nib__istartswith='0202',user=self.user.user)

            count_1 = 100 / sluchs.count()
            sm = 0
            for s in sluchs:
                sm += count_1
                temp = temp_sluch.objects.get(id=s['id'])
                datp = datetime.datetime.strptime(str(temp.datp), '%d.%m.%Y')
                if len(Sluchay.objects.filter(nib=temp.nib,datp=datp.date())) == 0:
                    oper_data = temp_oper.objects.values('kod_op', 'dato', 'goc_o', 'py', 'kodx', 'kodxa',
                                                         'kodxa1', 'obz', 'kodan', 'pr_osob', 'k_mm',
                                                         'nib').filter(nib=temp.nib, user=self.user.user)
                    sl = self.create_data_sluchay(temp)
                    self.create_data_oper(oper_data,sl)
                    vds = self.create_data_vds(temp,sl)
                    self.create_data_trv(temp,sl)
                    self.create_data_le_vr(temp,sl)
                    patient = self.create_data_patient(temp,sl)
                    sl.save()
                    try:
                        try:
                            monitoring = temp_monitoring_res.objects.get(nhistory=temp.nib,date_1=datp.date(),block_cd='S')
                        except temp_monitoring_res.MultipleObjectsReturned:
                            monitoring = temp_monitoring_res.objects.filter(nhistory=temp.nib,date_1=datp.date(),block_cd='S')[0]
                        self.create_sluchay(monitoring,sl,False)
                        self.create_patient(monitoring,patient,False)
                        self.create_vds(monitoring,vds,False)
                        patient_p = self.create_patient_pr(monitoring)
                        patient.patient_p = patient_p
                        patient.save()
                        self.create_le_vr(monitoring,sl.le_vr,False)
                        sl.le_vr.save()

                        try:
                            monitoring_i_all = temp_monitoring_res.objects.values('id').filter(sl_id=monitoring.sl_id, block_cd='I')
                            if monitoring_i_all.count() > 0:
                                for m in monitoring_i_all:
                                    data = temp_monitoring_res.objects.get(id=m['id'])
                                    self.create_implants(data,None,sl,True)
                        except temp_monitoring_res.DoesNotExist:
                            pass

                    except temp_monitoring_res.DoesNotExist:
                        pass


                async_to_sync(get_channel_layer().group_send)(self.user_group_name,{'type': 'progress', 'text': sm})
            else:
                async_to_sync(get_channel_layer().group_send)(self.user_group_name,{'type': 'report_data', 'text': 'Экспорт из 1с завершён'})
        else:
            if self.user.ws.kod == 1:
                monitoring =  temp_monitoring_res.objects.values('id').filter(nhistory__istartswith='0201',block_cd='S',user=self.user.user)
            else:
                monitoring = temp_monitoring_res.objects.values('id').filter(nhistory__istartswith='0202',block_cd='S', user=self.user.user)

            count_1 = 100/monitoring.count()
            sm = 0
            for m in monitoring:
                sm += count_1
                temp = temp_monitoring_res.objects.get(id=m['id'])
                if Sluchay.objects.filter(nib=temp.nhistory,datp=temp.date_1).count() == 0:
                    data = temp_monitoring_res.objects.values('id').filter(id=m['id'])
                    for d in data:
                        res = temp_monitoring_res.objects.get(id=d['id'])
                        if res.block_cd == 'S':
                            sluchay = self.create_sluchay(res,None,True)
                            patient = self.create_patient(res,None,True)
                            vds = self.create_vds(res,None,True)
                            le_vr = self.create_le_vr(res,None,True)
                            patient_p = self.create_patient_pr(res)

                            sluchay.vds = vds
                            sluchay.le_vr = le_vr
                            sluchay.save()
                            patient.sluchay.add(sluchay)
                            patient.patient_p = patient_p
                            patient.save()

                            try:
                                monitoring_i_all = temp_monitoring_res.objects.values('id').filter(sl_id=res.sl_id, block_cd='I')
                                if monitoring_i_all.count() > 0:
                                    for m in monitoring_i_all:
                                        data = temp_monitoring_res.objects.get(id=m['id'])
                                        self.create_implants(data, None, sluchay, True)
                            except temp_monitoring_res.DoesNotExist:
                                pass
                        elif res.block_cd == 'U':
                            pass
                else:
                    data = temp_monitoring_res.objects.values('id').filter(id=m['id'])
                    for d in data:
                        res = temp_monitoring_res.objects.get(id=d['id'])
                        if res.block_cd == 'S':
                            try:
                                sl_update = Sluchay.objects.get(nib=res.nhistory,datp=res.date_1,update_user=None)
                                self.create_sluchay(res,sl_update,False)
                                self.create_patient(res,Patient.objects.get(sluchay=sl_update), False)
                                self.create_vds(res,sl_update.vds, False)
                                self.create_le_vr(res,sl_update.le_vr,False)
                                try:
                                    monitoring_i_all = temp_monitoring_res.objects.values('id').filter(sl_id=res.sl_id,block_cd='I')
                                    if monitoring_i_all.count() > 0:
                                        for m in monitoring_i_all:
                                            data = temp_monitoring_res.objects.get(id=m['id'])
                                            self.create_implants(data, None, sl_update, True)
                                except temp_monitoring_res.DoesNotExist:
                                    pass
                            except:
                                pass


                async_to_sync(get_channel_layer().group_send)(self.user_group_name,{'type': 'progress', 'text': sm})
            else:
                async_to_sync(get_channel_layer().group_send)(self.user_group_name,{'type': 'report_data', 'text': 'Экспорт из 1с завершён'})


    def create_sluchay(self,data,sluchay,create_update):
        if create_update:
            sluchay = Sluchay()

        sluchay.usl_ok = data.usl_ok
        sluchay.vidpom = data.vidpom
        try:
            sluchay.goc = V014.objects.get(id_tip=data.for_pom,dateend=None)
        except V014.DoesNotExist:
            sluchay.goc = None
        sluchay.vid_hmp = data.vid_hmp
        sluchay.metod_hmp = data.metod_hmp
        if sluchay.lpy is None:
            try:
                sluchay.lpy = F003.objects.get(mo=data.npr_mo,dateend=None)
            except F003.DoesNotExist:
                sluchay.lpy = None
            except F003.MultipleObjectsReturned:
                sluchay.lpy = None

        sluchay.lpu_1 = data.lpu_1
        sluchay.podr = data.podr
        sluchay.det = data.det
        sluchay.tal_d = data.tal_d
        sluchay.tal_p = data.tal_p
        sluchay.tal_num = data.tal_num
        sluchay.nib = data.nhistory
        sluchay.datp = data.date_1
        sluchay.datv = data.date_2

        try:
            sluchay.p_per = PER.objects.get(kod=data.p_per,dateend=None)
        except PER.DoesNotExist:
            sluchay.p_per = None
        except PER.MultipleObjectsReturned:
            sluchay.p_per = None
        try:
            sluchay.dskz = Ds.objects.get(kod=data.ds1,dateend=None)
        except Ds.DoesNotExist:
            sluchay.dskz = None

        try:
            sluchay.ds_0 = Ds.objects.get(kod=data.ds0,dateend=None)
        except Ds.DoesNotExist:
            sluchay.ds_0 = None


        sluchay.ds2 = data.ds2
        sluchay.ds2_n = data.ds2_n
        sluchay.ds3 = data.ds3
        sluchay.code_mes1 = data.code_mes1
        sluchay.code_mes2 = data.code_mes2
        try:
            sluchay.rslt = V009.objects.get(id_tip=data.rslt,dateend=None)
        except V009.DoesNotExist:
            sluchay.rslt = None
        except V009.MultipleObjectsReturned:
            sluchay.rslt = None
        try:
            sluchay.icx = V012.objects.get(id_iz=data.ishod,dateend=None)
        except V012.DoesNotExist:
            sluchay.icx = None
        except V012.MultipleObjectsReturned:
            sluchay.icx = None
        sluchay.idsp = data.idsp
        sluchay.ed_col = data.ed_col
        sluchay.kol_usl = data.kol_usl
        sluchay.crit = data.crit
        sluchay.n_ksg = data.n_ksg
        sluchay.vb_p = data.vb_p
        sluchay.reab = data.reab
        sluchay.dn = data.dn
        sluchay.p_cel = data.p_cel
        sluchay.profil_k = data.profil_k

        try:
            sluchay.prpg = Prpg.objects.get(id=1, dateend=None)
        except Prpg.DoesNotExist:
            sluchay.prpg = None
        try:
            if sluchay.oper.count() > 0:
                opers=[Oper.objects.get(id=s['id']) for s in sluchay.oper.values('id')]
                oper = [(o.id,o.kod_op.kod) for o in opers if o.kod_op != None and o.kod_op.kod == data.vid_vme]
                if len(oper) > 0:
                    ope = Oper.objects.get(id=oper[0][0])
                    ope.pop = True
                    ope.save()
        except:
            pass

        if Load_md.debug_is_1c:
            sluchay.is_1c = True
        sluchay.statistics_type = self.user.statistics_type
        sluchay.save()
        return sluchay
    def create_patient(self,data,patient,create_update):
        self.YEAR = datetime.datetime.now()
        if create_update:
            patient = Patient()
        patient.fam = data.fam
        patient.im = data.im
        patient.ot = data.ot
        patient.novor = data.novor
        patient.vec = data.vnov_d
        try:
            patient.pol = V005.objects.get(id_pol=data.w,dateend=None)
        except V005.DoesNotExist:
            patient.pol = None
        if data.dr is not None:
            patient.datr = data.dr
            if self.YEAR.year > data.dr.year:
                patient.vs = self.YEAR.year - data.dr.year
                patient.nvs = 'Л'
            elif self.YEAR.year == data.dr.year:
                if int(data.dr.month) < int(self.YEAR.month):
                    patient.vs = self.YEAR.month - data.dr.month
                    patient.nvs = 'М'
                else:
                    patient.vs = self.YEAR.day - data.dr.day
                    patient.nvs = 'Д'
        patient.tel = data.tel
        patient.m_roj = data.mr
        try:
            patient.udl = F011.objects.get(id_doc=int(data.doctype),dateend=None) if data.doctype != '' else None
        except F011.DoesNotExist:
            patient.udl = None
        except F011.MultipleObjectsReturned:
            patient.udl = None
        patient.s_pasp = data.docser
        patient.n_pasp = data.docnum
        patient.docdate = data.docdate
        patient.docorg = data.docorg
        patient.ss = data.snils
        patient.okatog = data.okatog
        patient.okatop = data.okatop
        patient.adr = data.adres
        if Load_md.debug_is_1c:
            patient.is_1c = True
        patient.save()
        return patient
    def create_vds(self,data,vds,create_update):
        if create_update:
            vds = Vds()
        try:
            vds.t_pol = F008.objects.get(id_tip=data.vpolis,dateend=None)
        except F008.DoesNotExist:
            vds.t_pol = None
        except F008.MultipleObjectsReturned:
            vds.t_pol = None
        vds.sctp = data.spolis
        vds.nctp = data.npolis
        vds.vds = Isfin.objects.get(naim='OМС(КСГ базов.программа)', dateend=None)
        #ST_OKATO
        try:
            vds.ctkom = Skom.objects.get(smo=str(float(data.smo)),dateend=None) if data.smo != '' else None
        except Skom.DoesNotExist:
            vds.ctkom = None
        except Skom.MultipleObjectsReturned:
            vds.ctkom = None
        if Load_md.debug_is_1c:
            vds.is_1c = True
        vds.save()
        return vds
    def create_le_vr(self,data,le_vr,create_update):
        if create_update:
            le_vr = Le_Vr()
        le_vr.kd = data.kd
        le_vr.kd_z = data.kd_z
        try:
            le_vr.prof_k = V020.objects.get(idk_pr=data.profil_k,dateend=None)
        except V020.DoesNotExist:
            le_vr.prof_k = None
        try:
            v = Vra.objects.values('id').filter(t005=str(data.iddokt).split(" ")[1],dateend=None)[:1]
            if v.count() > 0:
                le_vr.kod = Vra.objects.get(id=v[0]['id'])
            else:
                le_vr.kod = None
        except IndexError:
            le_vr.kod = None


        if Load_md.debug_is_1c:
            le_vr.is_1c = True
        le_vr.save()
        return le_vr
    def create_implants(self,data,implant,sl,create_implant):
        if create_implant:
            implant = Med_dev()
        implant.date = data.date_med if data.date_med != None and data.date_med != "" else None
        try:
            implant.code = Code_med_dev.objects.get(rzn=data.codemeddev)
        except Code_med_dev.DoesNotExist:
            implant.code = None
        implant.number_ser = data.number_ser if data.number_ser != None and data.number_ser != "" else None
        if Load_md.debug_is_1c:
            implant.is_1c = True
        implant.save()
        sl.med_dev.add(implant)
        sl.save()

    def create_patient_pr(self,data):
        if data.fam_p != '' or data.im_p != '' or data.ot_p != '':
            patient_p = Patient_P()
            patient_p.fam_p = data.fam_p
            patient_p.im_p = data.im_p
            patient_p.ot_p = data.ot_p
            try:
                patient_p.pol = V005.objects.get(id_pol=data.w_p, dateend=None)
            except V005.DoesNotExist:
                patient_p.pol = None
            patient_p.datr = data.dr_p
            if Load_md.debug_is_1c:
                patient_p.is_1c = True
            patient_p.save()
            return patient_p
        return None
    def create_opers(self,oper,sluchay):
        for o in oper:

            if o['kod_op'] != '':
                try:
                    id_kod_op = V001.objects.get(kod=o['kod_op'],dateend=None)
                except V001.DoesNotExist:
                    id_kod_op = None
                except V001.MultipleObjectsReturned:
                    id_kod_op = None
            else:
                id_kod_op = None

            if o['obz'] != '':
                try:
                    id_obz = V001.objects.get(kod=o['obz'],dateend=None)
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
                    id_py = PY.objects.get(kod=o['py'],dateend=None)
                except PY.DoesNotExist:
                    id_py = None
                except PY.MultipleObjectsReturned:
                    id_py = None
            else:
                id_py = None

            if o['kodx'] != '':
                try:
                    kodx = self._jon(o['kodx'])
                    top_1 = Vra.objects.filter(kod=kodx,dateend=None).values_list('id')[:1]
                    try:
                        id_kodx = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodx = None
                except Vra.DoesNotExist:
                    id_kodx = None
            else:
                id_kodx = None

            if o['kodxa'] != '':
                try:
                    kodxa = self._jon(o['kodxa'])
                    top_1 = Vra.objects.filter(kod=kodxa,dateend=None).values_list('id')[:1]
                    try:
                        id_kodxa = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodxa = None
                except Vra.DoesNotExist:
                    id_kodxa = None
            else:
                id_kodxa = None

            if o['kodxa1'] != '':
                try:
                    kodxa1 = self._jon(o['kodxa1'])
                    top_1 = Vra.objects.filter(kod=kodxa1).values_list('id')[:1]
                    try:
                        id_kodxa1 = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodxa1 = None
                except Vra.DoesNotExist:
                    id_kodxa1 = None
            else:
                id_kodxa1 = None

            if o['kodan'] != '':
                try:
                    kodan = self._jon(o['kodan'])
                    top_1 = Vra.objects.filter(kod=kodan,dateend=None).values_list('id')[:1]
                    try:
                        id_kodan = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodan = None
                except Vra.DoesNotExist:
                    id_kodan = None
            else:
                id_kodan = None

            if o['goc_o'] != '':
                try:
                    id_goc = V014.objects.get(id_tip=o['goc_o'],dateend=None)
                except V014.DoesNotExist:
                    id_goc = None
                except V014.MultipleObjectsReturned:
                    id_goc = None
            else:
                id_goc = None

            if Load_md.debug_is_1c:
                is_1c = True
            else:
                is_1c = None

            oper_md = Oper.objects.create(
                kod_op=id_kod_op,
                dato=date,
                py=id_py,
                kodx=id_kodx,
                kodxa=id_kodxa,
                kodxa1=id_kodxa1,
                obz=id_obz,
                kodan=id_kodan,
                goc=id_goc,
                is_1c=is_1c
            )
            sluchay.oper.add(oper_md)
            sluchay.save()
    def _jon(self, s):
        l = str(s).split()
        j = ''.join(l)
        return j
    def insert_temp_monitoring(self):
        temp_oper.objects.filter(user=self.user.user).all().delete()
        temp_sluch.objects.filter(user=self.user.user).all().delete()
        temp_monitoring_res.objects.filter(user=self.user.user).all().delete()
        if self.dir_sluch is not None and self.dir_oper is not None and self.dir_sluch_10 is not None:
            self.insert_temp.insert_oper(self.dir_oper, self.user.user)
            self.insert_temp.insert_sluch(self.dir_sluch,self.user.user)
            self.insert_monitoring_res(self.dir_sluch_10,self.user.user,True,True)
        elif self.dir_sluch is not None and self.dir_oper is not None and self.dir_sluch_10 == None:
            self.insert_temp.insert_oper(self.dir_oper, self.user.user)
            self.insert_temp.insert_sluch(self.dir_sluch, self.user.user)
            self.insert_monitoring_res(self.dir_sluch_10, self.user.user, True,False)
        elif self.dir_sluch == None and self.dir_oper == None and self.dir_sluch_10 is not None :
            self.insert_monitoring_res(self.dir_sluch_10,self.user.user,False,True)

    def update_sluch_patient(self,sluchay,patient,le_vr,vds,data):
        if vds.t_pol is None:
            try:
                vds.t_pol = F008.objects.get(id_tip=data.t_pol,dateend=None) if data.t_pol != '' else None
            except F008.DoesNotExist:
                vds.t_pol = None
            except F008.MultipleObjectsReturned:
                vds.t_pol = None
        if vds.vds is None:
            try:
                vds.vds = V010.objects.get(spname=data.vds,dateend=None) if data.vds != '' else None
            except V010.DoesNotExist:
                vds.vds = None
            except V010.MultipleObjectsReturned:
                vds.vds = None
        if vds.ctkom is None:
            try:
                vds.ctkom = Skom.objects.get(kod=data.ctkom,dateend=None) if data.ctkom != '' else None
            except Skom.DoesNotExist:
                vds.ctkom = None
            except Skom.MultipleObjectsReturned:
                vds.ctkom = None
        if vds.ksg_ts is None:
            try:
                vds.ksg_ts = T003.objects.get(kod=data.ksg_ts,dateend=None) if data.ksg_ts != '' else None
            except T003.DoesNotExist:
                vds.ksg_ts = None
            except T003.MultipleObjectsReturned:
                vds.ksg_ts = None

        vds.save()

        if le_vr.prof_k is None:
            try:
                le_vr.prof_k = V020.objects.get(idk_pr=data.prof_k,dateend=None) if data.prof_k != '' else None
            except V020.DoesNotExist:
                le_vr.prof_k = None
            except V020.MultipleObjectsReturned:
                le_vr.prof_k = None

        le_vr.save()

        if patient.c_oksm is None:
            try:
                patient.c_oksm = Oksm.objects.get(kod=data.c_oksm,dateend=None) if data.c_oksm != '' else None
            except Oksm.DoesNotExist:
                patient.c_oksm = None
            except Oksm.MultipleObjectsReturned:
                patient.c_oksm = None

        if patient.c_oksm is None:
            try:
                patient.c_oksm = Oksm.objects.get(id=189,dateend=None)
            except Oksm.DoesNotExist:
                patient.c_oksm = None


        if patient.cj is None:
            try:
                patient.cj = CJ.objects.get(kod=data.cj,dateend=None) if data.cj != '' else None
            except CJ.DoesNotExist:
                patient.cj = None
            except CJ.MultipleObjectsReturned:
                patient.cj = None

        if patient.v_lgoty is None:
            try:
                patient.v_lgoty = V_LGOTY.objects.get(kod=data.v_lgoty,dateend=None) if data.v_lgoty != '' else None
            except V_LGOTY.DoesNotExist:
                patient.v_lgoty = None
            except V_LGOTY.MultipleObjectsReturned:
                patient.v_lgoty = None

        if patient.in_t is None:
            try:
                patient.in_t = T004.objects.get(kod=data.in_t,dateend=None) if data.in_t != '' else None
            except T004.DoesNotExist:
                patient.in_t = None
            except T004.MultipleObjectsReturned:
                patient.in_t = None

        if patient.r_n is None:
            try:
                patient.r_n = Rab_Ner.objects.get(kod=data.r_n,dateend=None) if data.r_n != '' else None
            except Rab_Ner.DoesNotExist:
                patient.r_n = None
            except Rab_Ner.MultipleObjectsReturned:
                patient.r_n = None

        patient.save()

        if sluchay.npr_date is None:
            sluchay.npr_date = data.npr_date


        # if sluchay.pmg is None:
        #     try:
        #         sluchay.pmg = F003.objects.get(mo=data.pmg) if data.pmg != '' else None
        #     except F003.DoesNotExist:
        #         sluchay.pmg = None
        #     except F003.MultipleObjectsReturned:
        #         sluchay.pmg

        # if sluchay.lpy is None:
        #     try:
        #         sluchay.lpy = F003.objects.get(mo=data.lpy) if data.lpy != '' else None
        #     except F003.DoesNotExist:
        #         sluchay.lpy = None
        #     except F003.MultipleObjectsReturned:
        #         sluchay.lpy = None

        if sluchay.vrez is None:
            try:
                sluchay.vrez = Vrzb.objects.get(kod=data.vrez,dateend=None) if data.vrez != '' else None
            except Vrzb.DoesNotExist:
                sluchay.vrez = None
            except Vrzb.MultipleObjectsReturned:
                sluchay.vrez = None

        if sluchay.ws is None:
            try:
                sluchay.ws = Ws.objects.get(kod=data.ws,dateend=None) if data.ws != '' else None
            except Ws.DoesNotExist:
                sluchay.ws = None
            except Ws.MultipleObjectsReturned:
                sluchay.ws = None
            except:
                sluchay.ws = None

        if sluchay.otd is None:
            try:
                sluchay.otd = otde.objects.get(kod=data.otd,dateend=None) if data.otd != '' else None
            except otde.DoesNotExist:
                sluchay.otd = None
            except otde.MultipleObjectsReturned:
                otdel = otde.objects.values('id').filter(kod=data.otd,dateend=None)[0]['id']
                sluchay.otd = otde.objects.get(id=otdel,dateend=None)

        if sluchay.dsny is None:
            try:
                sluchay.dsny = Ds.objects.get(kod=data.dsny,dateend=None) if data.dsny != '' else None
            except Ds.DoesNotExist:
                sluchay.dsny = None
            except Ds.MultipleObjectsReturned:
                sluchay.dsny = None

        if sluchay.dsk is None:
            try:
                sluchay.dsk = Ds.objects.get(kod=data.dsk,dateend=None) if data.dsk != '' else None
            except Ds.DoesNotExist:
                sluchay.dsk = None
            except Ds.MultipleObjectsReturned:
                sluchay.dsk = None

        if sluchay.dsc is None:
            try:
                sluchay.dsc = Ds.objects.get(kod=data.dsc,dateend=None) if data.dsc != '' else None
            except Ds.DoesNotExist:
                sluchay.dsc = None
            except Ds.MultipleObjectsReturned:
                sluchay.dsc = None

        if sluchay.ds_osl is None:
            try:
                sluchay.ds_osl = Ds.objects.get(kod=data.ds_osl,dateend=None) if data.ds_osl != '' else None
            except Ds.DoesNotExist:
                sluchay.ds_osl = None
            except Ds.MultipleObjectsReturned:
                sluchay.ds_osl = None

        if sluchay.dson is None:
            try:
                sluchay.dson = Ds.objects.get(kod=data.dson,dateend=None) if data.dson != '' else None
            except Ds.DoesNotExist:
                sluchay.dson = None
            except Ds.MultipleObjectsReturned:
                sluchay.dson = None

        # if sluchay.ksg_osn is None:
        #     try:
        #         sluchay.ksg_osn = T006.objects.get(code_usl=data.ksg_osn) if data.ksg_osn != '' else None
        #     except T006.DoesNotExist:
        #         sluchay.ksg_osn = None
        #     except T006.MultipleObjectsReturned:
        #         sluchay.ksg_osn = None
        #
        # if sluchay.ksg_sop is None:
        #     try:
        #         sluchay.ksg_sop = T006.objects.get(code_usl=data.ksg_sop) if data.ksg_sop != '' else None
        #     except T006.DoesNotExist:
        #         sluchay.ksg_sop = None
        #     except T006.MultipleObjectsReturned:
        #         sluchay.ksg_sop = None

        if sluchay.goc is None:
            try:
                sluchay.goc = V014.objects.get(id_tip=data.goc,dateend=None) if data.goc != '' else None
            except V014.DoesNotExist:
                sluchay.goc = None
            except V014.MultipleObjectsReturned:
                sluchay.goc = None

        if sluchay.trs is None:
            try:
                sluchay.trs = Trs.objects.get(kod=data.trs,dateend=None) if data.trs != '' else None
            except Trs.DoesNotExist:
                sluchay.trs = None
            except Trs.MultipleObjectsReturned:
                sluchay.trs = None

        if sluchay.ds_let is None:
            try:
                sluchay.ds_let = Ds.objects.get(kod=data.ds_let,dateend=None) if data.ds_let != '' else None
            except Ds.DoesNotExist:
                sluchay.ds_let = None
            except Ds.MultipleObjectsReturned:
                sluchay.ds_let = None

        if sluchay.dspat is None:
            try:
                sluchay.dspat = Ds.objects.get(kod=data.dspat,dateend=None) if data.dspat != '' else None
            except Ds.DoesNotExist:
                sluchay.dspat = None
            except Ds.MultipleObjectsReturned:
                sluchay.dspat = None

        if sluchay.otd_y is None:
            try:
                sluchay.otd_y = otde.objects.get(kod=data.otd_y,dateend=None) if data.otd_y != '' else None
            except otde.DoesNotExist:
                sluchay.otd_y = None
            except otdel.MultipleObjectsReturned:
                otdel_y = otde.objects.values('id').filter(kod=data.otd_y,dateend=None)[0]['id']
                sluchay.otd_y = otde.objects.get(id=otdel_y,dateend=None)

        if sluchay.tm_otd is None:
            sluchay.tm_otd = data.tm_otd if data.tm_otd != '' else None

        # if sluchay.prpg is None:
        try:
            sluchay.prpg = Prpg.objects.get(id=1,dateend=None)
        except Prpg.DoesNotExist:
            sluchay.prpg = None


        sluchay.save()

    def create_data_sluchay(self,sluchay):
        self.ICX = dict()
        self.ICX[1] = 101
        self.ICX[2] = 303
        self.ICX[3] = 203
        self.ICX[4] = 305

        try:
            id_pmg = F003.objects.get(mo=sluchay.pmg,dateend=None)
        except F003.DoesNotExist:
            id_pmg = None
        except F003.MultipleObjectsReturned:
            id_pmg = None

        try:
            id_lpy = F003.objects.get(mo=sluchay.lpy,dateend=None)
        except F003.DoesNotExist:
            id_lpy = None
        except F003.MultipleObjectsReturned:
            id_lpy = None

        if len(sluchay.datp) > 0:
            date1 = str(sluchay.datp).replace(".", "-")
            date1 = datetime.datetime.strptime(date1, "%d-%m-%Y").date()
        else:
            date1 = None

        if len(sluchay.datv) > 0:
            date2 = str(sluchay.datv).replace(".", "-")
            date2 = datetime.datetime.strptime(date2, "%d-%m-%Y").date()
        else:
            date2 = None

        if sluchay.vrez != '':
            try:
                id_vrez = Vrzb.objects.get(kod=sluchay.vrez,dateend=None)
            except Vrzb.DoesNotExist:
                id_vrez = None
            except Vrzb.MultipleObjectsReturned:
                id_vrez = None
        else:
            id_vrez = None

        if sluchay.ws != '':
            try:
                id_ws = Ws.objects.get(kod=sluchay.ws,dateend=None)
            except Ws.DoesNotExist:
                id_ws = None
            except Ws.MultipleObjectsReturned:
                id_ws = None
            except:
                id_ws = None
        else:
            id_ws = None

        if sluchay.otd != '':
            try:
                id_otd = otde.objects.get(kod=sluchay.otd,dateend=None)
            except otde.DoesNotExist:
                id_otd = None
            except otde.MultipleObjectsReturned:
                otdel = otde.objects.values('id').filter(kod=sluchay.otd,dateend=None)[0]['id']
                id_otd = otde.objects.get(id=otdel,dateend=None)
        else:
            id_otd = None

        if len(sluchay.icx) > 0:
            try:
                id_iz = self.ICX[int(sluchay.icx)]
                get_id_ishod = V012.objects.get(id_iz=id_iz,dateend=None)
            except (V012.DoesNotExist, KeyError):
                get_id_ishod = None
            except V012.MultipleObjectsReturned:
                get_id_ishod = None
        else:
            get_id_ishod = None

        if sluchay.dsny != '':
            try:
                id_dsny = Ds.objects.get(kod=sluchay.dsny,dateend=None)
            except Ds.DoesNotExist:
                id_dsny = None
            except Ds.MultipleObjectsReturned:
                id_dsny = None
        else:
            id_dsny = None

        if sluchay.dsk != '':
            try:
                id_dsk = Ds.objects.get(kod=sluchay.dsk,dateend=None)
            except Ds.DoesNotExist:
                id_dsk = None
            except Ds.MultipleObjectsReturned:
                id_dsk = None
        else:
            id_dsk = None

        if sluchay.dskz != '':
            try:
                id_dskz = Ds.objects.get(kod=sluchay.dskz,dateend=None)
            except Ds.DoesNotExist:
                id_dskz = None
            except Ds.MultipleObjectsReturned:
                id_dskz = None
        else:
            id_dskz = None

        if sluchay.dsc != '':
            try:
                id_dsc = Ds.objects.get(kod=sluchay.dsc,dateend=None)
            except Ds.DoesNotExist:
                id_dsc = None
            except Ds.MultipleObjectsReturned:
                id_dsc = None
        else:
            id_dsc = None

        if sluchay.ds_osl != '':
            try:
                id_ds_osl = Ds.objects.get(kod=sluchay.ds_osl,dateend=None)
            except Ds.DoesNotExist:
                id_ds_osl = None
            except Ds.MultipleObjectsReturned:
                id_ds_osl = None
        else:
            id_ds_osl = None

        if sluchay.dson != '':
            try:
                id_dson = Ds.objects.get(kod=sluchay.dson,dateend=None)
            except Ds.DoesNotExist:
                id_dson = None
            except Ds.MultipleObjectsReturned:
                id_dson = None
        else:
            id_dson = None
        if sluchay.ksg_osn != '':
            ks = sluchay.ksg_osn[8:]
            gkcg = group_kc_group.objects.values('id').filter(code_usl_kz=str(ks),dateend=None)[:1]
            if gkcg.count() > 0:
                try:
                    id_ksg_osn = group_kc_group.objects.get(id=gkcg[0]['id'],dateend=None)
                except group_kc_group.DoesNotExist:
                    id_ksg_osn = None
            else:
                id_ksg_osn = None
        else:
            id_ksg_osn = None

        if sluchay.ksg_sop != '':
            kso = sluchay.ksg_sop[8:]
            gkcg_so = group_kc_group.objects.values('id').filter(code_usl_kz=str(kso),dateend=None)[:1]
            if gkcg_so.count() > 0:
                try:
                    id_ksg_sop = group_kc_group.objects.get(id=gkcg_so[0]['id'],dateend=None)
                except group_kc_group.DoesNotExist:
                    id_ksg_sop = None
            else:
                id_ksg_sop = None
        else:
            id_ksg_sop = None

        if sluchay.goc != '':
            try:
                id_goc = V014.objects.get(id_tip=sluchay.goc,dateend=None)
            except V014.DoesNotExist:
                id_goc = None
            except V014.MultipleObjectsReturned:
                id_goc = None
        else:
            id_goc = None

        if sluchay.trs != '':
            try:
                id_trs = Trs.objects.get(kod=sluchay.trs,dateend=None)
            except Trs.DoesNotExist:
                id_trs = None
            except Trs.MultipleObjectsReturned:
                id_trs = None
        else:
            id_trs = None

        if sluchay.ds_let != '':
            try:
                id_ds_let = Ds.objects.get(kod=sluchay.ds_let,dateend=None)
            except Ds.DoesNotExist:
                id_ds_let = None
            except Ds.MultipleObjectsReturned:
                id_ds_let = None
        else:
            id_ds_let = None

        if sluchay.dspat != '':
            try:
                id_dspat = Ds.objects.get(kod=sluchay.dspat,dateend=None)
            except Ds.DoesNotExist:
                id_dspat = None
            except Ds.MultipleObjectsReturned:
                id_dspat = None
        else:
            id_dspat = None

        if sluchay.otd_y != '':
            try:
                id_otd_y = otde.objects.get(kod=sluchay.otd_y,dateend=None)
            except otde.DoesNotExist:
                id_otd_y = None
            except otdel.MultipleObjectsReturned:
                otdel_y = otde.objects.values('id').filter(kod=sluchay.otd_y,dateend=None)[0]['id']
                id_otd_y = otde.objects.get(id=otdel_y,dateend=None)
        else:
            id_otd_y = None

        sluchay_md = Sluchay.objects.create(
            pmg=id_pmg,
            lpy=id_lpy,
            nib=sluchay.nib,
            datp=date1,
            datv=date2,
            vrez=id_vrez,
            ws=id_ws,
            tm_otd=sluchay.tm_otd,
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
            vid_hmp=sluchay.vid_hmp,
            metod_hmp=sluchay.metod_hmp,
            tm_let=sluchay.tm_let,
            ds_let=id_ds_let,
            wskr=sluchay.wskr,
            dspat=id_dspat,
            rasxp=sluchay.rasxp,
            otd_y=id_otd_y,
            goc=id_goc,
            trs=id_trs,
        )
        sluchay_md.statistics_type = self.user.statistics_type
        return sluchay_md
    def create_data_oper(self,oper,sluchay):
        for o in oper:

            if o['kod_op'] != '':
                try:
                    id_kod_op = V001.objects.get(kod=o['kod_op'],dateend=None)
                except V001.DoesNotExist:
                    id_kod_op = None
                except V001.MultipleObjectsReturned:
                    id_kod_op = None
            else:
                id_kod_op = None

            if o['obz'] != '':
                try:
                    id_obz = V001.objects.get(kod=o['obz'],dateend=None)
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
                    id_py = PY.objects.get(kod=o['py'],dateend=None)
                except PY.DoesNotExist:
                    id_py = None
                except PY.MultipleObjectsReturned:
                    id_py = None
            else:
                id_py = None

            if o['kodx'] != '':
                try:
                    kodx = self._jon(o['kodx'])
                    top_1 = Vra.objects.filter(kod=kodx,dateend=None).values_list('id')[:1]
                    try:
                        id_kodx = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodx = None
                except Vra.DoesNotExist:
                    id_kodx = None
            else:
                id_kodx = None

            if o['kodxa'] != '':
                try:
                    kodxa = self._jon(o['kodxa'])
                    top_1 = Vra.objects.filter(kod=kodxa,dateend=None).values_list('id')[:1]
                    try:
                        id_kodxa = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodxa = None
                except Vra.DoesNotExist:
                    id_kodxa = None
            else:
                id_kodxa = None

            if o['kodxa1'] != '':
                try:
                    kodxa1 = self._jon(o['kodxa1'])
                    top_1 = Vra.objects.filter(kod=kodxa1,dateend=None).values_list('id')[:1]
                    try:
                        id_kodxa1 = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodxa1 = None
                except Vra.DoesNotExist:
                    id_kodxa1 = None
            else:
                id_kodxa1 = None

            if o['kodan'] != '':
                try:
                    kodan = self._jon(o['kodan'])
                    top_1 = Vra.objects.filter(kod=kodan,dateend=None).values_list('id')[:1]
                    try:
                        id_kodan = Vra.objects.get(id=top_1[0][0],dateend=None)
                    except IndexError:
                        id_kodan = None
                except Vra.DoesNotExist:
                    id_kodan = None
            else:
                id_kodan = None

            if o['goc_o'] != '':
                try:
                    id_goc = V014.objects.get(id_tip=o['goc_o'],dateend=None)
                except V014.DoesNotExist:
                    id_goc = None
                except V014.MultipleObjectsReturned:
                    id_goc = None
            else:
                id_goc = None

            oper_md = Oper.objects.create(
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
    def create_data_vds(self,vds,sluchay):
        if vds.t_pol != '':
            try:
                id_t_pol = F008.objects.get(id_tip=vds.t_pol,dateend=None)
            except F008.DoesNotExist:
                id_t_pol = None
            except F008.MultipleObjectsReturned:
                id_t_pol = None
        else:
            id_t_pol = None





        if vds.ctkom != '':
            try:
                id_ctkom = Skom.objects.get(kod=vds.ctkom,dateend=None)
            except Skom.DoesNotExist:
                id_ctkom = None
            except Skom.MultipleObjectsReturned:
                id_ctkom = None
        else:
            id_ctkom = None

        if vds.ksg_ts != '':
            try:
                id_ksg_ts = T003.objects.get(kod=vds.ksg_ts,dateend=None)
            except T003.DoesNotExist:
                id_ksg_ts = None
            except T003.MultipleObjectsReturned:
                id_ksg_ts = None
        else:
            id_ksg_ts = None

        vds_md = Vds.objects.create(
            t_pol=id_t_pol,
            # vds=id_vds,
            ctkom=id_ctkom,
            sctp=vds.sctp,
            nctp=vds.nctp,
            ksg_ts=id_ksg_ts)

        sluchay.vds = vds_md
        return vds_md
    def create_data_trv(self,le_trv,sluchay):
        if le_trv.t_trv != '':
            try:
                id_t_trv = Ds.objects.get(kod=le_trv.t_trv,dateend=None)
            except Ds.DoesNotExist:
                id_t_trv = None
            except Ds.MultipleObjectsReturned:
                id_t_trv = None
        else:
            id_t_trv = None

        if le_trv.details != '':
            try:
                id_details = Ds.objects.get(kod=le_trv.details,dateend=None)
            except Ds.DoesNotExist:
                id_details = None
            except Ds.MultipleObjectsReturned:
                id_details = None
        else:
            id_details = None

        if le_trv.trav_ns != '' and le_trv.trav_ns != None:
            try:
                id_trav_ns = Trvnas.objects.get(kod=le_trv.trav_ns,dateend=None)
            except Trvnas.DoesNotExist:
                id_trav_ns = None
            except Trvnas.MultipleObjectsReturned:
                id_trav_ns = None
        else:
            id_trav_ns = None

        le_trv_md = Le_trv.objects.create(
            t_trv=id_t_trv,
            details=id_details
        )
        sluchay.le_trv = le_trv_md
    def create_data_le_vr(self,le_vr,sluchay):
        if le_vr.prof_k != '':
            try:
                id_prof_k = V020.objects.get(idk_pr=le_vr.prof_k,dateend=None)
            except V020.DoesNotExist:
                id_prof_k = None
            except V020.MultipleObjectsReturned:
                id_prof_k = None
        else:
            id_prof_k = None

        le_vr_md = Le_Vr.objects.create(
            prof_k=id_prof_k
        )
        sluchay.le_vr = le_vr_md
    def create_data_patient(self,patient,sluchay):
        self.YEAR = datetime.datetime.now()
        if len(patient.datr) > 0:
            date = str(patient.datr).replace(".", "-")
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
            id_pol = V005.objects.get(id_pol=patient.pol,dateend=None)
        except V005.DoesNotExist:
            id_pol = None
        except V005.MultipleObjectsReturned:
            id_pol = None

        if patient.udl != '':
            try:
                id_udl = F011.objects.get(id_doc=patient.udl,dateend=None)
            except F011.DoesNotExist:
                id_udl = None
            except F011.MultipleObjectsReturned:
                id_udl = None
        else:
            id_udl = None

        if patient.c_oksm != '':
            try:
                id_c_oksm = Oksm.objects.get(kod=patient.c_oksm,dateend=None)
            except Oksm.DoesNotExist:
                id_c_oksm = None
            except Oksm.MultipleObjectsReturned:
                id_c_oksm = None
        else:
            id_c_oksm = None

        if patient.cj != '':
            try:
                id_cj = CJ.objects.get(kod=patient.cj,dateend=None)
            except CJ.DoesNotExist:
                id_cj = None
            except CJ.MultipleObjectsReturned:
                id_cj = None
        else:
            id_cj = None

        if patient.v_lgoty != '':
            try:
                id_v_lgoty = V_LGOTY.objects.get(kod=patient.v_lgoty,dateend=None)
            except V_LGOTY.DoesNotExist:
                id_v_lgoty = None
            except V_LGOTY.MultipleObjectsReturned:
                id_v_lgoty = None
        else:
            id_v_lgoty = None

        if patient.in_t != '':
            try:
                id_in_t = T004.objects.get(kod=patient.in_t,dateend=None)
            except T004.DoesNotExist:
                id_in_t = None
            except T004.MultipleObjectsReturned:
                id_in_t = None
        else:
            id_in_t = None

        if patient.r_n != '':
            try:
                id_r_n = Rab_Ner.objects.get(kod=patient.r_n,dateend=None)
            except Rab_Ner.DoesNotExist:
                id_r_n = None
            except Rab_Ner.MultipleObjectsReturned:
                id_r_n = None
        else:
            id_r_n = None

        if patient.vec == '':
            vec = 0
        else:
            vec = patient.vec

        patient_md = Patient.objects.create(
            fam=patient.fam,
            im=patient.im,
            ot=patient.ot,
            pol=id_pol,
            datr=date,
            vs=vs,
            nvs=nvs,
            udl=id_udl,
            s_pasp=patient.s_pasp,
            n_pasp=patient.n_pasp,
            ss=patient.ss,
            cod_adr=patient.cod_adr,
            c_oksm=id_c_oksm,
            adr=patient.adr,
            m_roj=patient.m_roj,
            cj=id_cj,
            v_lgoty=id_v_lgoty,
            in_t=id_in_t,
            rab=patient.rab,
            r_n=id_r_n,
            prof=patient.prof,
            vec=vec
        )
        patient_md.sluchay.add(sluchay)
        patient_md.save()
        return patient_md
    def update_data_sluchay(self):
        pass

# Sluchay.objects.filter(is_1c=True).all().delete()
# Patient_P.objects.filter(is_1c=True).all().delete()
# Patient.objects.filter(is_1c=True).all().delete()
# Vds.objects.filter(is_1c=True).all().delete()
# Le_Vr.objects.filter(is_1c=True).all().delete()
# Oper.objects.filter(is_1c=True).all().delete()