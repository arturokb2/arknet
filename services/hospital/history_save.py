
from hospital.models import *
from okb2.models import MyUser
import json
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.utils.dateparse import parse_date
from datetime import datetime
import requests

class Save():
    def __init__(self, request):
        self.request = request
        self.user = MyUser.objects.get(user=self.request.user.id)

    def save(self):
        otde_l = ['НЕВРОЛОГИЯ N1', 'НЕВРОЛОГИЯ N2', 'НЕВРОЛОГИЯ N3']
        ds_l = ['G45', 'G46', 'I60', 'I60.0', 'I60.1', 'I60.2', 'I60.3', 'I60.4', 'I60.5',
                'I60.6', 'I60.7', 'I60.8', 'I60.9', 'I61', 'I61.0', 'I61.1', 'I61.2', 'I61.3',
                'I61.4', 'I61.5', 'I61.6', 'I61.8', 'I61.9', 'I62', 'I62.0', 'I62.1', 'I62.9',
                'I63', 'I63.0', 'I63.1', 'I63.2', 'I63.3', 'I63.4', 'I63.5', 'I63.6', 'I63.8', 'I63.9']
        resl_l = ['Умер', 'Умер в приёмном покое']

        history = json.loads(self.request.POST.get("history"))
        sluchay = Sluchay.objects.get(id=history['sl_id'])
        patient = Patient.objects.get(sluchay=sluchay.id)
        #Шапка
        patient.fam = str(history['fam']) if str(history['fam']) != None and str(history['fam']) != "" else ''
        patient.im = str(history['im']) if str(history['im']) != None and str(history['im']) != "" else ''
        patient.ot = str(history['ot']) if str(history['ot']) != None and str(history['ot']) != "" else ''
        sluchay.update_user = self.user
        sluchay.err = history['err']
        sluchay.err_text = history['err_text']
        # if ((str(history['vds']).strip() != '' and str(history['vds']).strip() != 'ВТМП баз.программа ОМС') \
        #             (str(history['vds']).strip() != '' and str(history['vds']).strip() != 'ВТМП сверхбаз.программа')):
        #     sluchay.tip_oms = '1'
        # else:
        #     sluchay.tip_oms = '2'



        # sluchay.tip_oms = str(history['tip_oms']).strip() if history['tip_oms'] != '' and history['tip_oms'] != None else None
        try:
            if str(history['vds']).strip() == 'ВТМП баз.программа ОМС':
                sluchay.tip_oms = '2'
            elif str(history['vds']).strip() == 'ВТМП сверхбаз.программа':
                sluchay.tip_oms = '2'
            else:
                sluchay.tip_oms = '1'
        except:
            pass

        try:
            patient.pol = V005.objects.get(polname=str(history['pol']).strip(),dateend=None) if history['pol'] != None else None
        except V005.DoesNotExist:
            patient.pol = None

        try:
            sluchay.datp = self.str_form(history['datp']) if history['datp'] != None and history['datp'] != '' else None
        except ValidationError:
            sluchay.datp = None

        try:
            sluchay.tm_otd = str(history['tm_otd']) if str(history['tm_otd']) != None and str(history['tm_otd']) != "" else ''
        except:
            pass

        try:
            sluchay.datv = self.str_form(history['datv']) if history['datv'] != None and history['datv'] != '' else None
        except ValidationError:
            sluchay.datv = None
        except:
            pass

        try:
            patient.datr = self.str_form(history['datr']) if history['datr'] != None and history['datr'] != '' else None
        except ValidationError:
            patient.datr = None
        except:
            pass

        # 1.Персональные данные
        try:
            sluchay.otd = otde.objects.get(naim=str(history['otd']).strip(),dateend=None) if history['otd'] != None and history['otd'] != '' else None
        except otde.DoesNotExist:
            sluchay.otd = None
        try:
            patient.vec = str(history['vec']).strip() if str(history['vec']).strip() != None and str(history['vec']).strip() != "" else ''
        except:
            pass
        try:
            patient.m_roj = str(history['m_roj']).strip() if str(history['m_roj']).strip() != None and str(history['m_roj']).strip() != "" else ''
        except:
            pass

        try:
            patient.c_oksm = Oksm.objects.get(naim=str(history['c_oksm']).strip(),dateend=None) if history['c_oksm'] != None and \
                                                                                      history['c_oksm'] != '' else None
        except Oksm.DoesNotExist:
            patient.c_oksm = None
        try:
            patient.kv = str(history['kv']).strip() if str(history['kv']).strip() != None and str(history['kv']).strip() != "" else ''
        except:
            pass
        try:
            patient.kp = str(history['kp']).strip() if str(history['kp']).strip() !=  None and str(history['kp']).strip() != "" else ''
        except:
            pass
        try:
            patient.stro = str(history['stro']).strip() if str(history['stro']).strip() != None and str(history['stro']).strip() != "" else ''
        except:
            pass


        try:
            patient.cj = CJ.objects.get(naim=str(history['cj']).strip(),dateend=None) if history['cj'] != None and history['cj'] != '' else None
        except CJ.DoesNotExist:
            patient.cj = None

        try:
            if str(history['rai']) == 'Центральный АО':
                patient.rai = '1'
            elif str(history['rai']) == 'Ленинский АО':
                patient.rai = '2'
            elif str(history['rai']) == 'Калининский АО':
                patient.rai = '3'
            elif str(history['rai']) == 'Восточный АО':
                patient.rai = '4'
            else:
                patient.rai = None
        except:
            pass

        try:
            patient.adr = str(history['adr']).strip() if str(history['adr']).strip() != None and str(history['adr']).strip() != "" else ''
        except:
            pass

        try:
            patient.rab = str(history['rab']).strip() if str(history['rab']).strip() != None and str(history['rab']).strip() != "" else ''
        except:
            pass
        try:
            patient.prof = str(history['prof']).strip() if str(history['prof']).strip() != None and str(history['prof']).strip() != "" else ''
        except:
            pass
        try:
            patient.r_n = Rab_Ner.objects.get(naim=str(history['r_n']).strip(),dateend=None) if history['r_n'] != None and history[
                'r_n'] != '' else None
        except Rab_Ner.DoesNotExist:
            patient.r_n = None

        try:
            patient.in_t = T004.objects.get(name=str(history['in_t']).strip(),dateend=None) if history['in_t'] != None and history[
                'in_t'] != '' else None
        except T004.DoesNotExist:
            patient.in_t = None

        try:
            sluchay.lpy = F003.objects.get(naim=str(history['lpy']).strip(),dateend=None) if history['lpy'] != None and history[
                'lpy'] != '' else None
        except F003.DoesNotExist:
            sluchay.lpy = None
        try:
            sluchay.npr_num = str(history['npr_num']).strip() if str(history['npr_num']).strip() != None and str(history['npr_num']).strip() != "" else ""
        except:
            pass

        try:
            sluchay.npr_date = self.str_form(history['npr_date']) if history['npr_date'] != None and history[
                'npr_date'] != '' else None
        except ValidationError:
            sluchay.npr_date = None

        try:
            if str(history['alg']).strip() == "Нет":
                sluchay.alg = '1'
            elif str(history['alg']).strip() == "Алкогольное":
                sluchay.alg = '2'
            elif str(history['alg']).strip() == "Наркотическое":
                sluchay.alg = '3'
        except:
            pass

        try:
            sluchay.goc = V014.objects.get(tip_name=str(history['goc']).strip(),dateend=None) if history['goc'] != None and history[
                'goc'] != '' else None
        except V014.DoesNotExist:
            sluchay.goc = None

        try:
            sluchay.prpg = Prpg.objects.get(naim=str(history['prpg']).strip(),dateend=None) if history['prpg'] != None and history[
                'prpg'] != '' else None
        except Prpg.DoesNotExist:
            sluchay.prpg = None

        try:
            sluchay.vrez = Vrzb.objects.get(naim=str(history['vrez']).strip(),dateend=None) if history['vrez'] != None and history[
                'vrez'] != '' else None
        except Vrzb.DoesNotExist:
            sluchay.vrez = None

        try:
            sluchay.p_per = PER.objects.get(naim=str(history['p_per']).strip(),dateend=None) if history['p_per'] != None and history[
                'p_per'] != '' else None
        except PER.DoesNotExist:
            sluchay.p_per = None

        # 2. Сведения о диагнозах
        try:
            sluchay.dsny = Ds.objects.get(kod=str(history['dsny']['kod']).strip(), dateend=None) if history['dsny'][
                                                                                                        'kod'] != None and \
                                                                                                    history['dsny'][
                                                                                                        'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dsny = None
        try:
            sluchay.ds_0 = Ds.objects.get(kod=str(history['ds_0']['kod']).strip(), dateend=None) if history['ds_0'][
                                                                                                        'kod'] != None and \
                                                                                                    history['ds_0'][
                                                                                                        'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.ds_0 = None
        try:
            sluchay.dsk = Ds.objects.get(kod=str(history['dsk']['kod']).strip(), dateend=None) if history['dsk'][
                                                                                                      'kod'] != None and \
                                                                                                  history['dsk'][
                                                                                                      'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dsk = None
        try:
            sluchay.dskz = Ds.objects.get(kod=str(history['dskz']['kod']).strip(), dateend=None) if history['dskz']['kod'] != None and \
                                                                                                    history['dskz']['kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dskz = None

        try:
            sluchay.dskz2 = Ds.objects.get(kod=str(history['dskz2']['kod']).strip(), dateend=None) if history['dskz2']['kod'] != None and \
                                                                                                    history['dskz2']['kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dskz2 = None

        try:
            sluchay.ds_osl = Ds.objects.get(kod=str(history['ds_osl']['kod']).strip(), dateend=None) if \
            history['ds_osl'][
                'kod'] != None and \
            history['ds_osl'][
                'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.ds_osl = None

        try:
            sluchay.dsc = Ds.objects.get(kod=str(history['dsc']['kod']).strip(), dateend=None) if history['dsc'][
                                                                                                      'kod'] != None and \
                                                                                                  history['dsc'][
                                                                                                      'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dsc = None
        try:
            sluchay.dson = Ds.objects.get(kod=str(history['dson']['kod']).strip(), dateend=None) if history['dson'][
                                                                                                        'kod'] != None and \
                                                                                                    history['dson'][
                                                                                                        'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dson = None
        try:
            sluchay.dat_otd = self.str_form(str(history['dat_otd'])) if history['dat_otd'] != None and \
                                                                                history[
                                                                                    'dat_otd'] != '' else None
        except ValidationError:
            sluchay.dat_otd = None
        except:
            pass

        try:
            sluchay.tm_otd_1 = str(history['tm_otd_d']).strip() if str(history['tm_otd_d']).strip() != None and str(history['tm_otd_d']).strip() != "" else ''
        except:
            pass

        try:
            sluchay.icx = V012.objects.get(id_iz=[i for i in str(history['icx']).split(' ') if i.isdigit()][0]) if (
                    (history['icx'] != None) and (history['icx'] != '')) else None
        except V012.DoesNotExist:
            sluchay.icx = None

        try:
            sluchay.rslt = V009.objects.get(
                id_tip=[r for r in str(history['rslt']).split(' ') if r.isdigit()][0]) if (
                    (history['rslt'] != None) and (history['rslt'] != '')) else None
        except V009.DoesNotExist:
            sluchay.rslt = None

        # 3.Койко-дни

        if sluchay.le_vr != None:
            self.update_le_vr(sluchay.le_vr, history['le_vr'],sluchay.otd)
            sluchay.le_vr.save()
        else:
            le_vr = Le_Vr()
            le_vr.save()
            self.update_le_vr(le_vr, history['le_vr'],sluchay.otd)
            le_vr.save()
            sluchay.le_vr = le_vr

        # 4.Операции
        tem_oper = []
        for o in (history['oper']):
            if (o['dato'] != None and o['dato'] != ""):
                tem_oper.append(o)
        history['oper'].clear()
        history['oper'] = tem_oper
        if len(history['oper']) > 0:
            if sluchay.oper.count() == len(history['oper']):
                opers = sluchay.oper.values('id')
                for o in range(len(opers)):
                    oper = Oper.objects.get(id=opers[o]['id'])
                    self.update_oper(oper, history['oper'][o],sluchay.otd)
                    oper.save()
            else:
                opers = sluchay.oper.values('id')
                for o in opers:
                    Oper.objects.get(id=o['id']).delete()
                for o in range(len(history['oper'])):
                    oper = Oper()
                    oper.save()
                    self.update_oper(oper, history['oper'][o],sluchay.otd)
                    oper.save()
                    sluchay.oper.add(oper)
        else:
            if sluchay.oper.count() > 0:
                opers = sluchay.oper.values('id')
                for o in opers:
                    Oper.objects.get(id=o['id']).delete()

        #4.1 Импланты
        tem_med_dev = []

        for o in (history['med_dev']):
            if (o['date'] != None and o['date'] != ""):
                tem_med_dev.append(o)
        history['med_dev'].clear()
        history['med_dev'] = tem_med_dev

        if len(history['med_dev']) > 0:
            if sluchay.med_dev.count() == len(history['med_dev']):
                med_devs = sluchay.med_dev.values('id')
                for o in range(len(med_devs)):
                    med_dev = Med_dev.objects.get(id=med_devs[o]['id'])
                    self.update_med_dev(med_dev, history['med_dev'][o])
                    med_dev.save()
            else:
                med_devs = sluchay.med_dev.values('id')
                for o in med_devs:
                    Med_dev.objects.get(id=o['id']).delete()
                for o in range(len(history['med_dev'])):
                    med_dev = Med_dev()
                    med_dev.save()
                    self.update_med_dev(med_dev, history['med_dev'][o])
                    med_dev.save()
                    sluchay.med_dev.add(med_dev)
        else:
            if sluchay.med_dev.count() > 0:
                med_devs = sluchay.med_dev.values('id')
                for o in med_devs:
                    Med_dev.objects.get(id=o['id']).delete()

        # 5.Клинико-стат.гр.заболев-я

        # try:
        #     if self.user.ws.kod == 1:
        #         sluchay.ksg_osn = T006.objects.get(code_usl_kz=str(history['ksg_osn']).strip(),
        #                                            ksg__icontains='st', dateend=None) if \
        #             history['ksg_osn'] != None and history['ksg_osn'] != '' else None
        #     elif self.user.ws.kod == 2:
        #         sluchay.ksg_osn = T006.objects.get(code_usl_kz=str(history['ksg_osn']).strip(),
        #                                            ksg__icontains='ds', dateend=None) if \
        #             history['ksg_osn'] != None and history['ksg_osn'] != '' else None
        # except T006.DoesNotExist:
        #     sluchay.ksg_osn = None
        # except T006.MultipleObjectsReturned:
        #     if self.user.ws.kod == 1:
        #         ksg_osn = T006.objects.values('id').filter(code_usl_kz=str(history['ksg_osn']).strip(),ksg__icontains='st', dateend=None) if \
        #             history['ksg_osn'] != None and history['ksg_osn'] != '' else None
        #     elif self.user.ws.kod == 2:
        #         ksg_osn = T006.objects.values('id').filter(code_usl_kz=str(history['ksg_osn']).strip(),ksg__icontains='ds', dateend=None) if \
        #             history['ksg_osn'] != None and history['ksg_osn'] != '' else None
        #     if ksg_osn.count() > 0:
        #         sluchay.ksg_osn = T006.objects.get(id=ksg_osn[0]['id'])
        #     else:
        #         sluchay.ksg_osn = None

        # sluchay.ksg_osn = self.get_code_usl(history['ksg_osn'])
        # op = Sluchay.objects.get(id=186019).oper.filter(pop=True).all()


        if history['ksg_osn_helper'] is not None:
            try:
                sluchay.ksg_osn = group_kc_group.objects.get(id=history['ksg_osn_helper'],dateend=None) if history['ksg_osn_helper'] != '' and history['ksg_osn_helper'] != None else None
            except group_kc_group.DoesNotExist:
                sluchay.ksg_osn = None
        else:
            try:
                g = group_kc_group.objects.values('id').filter(code_usl_kz=history['ksg_osn'],dateend=None)[:1][0]
                sluchay.ksg_osn = group_kc_group.objects.get(id=g['id'])
            except:
                sluchay.ksg_osn = None

        try:
            sluchay.oopkk = group_kc_dkk.objects.get(kod=str(history['oopkk']).strip(), ksg_1=history['ksg_osn_all'],
                                                     dateend=None)
        except group_kc_dkk.DoesNotExist:
            sluchay.oopkk = None



        # if history['ksg_sop_helper'] is not None:
        #     try:
        #         sluchay.ksg_sop = group_kc_group.objects.get(id=history['ksg_sop_helper'],dateend=None) if history['ksg_sop_helper'] != '' else None
        #     except group_kc_group.DoesNotExist:
        #         sluchay.ksg_sop = None
        # else:
        #     print(history['ksg_sop'])
        #     try:
        #         g = group_kc_group.objects.values('id').filter(code_usl_kz=history['ksg_sop'],dateend=None)[:1][0]
        #         sluchay.ksg_sop = group_kc_group.objects.get(id=g['id'])
        #     except:
        #         sluchay.ksg_sop = None

        try:
            sluchay.code_usl = T003.objects.get(kod=str(history['code_usl']).strip(),vidpom=1,usl_ok=1,idsp=33, dateend=None) if history['code_usl'] != None and \
                                                                                                       history['code_usl'] != None != '' else None
        except T003.DoesNotExist:
            sluchay.code_usl = None
        except T003.MultipleObjectsReturned:
            sluchay.code_usl = None

        # try:
        #     sluchay.iddokt = Vra.objects.get(kod=history['iddoc'], dateend=None) if (
        #             (history['iddoc'] != '') and (history['iddoc'] != None)) else None
        # except Vra.DoesNotExist:
        #     sluchay.iddokt = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=history['iddoc'], dateend=None)[0]['id']
        #     sluchay.iddokt = Vra.objects.get(id=vra)
        sluchay.iddokt = self.get_vra(None,history['iddoc'])
        try:
            sluchay.metod_hmp = str(history['metod_hmp']) if str(history['metod_hmp']) != None and str(history['metod_hmp']) != "" else ''
        except:
            pass
        try:
            sluchay.vid_hmp =str( history['vid_hmp']) if str(history['vid_hmp']) != None and str( history['vid_hmp']) != "" else ''
        except:
            pass
        # if history['code_usl_vt'] != '' and sluchay.dskz != None:

        # vt = Tar_vt.objects.values('id').filter(kod_stat=metod_hmp, metod__icontains=vid_hmp, mkb__icontains=dskz,
        #                                         dateend=None)

        # try:
        #     sluchay.code_usl_vt =  Tar_vt.objects.get(kod_stat=history['metod_hmp'],metod__icontains=history['vid_hmp'],mkb__icontains=str(sluchay.dskz.kod).split('.')[0],dateend=None)
        # except Tar_vt.DoesNotExist:
        #     sluchay.code_usl_vt = None
        # except Tar_vt.MultipleObjectsReturned:
        #     vt = Tar_vt.objects.values('id').filter(kod_stat=history['metod_hmp'],metod__icontains=history['vid_hmp'],mkb__icontains=str(sluchay.dskz.kod).split('.')[0],dateend=None)[:1]
        #     sluchay.code_usl_vt = Tar_vt.objects.get(id=vt[0]['id'])
        # except:
        #     sluchay.code_usl_vt = None

        if  sluchay.dskz2 != None:
            ds = sluchay.dskz2.kod if sluchay.dskz2 != None else ''
        else:
            ds = sluchay.dskz.kod if sluchay.dskz != None else ''

        try:
            sluchay.code_usl_vt = Tar_vt.objects.get(kod_stat=history['metod_hmp'], metod__icontains=history['vid_hmp'],
                                                     mkb__icontains=sluchay.dskz.kod, dateend=None)
        except Tar_vt.DoesNotExist:
            sluchay.code_usl_vt = None

        except Tar_vt.MultipleObjectsReturned:
            vt = Tar_vt.objects.values('id').filter(kod_stat=history['metod_hmp'], metod__icontains=history['vid_hmp'],
                                                    mkb__icontains=sluchay.dskz.kod, dateend=None)[:1]
            sluchay.code_usl_vt = Tar_vt.objects.get(id=vt[0]['id'])
        except:
            sluchay.code_usl_vt = None

        if sluchay.code_usl_vt == None:
            try:
                sluchay.code_usl_vt =  Tar_vt.objects.get(kod_stat=history['metod_hmp'],metod__icontains=history['vid_hmp'],mkb__icontains=str(sluchay.dskz.kod).split('.')[0],dateend=None)
            except Tar_vt.DoesNotExist:
                sluchay.code_usl_vt = None
            except Tar_vt.MultipleObjectsReturned:
                vt = Tar_vt.objects.values('id').filter(kod_stat=history['metod_hmp'],metod__icontains=history['vid_hmp'],mkb__icontains=str(sluchay.dskz.kod).split('.')[0],dateend=None)[:1]
                sluchay.code_usl_vt = Tar_vt.objects.get(id=vt[0]['id'])
            except:
                sluchay.code_usl_vt = None

            # 6.Oсложнение
        tem_oslo = []
        for o in (history['oslo']):
            if (o['inf_oper'] != None and o['inf_oper'] != ""):
                tem_oslo.append(o)
        history['oslo'].clear()
        history['oslo'] = tem_oslo

        if len(history['oslo']) > 0:
            if oper.oslo.count() == len(history['oslo']):
                oslos = oper.oslo.values('id')
                for o in range(len(oslos)):
                    oslo = Oslo.objects.get(id=oslos[o]['id'])
                    self.update_oslo(oslo, history['oslo'][o])
                    oslo.save()
            else:
                oslos = oper.oslo.values('id')
                for o in oslos:
                    Oslo.objects.get(id=o['id']).delete()
                for o in range(len(history['oslo'])):
                    oslo = Oslo()
                    oslo.save()
                    self.update_oslo(oslo, history['oslo'][o])
                    oslo.save()
                    oper.oslo.add(oslo)
        else:
            if sluchay.oper.count() > 0:
                opers = sluchay.oper.values('id')
                for o in opers:
                    oper = Oper.objects.get(id=o['id'])
                    oper.oslo.clear()
                    oper.save()

        # 7.Трудоспособность
        try:
            try:
                sluchay.trs = Trs.objects.get(naim=str(history['trs']).upper(), dateend=None) if history[
                                                                                                    'trs'] != None and \
                                                                                                history[
                                                                                                    'trs'] != '' else None
            except Trs.DoesNotExist:
                sluchay.trs = None
        except:
            pass

        # 8.Манипуляции
        tem_manipulation = []
        for o in history['manipulation']:
            if (o['datm'] != None and o['datm'] != ""):
                tem_manipulation.append(o)
        history['manipulation'].clear()
        history['manipulation'] = tem_manipulation

        if len(history['manipulation']) > 0:
            if sluchay.manpy.count() == len(history['manipulation']):
                manpys = sluchay.manpy.values('id')
                for m in range(len(manpys)):
                    manpy = Manpy.objects.get(id=manpys[m]['id'])
                    self.update_manpy(manpy, history['manipulation'][m])
                    manpy.save()
            else:
                manpys = sluchay.manpy.values('id')
                for m in manpys:
                    Manpy.objects.get(id=m['id']).delete()
                for m in range(len(history['manipulation'])):
                    manpy = Manpy()
                    manpy.save()
                    self.update_manpy(manpy, history['manipulation'][m])
                    manpy.save()
                    sluchay.manpy.add(manpy)
        else:
            if sluchay.manpy.count() > 0:
                manpys = sluchay.manpy.values('id')
                for m in manpys:
                    Manpy.objects.get(id=m['id']).delete()

        # 9.Переводы
        if (((history['potd'] != None) and (history['dat_pe'] != "")) or (
                (history['kod_y'] != None) and (history['pr_per'] != ""))):
            if sluchay.vb_s.count() > 0:
                vb_s = Vb_s.objects.get(id=sluchay.vb_s.values('id')[0]['id'])
                self.update_vb_s(vb_s, history)
                vb_s.save()
            else:
                vb_s = Vb_s()
                vb_s.save()
                self.update_vb_s(vb_s, history)
                vb_s.save()
                sluchay.vb_s.add(vb_s)
        else:
            if sluchay.vb_s.count() > 0:
                vb_s = Vb_s.objects.get(id=sluchay.vb_s.values('id')[0]['id'])
                vb_s.delete()

        # А.Патанатомический Ds
        try:
            sluchay.wskr_date = self.str_form(history['wskr_date']) if (
                    (history['wskr_date'] != None) and (history['wskr_date'] != "")) else None
        except ValidationError:
            sluchay.wskr_date = None
        except:
            pass

        try:
            sluchay.tm_let = str(history['tm_let']).strip() if history['tm_let'] != None and history['tm_let'] != '' else ''
        except:
            pass

        try:
            sluchay.pri = Prli.objects.get(naim=str(history['pri']).strip(), dateend=None) if history[
                                                                                                  'pri'] != None and \
                                                                                              history[
                                                                                                  'pri'] != '' else None
        except Prli.DoesNotExist:
            sluchay.pri = None

        try:
            sluchay.ds_let = Ds.objects.get(kod=str(history['ds_let']['kod']).strip(), dateend=None) if \
            history['ds_let'][
                'kod'] != None and \
            history['ds_let'][
                'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.ds_let = None
        try:
            if str(history['wskr']).strip() == "без вскрытия":
                sluchay.wskr = '1'
            elif str(history['wskr']).strip() == "патологоанатом.":
                sluchay.wskr = '2'
            elif str(history['wskr']).strip() == "судебное":
                sluchay.wskr = '3'
        except:
            pass
        try:
            sluchay.dspat = Ds.objects.get(kod=str(history['dspat']['kod']).strip(), dateend=None) if \
            history['dspat'][
                'kod'] != None and \
            history['dspat'][
                'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dspat = None
        try:
            if history['rasxp'] == "Да":
                sluchay.rasxp = '1'
            elif history['rasxp'] == "Нет":
                sluchay.rasxp = '2'
        except:
            pass
        try:
            sluchay.otd_y = otde.objects.get(naim=str(history['otd_y']).strip(), dateend=None) if history[
                                                                                                      'otd_y'] != None else None
        except otde.DoesNotExist:
            sluchay.otd_y = None
        # B.Сведения о травмах
        if ((history['details']['kod'] != None) and (history['details']['kod'] != "") or (
                (history['t_trv'] != None) and (history['t_trv'] != ""))):
            if sluchay.le_trv != None:
                self.update_le_trv(sluchay.le_trv, history)
                sluchay.le_trv.save()
            else:
                le_trv = Le_trv()
                le_trv.save()
                self.update_le_trv(le_trv, history)
                le_trv.save()
                sluchay.le_trv = le_trv
        else:
            if sluchay.le_trv != None:
                id = sluchay.le_trv.id
                sluchay.le_trv = None
                Le_trv.objects.get(id=id).delete()
        # C.Полис/Документ/Снилс
        if sluchay.vds != None:
            self.update_vds(sluchay.vds, history)
            sluchay.vds.save()
        else:
            vds = Vds()
            vds.save()
            self.update_vds(vds, history)
            vds.save()
            sluchay.vds = vds
        try:
            patient.udl = F011.objects.get(docname=history['udl'], dateend=None) if history['udl'] != None and history['udl'] != '' else None
        except F011.DoesNotExist:
            patient.udl = None
        try:
            patient.s_pasp = str(history['s_pasp']).strip() if str(history['s_pasp']).strip() != None and str(history['s_pasp']).strip() != "" else ''
        except:
            pass
        try:
            patient.n_pasp = str(history['n_pasp']).strip() if str(history['n_pasp']).strip() != None and str(history['n_pasp']).strip() != "" else ''
        except:
            pass

        try:
            patient.docdate = self.str_form(history['docdate']) if (
                    (history['docdate'] != None) and (history['docdate'] != "")) else None
        except ValidationError:
            patient.docdate = None
        except:
            pass

        try:
            patient.docorg = str(history['docorg']).strip() if str(history['docorg']).strip() != None and str(history['docorg']).strip() != "" else ''
        except:
            pass
        try:
            patient.ss = str(history['ss']).strip() if str(history['ss']).strip() != None and str(history['ss']).strip() != "" else ''
        except:
            pass
        # D.Прерывание беременности
        # if ((history['vb_a_datv'] != None and history['vb_a_datv'] != "") or (
        #         history['pria'] != None and history['pria'] != "") or (
        #         history['m_prer'] != None and history['m_prer'] != "")):
        if (sluchay.dskz != None and str(sluchay.dskz.kod)[:1] == "O"):
            if sluchay.vb_a != None:
                self.update_vb_a(sluchay.vb_a, history)
                sluchay.vb_a.save()
            else:
                vb_a = Vb_a()
                vb_a.save()
                self.update_vb_a(vb_a, history)
                vb_a.save()
                sluchay.vb_a = vb_a
        else:
            if sluchay.vb_a != None:
                id = sluchay.vb_a.id
                sluchay.vb_a = None
                Vb_a.objects.get(id=id).delete()


        # E.Лист нетрудоспособности
        try:
            if ((history['dat_l1'] != None) or (history['dat_l2'] != None)):
                if sluchay.disability != None:
                    self.update_disability(sluchay.disability, history)
                    sluchay.disability.save()
                else:
                    disability = Disability()
                    disability.save()
                    self.update_disability(disability, history)
                    disability.save()
                    sluchay.disability = disability
            else:
                if sluchay.disability != None:
                    id = sluchay.disability.id
                    sluchay.disability = None
                    Disability.objects.get(id=id).delete()
        except:
            pass

        # F.Представитель пациента
        if ((history['fam_p'] != None and history['fam_p'] != "") or (
                history['im_p'] != None and history['im_p'] != "") or (
                history['ot_p'] != None and history['ot_p'] != "")):
            if patient.patient_p != None:
                self.update_patient_p(patient.patient_p, history)
                patient.patient_p.save()
            else:
                patient_p = Patient_P()
                patient_p.save()
                self.update_patient_p(patient_p, history)
                patient_p.save()
                patient.patient_p = patient_p
                patient.save()
        else:
            if patient.patient_p != None:
                id = patient.patient_p.id
                patient.patient_p = None
                Patient_P.objects.get(id=id).delete()
        # G.Адрес проживания
        try:
            patient.c_oksm = Oksm.objects.get(naim=str(history['c_oksm']).strip(), dateend=None) if history[
                                                                                                        'c_oksm'] != None and \
                                                                                                    history[
                                                                                                        'c_oksm'] != '' else None
        except Oksm.DoesNotExist:
            patient.c_oksm = None
        try:
            patient.kv = str(history['kv']).strip()
        except:
            pass

        try:
            patient.kp = str(history['kp']).strip()
        except:
            pass
        try:
            patient.stro = str(history['stro']).strip()
        except:
            pass

        try:
            patient.cj = CJ.objects.get(naim=str(history['cj']).lower(), dateend=None) if history[
                                                                                              'cj'] != None and \
                                                                                          history[
                                                                                              'cj'] != '' else None
        except CJ.DoesNotExist:
            patient.cj = None

        try:
            patient.okatog = str(history['okatog']).strip() if str(history['okatog']).strip() != None and str(history['okatog']).strip() != "" else ''
        except:
            pass
        try:
            patient.okatop = str(history['okatop']).strip() if str(history['okatop']).strip() != None and str(history['okatop']).strip() != "" else ''
        except:
            pass
        # I.Карта больного с ОНМК
        if ( sluchay.dskz != None and sluchay.dskz.kod in ds_l) and (sluchay.otd.naim in otde_l):
            if sluchay.onmk_sp != None:
                self.update_onmk_sp(sluchay.onmk_sp, history['onmk_sp'])
                sluchay.onmk_sp.save()
            else:
                onmk_sp = Onmk_sp()
                onmk_sp.save()
                self.update_onmk_sp(onmk_sp, history['onmk_sp'])
                onmk_sp.save()
                sluchay.onmk_sp = onmk_sp
            if (sluchay.rslt.tip_name in resl_l):
                if sluchay.onmk_li != None:
                    self.update_onmk_li(sluchay.onmk_li, history['onmk_li'])
                    sluchay.onmk_li.save()
                else:
                    onmk_li = Onmk_li()
                    onmk_li.save()
                    self.update_onmk_li(onmk_li, history['onmk_li'])
                    onmk_li.save()
                    sluchay.onmk_li = onmk_li
        else:
            if sluchay.onmk_sp != None:
                id = sluchay.onmk_sp.id
                sluchay.onmk_sp = None
                Onmk_sp.objects.get(id=id).delete()
            if sluchay.onmk_li != None:
                id = sluchay.onmk_li.id
                sluchay.onmk_li = None
                Onmk_li.objects.get(id=id).delete()
        # J.Карта онкобольного
        if (sluchay.dskz != None and str(sluchay.dskz.kod)[:1] == "C"):
            if sluchay.onk_sl != None:
                self.update_onk_sl(sluchay.onk_sl, history)
                sluchay.onk_sl.save()
            else:
                onk_sl = Onk_sl()
                onk_sl.save()
                self.update_onk_sl(onk_sl, history)
                onk_sl.save()
                sluchay.onk_sl = onk_sl

            if sluchay.b_diag != None:
                self.update_b_diag(sluchay.b_diag, history)
                sluchay.b_diag.save()
            else:
                b_diag = B_diag()
                b_diag.save()
                self.update_b_diag(b_diag, history)
                b_diag.save()
                sluchay.b_diag = b_diag

            if sluchay.cons != None:
                self.update_cons(sluchay.cons, history)
                sluchay.cons.save()
            else:
                cons = Cons()
                cons.save()
                self.update_cons(cons, history)
                cons.save()
                sluchay.cons = cons

            if sluchay.onk_usl != None:
                self.update_onk_usl(sluchay.onk_usl, history)
                sluchay.onk_usl.save()
            else:
                onk_usl = Onk_usl()
                onk_usl.save()
                self.update_onk_usl(onk_usl, history)
                onk_usl.save()
                sluchay.onk_usl = onk_usl

            if sluchay.b_prot != None:
                self.update_b_prot(sluchay.b_prot, history)
                sluchay.b_prot.save()
            else:
                b_prot = B_prot()
                b_prot.save()
                self.update_b_prot(b_prot, history)
                b_prot.save()
                sluchay.b_prot = b_prot

            if sluchay.napr != None:
                self.update_napr(sluchay.napr, history)
                sluchay.napr.save()
            else:
                napr = Napr()
                napr.save()
                self.update_napr(napr, history)
                napr.save()
                sluchay.napr = napr
            try:
                sluchay.c_zab = V027.objects.get(n_cz=str(history['c_zab']), dateend=None) if history[
                                                                                                          'c_zab'] != None and \
                                                                                                      history[
                                                                                                          'c_zab'] != '' else None
            except V027.DoesNotExist:
                sluchay.c_zab = None
        # K.Мо прикрепления
        try:
            sluchay.pmg = F003.objects.get(naim=history['pmg'], dateend=None) if \
            history['pmg'] != None and history[
                'pmg'] != '' else None
        except F003.DoesNotExist:
            sluchay.pmg = None

        patient.save()
        sluchay.save()


        # if history['ksg_sop_helper'] is not None:
        #     try:
        #         sluchay.ksg_sop = group_kc_group.objects.get(id=history['ksg_sop_helper'], dateend=None) if history['ksg_sop_helper'] != '' else None
        #     except group_kc_group.DoesNotExist:
        #         sluchay.ksg_sop = None
        # else:
        try:
            g = group_kc_group.objects.values('id').filter(code_usl_kz=history['ksg_sop'],mkb_10=history['dsc']['kod'], dateend=None)
            if g.count()> 0:
                g = g[0]
            sluchay.ksg_sop = group_kc_group.objects.get(id=g['id'])
        except:
            sluchay.ksg_sop = None

        sluchay.save()
        # else:
            # print(history['ksg_sop'])
            # try:
            #     g = group_kc_group.objects.values('id').filter(code_usl_kz=history['ksg_sop'], dateend=None)[:1][0]
            #     sluchay.ksg_sop = group_kc_group.objects.get(id=g['id'])
            # except:
            #     sluchay.ksg_sop = None

        try:
            d = {}
            d['dskz'] = ds
            d['dsc'] = sluchay.dsc.kod if sluchay.dsc else ''
            d['ds_osl'] = sluchay.ds_osl.kod if sluchay.ds_osl else ''
            d['ksg_osn'] = history['ksg_osn']
            d['ksg_osn_all'] = history['ksg_osn_all']
            d['pol'] = str(patient.pol.id_pol) if patient.pol else ''
            dr = patient.datr.split('-')
            d['datr'] = f'{dr[2]}-{dr[1]}-{dr[0]}'
            op = sluchay.oper.filter(pop=True) if sluchay.oper else 0
            if op.count() > 0:
                op = op[0]
            else:
                op = 0
            d['oper_osn'] = op.kod_op.kod if op != 0 else ''
            d['oopkk'] = history['oopkk']
            d['code_usl'] = history['code_usl']
            dv = sluchay.datv.split('-')
            d['datv'] = f'{dv[2]}-{dv[1]}-{dv[0][2:]}'
            dp = sluchay.datp.split('-')
            d['datp'] = f'{dp[2]}-{dp[1]}-{dp[0][2:]}'
        except:
            pass

        try:
            if sluchay.ksg_osn == None:
                r = requests.get('http://arknet.okb2-tmn.ru/hospital/search/check_ksg', params=d)
                r_id = r.json()['r']
                try:
                    sluchay.ksg_osn = group_kc_group.objects.get(id=r_id)
                except group_kc_group.DoesNotExist:
                    sluchay.ksg_osn = None
                except:
                    pass
        except:
            pass

        sluchay.save()
        try:
            if sluchay.ksg_osn == None:
                data_ksg = history['data_ksg']
                r = requests.get('http://arknet.okb2-tmn.ru/hospital/search/check_ksg', params=data_ksg)
                r_id = r.json()['r']
                try:
                    sluchay.ksg_osn = group_kc_group.objects.get(id=r_id)
                except group_kc_group.DoesNotExist:
                    sluchay.ksg_osn = None
                except:
                    pass
        except:
            pass
        sluchay.save()
        if sluchay.ksg_osn == None:
            try:
                g = group_kc_group.objects.values('id').filter(code_usl_kz=history['ksg_osn'], dateend=None)[:1][0]
                sluchay.ksg_osn = group_kc_group.objects.get(id=g['id'])
            except:
                sluchay.ksg_osn = None

        sluchay.save()

    def update_le_vr(self, le_vr, data,otd):
        try:
            le_vr.kd = int(str(data['N']).strip()) if data['N'] != None and data['N'] != "" else None
        except ValueError:
            print('error int le_vr.kd')
            
        try:
            le_vr.aro = str(data['aro']).strip()
        except:
            pass
        try:
            le_vr.otd = int(str(data['otd']).strip()) if ((data['otd'] != None) and (data['otd'] != "")) else None
        except ValueError:
            print('error int le_vr.otd')
        except:
            pass
        try:
            le_vr.prof_k = V020.objects.get(k_prname=str(data['prof_k']),dateend=None) if data['prof_k'] != None and \
                                                                                              data['prof_k'] != '' else None
        except V020.DoesNotExist:
            le_vr.prof_k = None

        # try:
        #     le_vr.kod = Vra.objects.get(kod=str(data['kod']),dateend=None) if data['kod'] != None and data['kod'] != '' else None
        # except Vra.DoesNotExist:
        #     le_vr.kod = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=data['kod'],dateend=None)[0]['id']
        #     le_vr.kod = Vra.objects.get(id=vra)
        # self.get_vra(self, otd.kod, data['kodan'])

        # le_vr.kod = self.get_vra(otd.kod,data['kod']) if otd != None and otd != '' else None
        try:
            le_vr.kod = self.get_vra(None,data['kod']) if otd != None and otd != '' else None
        except:
            pass


        try:
            le_vr.spec = V021.objects.get(postname=str(data['spec']).strip(),dateend=None) if data['spec'] != None and data['spec'] != '' else None
        except V021.DoesNotExist:
            le_vr.spec = None

        try:
            le_vr.aro_n = int(str(data['aro_n']).strip()) if data['aro_n'] != "" and data['aro_n'] != None else None
        except ValueError:
            print('error int le_vr.aro_n')
        except:
            pass

        try:
            if data['aro_let'] != "" and data['aro_let'] != None:
                if data['aro_let'] == "1 - в течение 1 часа":
                    le_vr.aro_let = '1'
                elif data['aro_let'] == "2 - в течение 1 суток":
                    le_vr.aro_let = '2'
                elif data['aro_let'] == "3 - более чем через 1 сутки":
                    le_vr.aro_let = '3'
                else:
                    le_vr.aro_let = None
            else:
                le_vr.aro_let = None
        except:
            pass


        # if data['aro_let'] != "" and data['aro_let'] != None:
        #     if str(data['aro_let']).strip() == "1.Да":
        #         le_vr.aro_let = True
        #     elif str(data['aro_let']).strip() == "2.Нет":
        #         le_vr.aro_let = False
        #     else:
        #         le_vr.aro_let = None
        # try:
        #     le_vr.aro_let = [m for m in range(len(Le_Vr.AroLet_CHOICES)) if Le_Vr.AroLet_CHOICES[m][1] == str(data['aro_let'])][0]
        # except IndexError:
        #     le_vr.aro_let = None
        # except:
        #     pass
        try:
            if data['aro_sofa'] != None and data['aro_sofa'] != "":
                if str(data['aro_sofa']).strip() == "1.Да":
                    le_vr.aro_sofa = True
                elif str(data['aro_sofa']).strip() == "2.Нет":
                    le_vr.aro_sofa = False
                else:
                    le_vr.aro_sofa = None
        except:
            pass

        try:
            if data['aro_ivl'] != None and data['aro_ivl'] != "":
                if str(data['aro_ivl']).strip() == "1.Да":
                    le_vr.aro_ivl = True
                elif str(data['aro_ivl']).strip() == "2.Нет":
                    le_vr.aro_ivl = False
                else:
                    le_vr.aro_ivl = None
        except:
            pass

    def update_oper(self, oper, data,otd):
        try:
            oper.dato = self.str_form(data['dato']) if ((data['dato'] != None) and (data['dato'] != "")) else None
        except ValidationError:
            oper.dato = None
        except:
            pass
        try:
            oper.tm_o = str(data['tm_o']).strip() if data['tm_o'] != '' else None
        except:
            pass

        try:
            oper.py = PY.objects.get(kod=str(data['py']).strip(), dateend=None) if (
                    (data['py'] != '') and (data['py'] != None)) else None
        except PY.DoesNotExist:
            oper.py = None
        # try:
        #     oper.kod_op = V001.objects.get(kod=str(data['kod_op']).strip(), dateend=None) if (
        #             (data['kod_op'] != '') and (data['kod_op'] != None)) else None
        # except V001.DoesNotExist:
        #     oper.kod_op = None
        # except V001.MultipleObjectsReturned:
        #     kod_op = V001.objects.values('id').filter(kod=str(data['kod_op']).strip(), dateend=None)
        #     if kod_op.count() > 0:
        #         oper.kod_op = V001.objects.get(id=kod_op[0]['id'])
        #     else:
        #         oper.kod_op = None
        oper.kod_op = self.get_v001(data['kod_op'])
        try:
            oper.goc = V014.objects.get(kod=str(data['goc']).strip(), dateend=None) if (
                    (data['goc'] != '') and (data['goc'] != None)) else None
        except V014.DoesNotExist:
            oper.goc = None

        # try:
        #     oper.kodx = Vra.objects.get(kod=str(data['kodx']), dateend=None) if (
        #             (data['kodx'] != '') and (data['kodx'] != None)) else None
        # except Vra.DoesNotExist:
        #     oper.kodx = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=str(data['kodx']), dateend=None)[0]['id']
        #     oper.kodx = Vra.objects.get(id=vra)

        oper.kodx = self.get_vra(None,data['kodx'])

        try:
            if str(data['pop']).strip() == 'Да':
                oper.pop = True
            elif str(data['pop']).strip() == 'Нет':
                oper.pop = False
            else:
                oper.pop = None
        except:
            pass
        try:
            pr_osob = dict(list(map(lambda p: p, PR_OSOB.objects.values_list('kod', 'id'))))
            if len(data['pr_osob']) != 0:
                if oper.pr_osob.count() != 0:
                    oper.pr_osob.clear()
                    for p in range(len(data['pr_osob'])):
                        pr = PR_OSOB.objects.get(id=pr_osob.get(data['pr_osob'][p]), dateend=None)
                        oper.pr_osob.add(pr.pk)
                else:
                    for p in range(len(data['pr_osob'])):
                        pr = PR_OSOB.objects.get(id=pr_osob.get(data['pr_osob'][p]), dateend=None)
                        oper.pr_osob.add(pr.pk)
            else:
                oper.pr_osob.clear()
        except:
            pass

        try:
            oper.k_mm = str(data['k_mm']).strip() if ((data['k_mm'] != '') and (data['k_mm'] != None)) else None
        except:
            pass
        oper.kodxa = self.get_vra(None,data['kodxa'])
        oper.kodxa1 = self.get_vra(None,data['kodxa1'])
        # try:
        #     oper.kodxa = Vra.objects.get(kod=str(data['kodxa']), dateend=None) if (
        #             (data['kodxa'] != '') and (data['kodxa'] != None)) else None
        #     print(oper.kodxa)
        # except Vra.DoesNotExist:
        #     oper.kodxa = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=str(data['kodxa']), dateend=None)[0]['id']
        #     oper.kodxa = Vra.objects.get(id=vra)
        #
        # try:
        #     oper.kodxa1 = Vra.objects.get(kod=str(data['kodxa1']), dateend=None) if (
        #             (data['kodxa1'] != '') and (data['kodxa1'] != None)) else None
        # except Vra.DoesNotExist:
        #     oper.kodxa1 = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=str(data['kodxa1']), dateend=None)[0]['id']
        #     oper.kodxa1 = Vra.objects.get(id=vra)
        try:
            oper.obz = anesthesia.objects.get(kod=str(data['obz']).strip(), dateend=None) if (
                    (data['obz'] != '') and (data['obz'] != None)) else None
        except anesthesia.DoesNotExist:
            oper.obz = None
        #
        try:
            oper.obz_2 = anesthesia.objects.get(kod=str(data['obz_2']).strip(), dateend=None) if (
                    (data['obz_2'] != '') and (data['obz_2'] != None)) else None
        except anesthesia.DoesNotExist:
            oper.obz_2 = None
        #
        # try:
        #     oper.kodan = Vra.objects.get(kod=str(data['kodan']), dateend=None) if (
        #             (data['kodan'] != '') and (data['kodan'] != None)) else None
        # except Vra.DoesNotExist:
        #     oper.kodan = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=str(data['kodan']), dateend=None)[0]['id']
        #     oper.kodan = Vra.objects.get(id=vra)
        oper.kodan = self.get_vra(None, data['kodan'])
    def update_med_dev(self,med_dev,data):
        try:
            med_dev.date = self.str_form(data['date'])
        except:
            pass
        try:
            med_dev.code = Code_med_dev.objects.get(rzn=data['code']) if data['code'] != None and data['code'] != '' else None
        except Code_med_dev.DoesNotExist:
            med_dev.code = None
        try:
            med_dev.number_ser = data['number_ser'] if data['number_ser'] != None and data['number_ser'] != '' else ''
        except:
            pass

    def update_oslo(self, oslo, data):
        # try:
        #     oslo.inf_oper = V001.objects.get(kod=str(data['inf_oper']).strip(),dateend=None) if (
        #                 (data['inf_oper'] != None) and (data['inf_oper'] != '')) else None
        # except V001.DoesNotExist:
        #     oslo.inf_oper = None
        oslo.inf_oper = self.get_v001(data['inf_oper'])

        # try:
        #     oslo.tnvr = Vra.objects.get(kod=str(data['tnvr']),dateend=None) if (
        #                 (data['tnvr'] != '') and (data['tnvr'] != None)) else None
        # except Vra.DoesNotExist:
        #     oslo.tnvr = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=data['tnvr'],dateend=None)[0]['id']
        #     oslo.tnvr = Vra.objects.get(id=vra)
        oslo.tnvr = self.get_vra(None,data['tnvr'])

        try:
            oslo.dato = self.str_form(data['dato']) if ((data['dato'] != None) and (data['dato'] != "")) else None
        except ValidationError:
            oslo.dato = None

        try:
            oslo.osl = Pope.objects.get(kod=str(data['osl']).strip(),dateend=None) if (
                        (data['osl'] != None) and (data['osl'] != "")) else None
        except Pope.DoesNotExist:
            oslo.osl = None

        try:
            oslo.xosl = Xosl.objects.get(naim=str(data['xosl']).strip(),dateend=None) if (
                        (data['xosl'] != None) and (data['xosl'] != "")) else None
        except Xosl.DoesNotExist:
            oslo.xosl = None

        try:
            oslo.posl = Posl.objects.get(naim=str(data['posl']).strip(),dateend=None) if (
                        (data['posl'] != None) and (data['posl'] != "")) else None
        except Posl.DoesNotExist:
            oslo.posl

        try:
            oslo.aosl = Aosl.objects.get(naim=str(data['aosl']).strip(),dateend=None) if (
                        (data['aosl'] != None) and (data['aosl'] != "")) else None
        except Aosl.DoesNotExist:
            oslo.aosl = None

    def update_manpy(self, manpy, data):
        try:
            manpy.datm = self.str_form(data['datm']) if ((data['datm'] != None) and (data['datm'] != "")) else None
        except ValidationError:
            manpy.datm = None

        # try:
        #     manpy.tnvr = Vra.objects.get(kod=str(data['tnvr']),dateend=None) if (
        #                 (data['tnvr'] != '') and (data['tnvr'] != None)) else None
        # except Vra.DoesNotExist:
        #     manpy.tnvr = None
        # except Vra.MultipleObjectsReturned:
        #     vra = Vra.objects.values('id').filter(kod=data['tnvr'],dateend=None)[0]['id']
        #     manpy.tnvr = Vra.objects.get(id=vra)
        manpy.tnvr = self.get_vra(None,data['tnvr'])
        try:
            manpy.kodmn = Ab_Obsh.objects.get(kod=str(data['kodmn']).strip(),dateend=None) if (
                        (data['kodmn'] != None) and (data['kodmn'] != "")) else None
        except Ab_Obsh.DoesNotExist:
            manpy.kodmn = None
        except Ab_Obsh.MultipleObjectsReturned:
            kodmn = Ab_Obsh.objects.values('id').filter(kod=str(data['kodmn']).strip(),dateend=None) if ((data['kodmn'] != None) and (data['kodmn'] != "")) else None
            if kodmn.count() > 0:
                manpy.kodmn = Ab_Obsh.objects.get(id=kodmn[0]['id'])
        except:
            pass

        try:
            manpy.kol = str(data['kol']).strip() if data['kol'] != None and data['kol'] != '' else None
        except:
            pass

        # try:
        #     manpy.pl = [m for m in range(len(Manpy.PL_CHOICES)) if Manpy.PL_CHOICES[m][1] == str(data['pl'])][0]
        # except IndexError:
        #     manpy.pl = None
    def update_vb_s(self, vb_s, data):

        try:
            vb_s.potd = otde.objects.get(naim=str(data['potd']), dateend=None) if (
                    (data['potd'] != None) and (data['potd'] != "")) else None
        except otde.DoesNotExist:
            vb_s.potd = None

        try:
            vb_s.dat_pe = self.str_form(data['dat_pe']) if (
                        (data['dat_pe'] != None) and (data['dat_pe'] != "")) else None
        except ValidationError:
            vb_s.dat_pe = None
        except:
            pass



        try:
            vb_s.kod_y = F003.objects.get(naim=data['kod_y'],dateend=None) if (
                        (data['kod_y'] != None) and (data['kod_y'] != "")) else None
        except F003.DoesNotExist:
            vb_s.kod_y = None


        try:
            vb_s.pr_per = PR_PER.objects.get(naim=str(data['pr_per']),dateend=None) if (
                        (data['pr_per'] != None) and (data['pr_per'] != "")) else None
        except PR_PER.DoesNotExist:
            vb_s.pr_per = None








        # try:
        #     vb_s.datv = self.str_form(data['vb_s_datv']) if (
        #                 (data['vb_s_datv'] != None) and (data['vb_s_datv'] != "")) else None
        # except ValidationError:
        #     vb_s.datv = None


    def update_le_trv(self, le_trv, data):
        try:
            le_trv.details = Ds.objects.get(kod=str(data['details']['kod']),dateend=None) if (
                        (data['details']['kod'] != None) and (data['details']['kod'] != "")) else None
        except Ds.DoesNotExist:
            le_trv.details = None

        try:
            le_trv.t_trv = Trv.objects.get(naim=data['t_trv'],dateend=None) if (
                        (data['t_trv'] != None) and (data['t_trv'] != "")) else None
        except Trv.DoesNotExist:
            le_trv.t_trv = None

        # try:
        #     le_trv.trav_ns = Trvnas.objects.get(naim=data['trav_ns'],dateend=None) if (
        #                 (data['trav_ns'] != None) and (data['trav_ns'] != "")) else None
        # except Trvnas.DoesNotExist:
        #     le_trv.trav_ns = None
        try:
            if data['trav_ns'] != None and data['trav_ns'] != '':
                if str(data['trav_ns']).strip() == "Да":
                    le_trv.trav_ns = True
                elif str(data['trav_ns']).strip() == "Нет":
                    le_trv.trav_ns = False
        except KeyError:
            le_trv.trav_ns = None
        except:
            pass
    def update_vds(self, vds, data):
        try:
            vds.vds = Isfin.objects.get(naim=str(data['vds']).strip(),dateend=None) if (
                        (data['vds'] != None) and (data['vds'] != "")) else None
        except Isfin.DoesNotExist:
            vds.vds = None
        try:
            vds.sctp = str(data['sctp']).strip() if ((data['sctp'] != None) and (data['sctp'] != "")) else None
        except:
            pass
        try:
            vds.nctp = str(data['nctp']).strip() if ((data['nctp'] != None) and (data['nctp'] != "")) else None
        except:
            pass

        try:
            vds.ctkom = Skom.objects.get(naim=str(data['ctkom']).strip(),dateend=None) if (
                        (data['ctkom'] != None) and (data['ctkom'] != "")) else None
        except Skom.DoesNotExist:
            vds.ctkom = None
        except Skom.MultipleObjectsReturned:
            ctkom = Skom.objects.values('id').filter(naim=str(data['ctkom']).strip(),dateend=None) if ((data['ctkom'] != None) and (data['ctkom'] != "")) else None
            if ctkom.count() > 0:
                vds.ctkom = Skom.objects.get(id=ctkom[0]['id'])
        except:
            pass

        try:
            vds.t_pol = F008.objects.get(tip_name=str(data['t_pol']).strip(),dateend=None) if (
                        (data['t_pol'] != None) and (data['t_pol'] != "")) else None
        except F008.DoesNotExist:
            vds.t_pol = None

    def update_vb_a(self, vb_a, data):
        # try:
        #     vb_a.datv = self.str_form(data['vb_a_datv']) if (
        #                 (data['vb_a_datv'] != None) and (data['vb_a_datv'] != "")) else None
        # except ValidationError:
        #     vb_a.datv = None
        try:
            vb_a.srber = int(data['srber']) if ((data['srber'] != None) and (data['srber'] != "")) else None
        except ValueError:
            print('error int vb_a.srber')
        except:
            pass

        try:
            vb_a.n_ber = int(data['n_ber']) if ((data['n_ber'] != None) and (data['n_ber'] != "")) else None
        except ValueError:
            print('error int vb_a.n_ber')
        except:
            pass

        try:
            vb_a.pria = Tip_pb.objects.get(naim=data['pria'],dateend=None) if (
                        (data['pria'] != None) and (data['pria'] != "")) else None
        except Tip_pb.DoesNotExist:
            vb_a.pria = None

        try:
            vb_a.m_prer = Met_pb.objects.get(naim=data['m_prer'],dateend=None) if (
                        (data['m_prer'] != None) and (data['m_prer'] != "")) else None
        except Met_pb.DoesNotExist:
            vb_a.m_prer = None

    def update_disability(self, disability, data):
        try:
            disability.dat_l1 = self.str_form(data['dat_l1']) if (
                        (data['dat_l1'] != None) and (data['dat_l1'] != "")) else None
        except ValidationError:
            disability.dat_l1 = None
        except:
            pass


        try:
            disability.dat_l2 = self.str_form(data['dat_l2']) if (
                        (data['dat_l2'] != None) and (data['dat_l2'] != "")) else None
        except ValidationError:
            disability.dat_l2 = None
        except:
            pass


        try:
            if str(data['ot_ln']).strip() == "Да":
                disability.ot_ln = True
            elif str(data['ot_ln']).strip() == "Нет":
                disability.ot_ln = False
        except:
            disability.ot_ln = None

        try:
            disability.vs_bol = int(str(data['vs_bol']).strip()) if ((data['ot_ln'] != None) and (data['ot_ln'] != "")) else None
        except ValueError:
            pass
        except:
            pass

        try:
            disability.sex_bol = V005.objects.get(polname=str(data['dis_sex_bol']).strip(),dateend=None) if (
                        (data['dis_sex_bol'] != None) and (data['dis_sex_bol'] != "")) else None
        except V005.DoesNotExist:
            disability.vs_bol = None


    def update_patient_p(self, patient_p, data):
        try:
            patient_p.fam_p = str(data['fam_p']).strip() if ((data['fam_p'] != None) and (data['fam_p'] != "")) else None
        except:
            pass

        try:
            patient_p.im_p = str(data['im_p']).strip() if ((data['im_p'] != None) and (data['im_p'] != "")) else None
        except:
            pass

        try:
            patient_p.ot_p = str(data['ot_p']).strip() if ((data['ot_p'] != None) and (data['ot_p'] != "")) else None
        except:
            pass

        try:
            patient_p.pol = V005.objects.get(polname=str(data['sex_bol']).strip(),dateend=None) if (
                        (data['sex_bol'] != None) and (data['sex_bol'] != "")) else None
        except V005.DoesNotExist:
            patient_p.pol = None

        try:
            patient_p.datr = self.str_form(data['datr_p']) if data['datr_p'] != None and data['datr_p'] != '' else None
        except ValidationError:
            patient_p.datr = None
        except:
            pass

        try:
            patient_p.m_roj = str(data['mp_roj']).strip() if ((data['mp_roj'] != None) and (data['mp_roj'] != "")) else ''
        except:
            pass

        try:
            patient_p.okatog = str(data['okatog_p']).strip() if ((data['okatog_p'] != None) and (data['okatog_p'] != "")) else ''
        except:
            pass

        try:
            patient_p.okatop = str(data['okatop_p']).strip() if ((data['okatop_p'] != None) and (data['okatop_p'] != "")) else ''
        except:
            pass

        try:
            patient_p.udl_p = F011.objects.get(docname=str(data['udl_p']).strip(),dateend=None) if (
                        (data['udl_p'] != None) and (data['udl_p'] != "")) else None
        except F011.DoesNotExist:
            patient_p.udl_p = None

        try:
            patient_p.sp_pasp = str(data['sp_pasp']).strip() if ((data['sp_pasp'] != None) and (data['sp_pasp'] != "")) else None
        except:
            pass

        try:
            patient_p.np_pasp = str(data['np_pasp']).strip() if ((data['np_pasp'] != None) and (data['np_pasp'] != "")) else None
        except:
            pass

        try:
            patient_p.skom_p = Skom.objects.get(naim=str(data['skom_p']).strip(),dateend=None) if (
                        (data['skom_p'] != None) and (data['skom_p'] != "")) else None
        except Skom.DoesNotExist:
            patient_p.skom_p = None
        except Skom.MultipleObjectsReturned:
            ctkom = Skom.objects.values('id').filter(naim=str(data['ctkom']).strip(),dateend=None) if ((data['ctkom'] != None) and (data['ctkom'] != "")) else None
            if ctkom.count() > 0:
                patient_p.ctkom = Skom.objects.get(id=ctkom[0]['id'])
        except:
            pass

        try:
            patient_p.stat_p = F008.objects.get(tip_name=str(data['stat_p']).strip(),dateend=None) if (
                        (data['stat_p'] != None) and (data['stat_p'] != "")) else None
        except F008.DoesNotExist:
            patient_p.stat_p = None

        try:
            patient_p.s_pol = str(data['s_pol']).strip() if ((data['s_pol'] != None) and (data['s_pol'] != "")) else None
        except:
            pass

        try:
            patient_p.n_pol = str(data['n_pol']).strip() if ((data['n_pol'] != None) and (data['n_pol'] != "")) else None
        except:
            pass

    def update_onmk_sp(self, onmk_sp, data):
        try:
            onmk_sp.p001 = data['p001']
        except:
            pass

        try:
            onmk_sp.p002 = data['p002']
        except:
            pass

        try:
            onmk_sp.p003 = data['p003']
        except:
            pass

        try:
            onmk_sp.p004 = data['p004']
        except:
            pass

        try:
            onmk_sp.p005_1 = data['p005_1']
        except:
            pass

        try:
            onmk_sp.p005_2 = data['p005_2']
        except:
            pass

        try:
            onmk_sp.p006 = data['p006']
        except:
            pass

        try:
            onmk_sp.p007 = data['p007']
        except:
            pass

        try:
            onmk_sp.p008 = data['p008']
        except:
            pass

        try:
            onmk_sp.p009 = data['p009']
        except:
            pass

        try:
            onmk_sp.p010 = data['p010']
        except:
            pass

        try:
            onmk_sp.p011 = data['p011']
        except:
            pass

        try:
            onmk_sp.p012 = data['p012']
        except:
            pass

        try:
            onmk_sp.p013 = data['p013']
        except:
            pass

        try:
            onmk_sp.p014 = data['p014']
        except:
            pass

        try:
            onmk_sp.p015 = data['p015']
        except:
            pass

        try:
            onmk_sp.p016 = data['p016']
        except:
            pass

    def update_onmk_li(self, onmk_li, data):
        try:
            onmk_li.p001 = data['p001']
        except:
            pass

        try:
            onmk_li.p002 = data['p002']
        except:
            pass

        try:
            onmk_li.p003 = data['p003']
        except:
            pass

        try:
            onmk_li.p004 = data['p004']
        except:
            pass

        try:
            onmk_li.p005 = data['p005']
        except:
            pass

        try:
            onmk_li.p006 = data['p006']
        except:
            pass

        try:
            onmk_li.p007 = data['p007']
        except:
            pass

        try:
            onmk_li.p008 = data['p008']
        except:
            pass

        try:
            onmk_li.p009 = data['p009']
        except:
            pass

        try:
            onmk_li.p010 = data['p010']
        except:
            pass

        try:
            onmk_li.p011 = data['p011']
        except:
            pass

        try:
            onmk_li.p012 = data['p012']
        except:
            pass

        try:
            onmk_li.p013 = data['p013']
        except:
            pass

        try:
            onmk_li.p014 = data['p014']
        except:
            pass

        try:
            onmk_li.p015 = data['p015']
        except:
            pass

        try:
            onmk_li.p016 = data['p016']
        except:
            pass

        try:
            onmk_li.p017 = data['p017']
        except:
            pass

        try:
            onmk_li.p018 = data['p018']
        except:
            pass

        try:
            onmk_li.p019 = data['p019']
        except:
            pass

        try:
            onmk_li.p020 = data['p020']
        except:
            pass

        try:
            onmk_li.p021 = data['p021']
        except:
            pass

        try:
            onmk_li.p022 = data['p022']
        except:
            pass

        try:
            onmk_li.p023 = data['p023']
        except:
            pass

    def update_onk_sl(self, onk_sl, data):
        try:
            onk_sl.ds1_t = N018.objects.get(reas_name=str(data['ds1_t']).strip(),dateend=None) if (
                        (data['ds1_t'] != None) and (data['ds1_t'] != "")) else None
        except N018.DoesNotExist:
            onk_sl.ds1_t = None

        try:
            onk_sl.stad = N002.objects.get(kod_st=str(data['stad']).strip(), dateend=None,
                                           ds_st=data['dskz']['kod']) if (
                        (data['stad'] != None) and (data['stad'] != "")) else None
        except N002.DoesNotExist:
            onk_sl.stad = None

        try:
            onk_sl.onk_t = N003.objects.get(kod_t=str(data['onk_t']).strip(), dateend=None,
                                            ds_t=data['dskz']['kod']) if (
                        (data['onk_t'] != None) and (data['onk_t'] != "")) else None
        except N003.DoesNotExist:
            onk_sl.onk_t = None

        try:
            onk_sl.onk_n = N004.objects.get(kod_n=str(data['onk_n']).strip(), dateend=None,
                                            ds_n=data['dskz']['kod']) if (
                        (data['onk_n'] != None) and (data['onk_n'] != "")) else None
        except N004.DoesNotExist:

            onk_sl.onk_n = None
        try:
            onk_sl.onk_m = N005.objects.get(kod_m=str(data['onk_m']).strip(), dateend=None,
                                            ds_m=data['dskz']['kod']) if (
                        (data['onk_m'] != None) and (data['onk_m'] != "")) else None
        except N005.DoesNotExist:
            onk_sl.onk_m = None

        # try:
        #     onk_sl.mtstz = [m for m in range(len(Onk_sl.MTSTZ_CHOICES)) if Onk_sl.MTSTZ_CHOICES [m][1] == str(data['mtstz'])][0]
        # except IndexError:
        #     onk_sl.mtstz = None
        try:
            if data['mtstz'] == 'впервые':
                onk_sl.mtstz = '1'
            elif data['mtstz'] == 'ранее':
                onk_sl.mtstz = '2'
            else:
                onk_sl.mtstz = None
        except:
            pass


        # onk_sl.mtstz = int(data['mtstz']) if ((data['mtstz'] != None) and (data['mtstz'] != "")) else None
    def update_b_diag(self, b_diag, data):
        try:
            b_diag.diag_date = self.str_form(data['diag_date']) if (
                        (data['diag_date'] != None) and (data['diag_date'] != "")) else None
        except ValidationError:
            b_diag.diag_date = None
        except:
            pass

        try:
            if str(data['diag_tip']).strip() == 'Гистологический признак':
                b_diag.diag_tip = '1'
            elif str(data['diag_tip']).strip() == 'Маркёр (ИГХ)':
                b_diag.diag_tip = '2'
        except:
            pass

        try:
            b_diag.diag_code = str(data['diag_code']).strip() if ((data['diag_code'] != None) and (data['diag_code'] != "")) else None
        except:
            pass

        try:
            b_diag.diag_rslt = str(data['diag_rslt']).strip() if ((data['diag_rslt'] != None) and (data['diag_rslt'] != "")) else None
        except:
            pass

        try:
            b_diag.rec_rslt = int(str(data['rec_rslt']).strip()) if ((data['rec_rslt'] != None) and (data['rec_rslt'] != "")) else None
        except ValueError:
            print('error int b_diag.rec_rslt')
        except:
            pass

    def update_cons(self, cons, data):
        try:
            cons.pr_cons = N019.objects.get(cons_name=str(data['pr_cons']).strip(),dateend=None) if (
                        (data['pr_cons'] != None) and (data['pr_cons'] != "")) else None
        except N019.DoesNotExist:
            cons.pr_cons

        try:
            cons.dt_cons = self.str_form(data['dt_cons']) if (
                        (data['dt_cons'] != None) and (data['dt_cons'] != "")) else None
        except ValidationError:
            cons.dt_cons = None
        except:
            pass

    def update_onk_usl(self, onk_usl, data):
        try:
            onk_usl.usl_tip = N013.objects.get(tlech_name=str(data['usl_tip']).strip(),dateend=None) if (
                        (data['usl_tip'] != None) and (data['usl_tip'] != "")) else None
        except N013.DoesNotExist:
            onk_usl.usl_tip = None

        try:
            onk_usl.hir_tip = N014.objects.get(thir_name=str(data['hir_tip']).strip(),dateend=None) if (
                        (data['hir_tip'] != None) and (data['hir_tip'] != "")) else None
        except N014.DoesNotExist:
            onk_usl.hir_tip = None

    def update_b_prot(self, b_prot, data):
        try:
            b_prot.prot = N001.objects.get(prot_name=str(data['prot']).strip(),dateend=None) if (
                        (data['prot'] != None) and (data['prot'] != "")) else None
        except N001.DoesNotExist:
            b_prot.prot = None

        try:
            b_prot.d_prot = self.str_form(data['d_prot']) if (
                        (data['d_prot'] != None) and (data['d_prot'] != "")) else None
        except ValidationError:
            b_prot.d_prot = None
        except:
            pass

    def update_napr(self, napr, data):
        try:
            napr.naprdate = self.str_form(data['naprdate']) if (
                        (data['naprdate'] != None) and (data['naprdate'] != "")) else None
        except ValidationError:
            napr.naprdate = None
        except:
            pass

        try:
            napr.napr_mo = F003.objects.get(naim=str(data['napr_mo']).strip(),dateend=None) if (
                        (data['napr_mo'] != None) and (data['napr_mo'] != "")) else None
        except F003.DoesNotExist:
            napr.napr_mo = None

        try:
            napr.napr_v = V028.objects.get(n_vn=str(data['napr_v']).strip(),dateend=None) if (
                        (data['napr_v'] != None) and (data['napr_v'] != "")) else None
        except V028.DoesNotExist:
            napr.napr_v = None

        try:
            napr.napr_issl = V029.objects.get(n_met=str(data['napr_issl']).strip(),dateend=None) if (
                        (data['napr_issl'] != None) and (data['napr_issl'] != "")) else None
        except V029.DoesNotExist:
            napr.napr_issl = None
        # try:
        #     napr.napr_usl = V001.objects.get(kod=str(data['napr_usl']).strip(),dateend=None) if (
        #                 (data['napr_usl'] != None) and (data['napr_usl'] != "")) else None
        # except V001.DoesNotExist:
        #     napr.napr_usl = None
        napr.napr_usl = self.get_v001(data['napr_usl'])
    def str_form(self, st):
        try:
            st = str(st)
            if len(st) > 0:
                if len(st) != 8:
                    date = "{}-{}-{}".format(st[6:10], st[3:5], st[0:2])
                else:
                    date = "{}-{}-{}".format('20'+st[6:10], st[3:5], st[0:2])
                return date
            else:
                return None
        except:
            return None

    def get_vra(self,otd,kod):
        try:
            if otd != None:
                if self.user.ws.kod == 1:
                    kod_vra = Vra.objects.values('id', 'kod_ot').filter(kod=kod, kod_lpy='1', dateend=None).exclude(kod='')
                else:
                    kod_vra = Vra.objects.values('id', 'kod_ot').filter(kod=kod, kod_lpy='2', dateend=None).exclude(kod='')
            else:
                kod_vra = Vra.objects.values('id').filter(kod=kod, dateend=None).exclude(kod='')
            vra = None
            for k in kod_vra:
                if otd != None:
                    if otd == k['kod_ot']:
                        vra = Vra.objects.get(id=k['id'])
                        break
                else:
                    vra = Vra.objects.get(id=k['id'])
                    break
            if vra != None:
                return vra
            return None
        except:
            return None

    # def get_code_usl(self,code_usl):
    #     try:
    #         if self.user.ws.kod == 1:
    #             ksg_osn = T006.objects.get(code_usl_kz=str(code_usl).strip(),ksg__icontains='st', dateend=None) if code_usl != None and code_usl != '' else None
    #         elif self.user.ws.kod == 2:
    #             ksg_osn = T006.objects.get(code_usl_kz=str(code_usl).strip(),ksg__icontains='ds', dateend=None) if code_usl != None and code_usl != '' else None
    #     except T006.DoesNotExist:
    #         ksg_osn = None
    #     except T006.MultipleObjectsReturned:
    #         if self.user.ws.kod == 1:
    #             ksg_osn = T006.objects.values('id').filter(code_usl_kz=str(code_usl).strip(),ksg__icontains='st', dateend=None) if code_usl != None and code_usl != '' else None
    #         elif self.user.ws.kod == 2:
    #             ksg_osn = T006.objects.values('id').filter(code_usl_kz=str(code_usl).strip(),ksg__icontains='ds', dateend=None) if code_usl != None and code_usl != '' else None
    #         if ksg_osn.count() > 0:
    #             ksg_osn = T006.objects.get(id=ksg_osn[0]['id'])
    #         else:
    #             ksg_osn = None
    #     return  ksg_osn
    def get_v001(self,code):
        try:
            kod_op = V001.objects.get(kod=str(code).strip(), dateend=None) if ((code != '') and (code != None)) else None
        except V001.DoesNotExist:
            kod_op = None
        except V001.MultipleObjectsReturned:
            kod_op = V001.objects.values('id').filter(kod=str(code).strip(), dateend=None)
            if kod_op.count() > 0:
                kod_op = V001.objects.get(id=kod_op[0]['id'])
            else:
                kod_op = None
        except:
            kod_op = None

        return kod_op