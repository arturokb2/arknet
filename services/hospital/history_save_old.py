from hospital.models import *
from okb2.models import MyUser
import json
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.utils.dateparse import parse_date
from datetime import datetime


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

        # Шапка
        patient.fam = str(history['fam']).strip()
        patient.im = str(history['im']).strip()
        patient.ot = str(history['ot']).strip()

        sluchay.update_user=self.user

        try:
            patient.pol = V005.objects.get(polname=str(history['pol']).strip(),dateend=None) if history['pol'] != None else None
        except V005.DoesNotExist:
            patient.pol = None
        try:
            sluchay.datp = self.str_form(history['datp']) if history['datp'] != None and history['datp'] != '' else None
        except ValidationError:
            sluchay.datp = None

        sluchay.tm_otd = history['tm_otd']
        try:
            sluchay.datv = self.str_form(history['datv']) if history['datv'] != None and history['datv'] != '' else None
        except ValidationError:
            sluchay.datv = None
        try:
            patient.datr = self.str_form(history['datr']) if history['datr'] != None and history['datr'] != '' else None
        except ValidationError:
            patient.datr = None
        patient.save()
        sluchay.save()

        # 1.Персональные данные
        try:
            sluchay.otd = otde.objects.get(naim=str(history['otd']).strip(),dateend=None) if history['otd'] != None and history['otd'] != '' else None
        except otde.DoesNotExist:
            sluchay.otd = None
        patient.vec = history['vec']
        patient.m_roj = history['m_roj']
        try:
            patient.c_oksm = Oksm.objects.get(naim=str(history['c_oksm']).strip(),dateend=None) if history['c_oksm'] != None and \
                                                                                      history['c_oksm'] != '' else None
        except Oksm.DoesNotExist:
            patient.c_oksm = None

        patient.kv = history['kv']
        patient.kp = history['kp']
        patient.stro = history['stro']

        try:
            patient.cj = CJ.objects.get(naim=str(history['cj']).strip(),dateend=None) if history['cj'] != None and history['cj'] != '' else None
        except CJ.DoesNotExist:
            patient.cj = None
        try:
            patient.rai = [r for r in range(len(Patient.RPR_CHOICES)) if Patient.RPR_CHOICES[r][1] == str(history['rai'])][0]
        except IndexError:
            patient.rai = None
        patient.adr = history['adr']
        patient.rab = history['rab']
        patient.prof = history['prof']
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
            sluchay.lpy = F003.objects.get(naim__icontains=str(history['lpy']).strip(),dateend=None) if history['lpy'] != None and history[
                'lpy'] != '' else None
        except F003.DoesNotExist:
            sluchay.lpy = None
        sluchay.npr_num = history['npr_num']
        try:
            sluchay.npr_date = self.str_form(history['npr_date']) if history['npr_date'] != None and history[
                'npr_date'] != '' else None
        except ValidationError:
            sluchay.npr_date = None

        if history['alg'] == "Нет":
            sluchay.alg = '1'
        elif history['alg'] == "Алкогольное":
            sluchay.alg = '2'
        elif history['alg'] == "Наркотическое":
            sluchay.alg = '3'
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

        patient.save()
        sluchay.save()

        # 2. Сведения о диагнозах
        try:
            sluchay.dsny = Ds.objects.get(kod=str(history['dsny']['kod']).strip(),dateend=None) if history['dsny']['kod'] != None and \
                                                                                      history['dsny'][
                                                                                          'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dsny = None
        try:
            sluchay.ds_0 = Ds.objects.get(kod=str(history['ds_0']['kod']).strip(),dateend=None) if history['ds_0']['kod'] != None and \
                                                                                      history['ds_0'][
                                                                                          'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.ds_0 = None
        try:
            sluchay.dsk = Ds.objects.get(kod=str(history['dsk']['kod']).strip(),dateend=None) if history['dsk']['kod'] != None and \
                                                                                    history['dsk'][
                                                                                        'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dsk = None
        try:
            sluchay.dskz = Ds.objects.get(kod=str(history['dskz']['kod']).strip(),dateend=None) if history['dskz']['kod'] != None and \
                                                                                      history['dskz'][
                                                                                          'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dskz = None
        try:
            sluchay.ds_osl = Ds.objects.get(kod=str(history['ds_osl']['kod']).strip(),dateend=None) if history['ds_osl'][
                                                                                              'kod'] != None and \
                                                                                          history['ds_osl'][
                                                                                              'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.ds_osl = None
        try:
            sluchay.dsc = Ds.objects.get(kod=str(history['dsc']['kod']).strip(),dateend=None) if history['dsc']['kod'] != None and \
                                                                                    history['dsc'][
                                                                                        'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dsc = None
        try:
            sluchay.dson = Ds.objects.get(kod=str(history['dson']['kod']).strip(),dateend=None) if history['dson']['kod'] != None and \
                                                                                      history['dson'][
                                                                                          'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dson = None
        try:
            sluchay.dat_otd = self.str_form(str(history['dat_otd']).strip()) if history['dat_otd'] != None and history[
                'dat_otd'] != '' else None
        except ValidationError:
            sluchay.dat_otd = None
        sluchay.tm_otd_1 = history['tm_otd_d']
        try:
            sluchay.icx = V012.objects.get(id_iz=[i for i in str(history['icx']).split(' ') if i.isdigit()][0]) if (
                        (history['icx'] != None) and (history['icx'] != '')) else None
        except V012.DoesNotExist:
            sluchay.icx = None
        try:
            sluchay.rslt = V009.objects.get(id_tip=[r for r in str(history['rslt']).split(' ') if r.isdigit()][0]) if (
                        (history['rslt'] != None) and (history['rslt'] != '')) else None
        except V009.DoesNotExist:
            sluchay.rslt = None

        sluchay.save()

        # 3.Койко-дни
        if history['le_vr'] != None and len(history['le_vr']) > 0:
            if sluchay.le_vr != None:
                self.update_le_vr(sluchay.le_vr, history, sluchay)
                sluchay.le_vr.save()
            else:
                le_vr = Le_Vr()
                le_vr.save()
                self.update_le_vr(le_vr, history, sluchay)
                le_vr.save()
                sluchay.le_vr = le_vr
        else:
            if sluchay.le_vr != None:
                id = sluchay.le_vr.id
                sluchay.le_vr = None
                Le_Vr.objects.get(id=id).delete()

        sluchay.save()

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
                    self.update_oper(oper, history['oper'][o])
                    oper.save()
            else:
                opers = sluchay.oper.values('id')
                for o in opers:
                    Oper.objects.get(id=o['id']).delete()
                for o in range(len(history['oper'])):
                    oper = Oper()
                    oper.save()
                    self.update_oper(oper, history['oper'][o])
                    oper.save()
                    sluchay.oper.add(oper)
        else:
            if sluchay.oper.count() > 0:
                opers = sluchay.oper.values('id')
                for o in opers:
                    Oper.objects.get(id=o['id']).delete()

        sluchay.save()
        try:
            oper.save()
        except:
            pass
        # 5.Клинико-стат.гр.заболев-я
        try:
            if self.user.ws.kod == 1:
                sluchay.ksg_osn = T006.objects.get(code_usl_kz=str(history['ksg_osn']).strip(), ksg__icontains='st',dateend=None) if \
                history['ksg_osn'] != None and history['ksg_osn'] != '' else None
            elif self.user.ws.kod == 2:
                sluchay.ksg_osn = T006.objects.get(code_usl_kz=str(history['ksg_osn']).strip(), ksg__icontains='ds',dateend=None) if \
                history['ksg_osn'] != None and history['ksg_osn'] != '' else None
        except T006.DoesNotExist:
            sluchay.ksg_osn = None
        except T006.MultipleObjectsReturned:
            sluchay.ksg_osn = None
        try:
            sluchay.oopkk = group_kc_dkk.objects.get(kod=history['oopkk'], ksg_1=history['ksg_osn_all'],dateend=None)
        except group_kc_dkk.DoesNotExist:
            sluchay.oopkk = None

        try:
            if self.user.ws.kod == 1:
                sluchay.ksg_sop = T006.objects.get(code_usl_kz=str(history['ksg_sop']).strip(), ksg__icontains='st',dateend=None) if \
                history['ksg_sop'] != None and history['ksg_sop'] != '' else None
            elif self.user.ws.kod == 2:
                sluchay.ksg_sop = T006.objects.get(code_usl_kz=str(history['ksg_sop']).strip(), ksg__icontains='ds',dateend=None) if \
                history['ksg_sop'] != None and history['ksg_sop'] != '' else None
        except T006.DoesNotExist:
            sluchay.ksg_sop = None

        try:
            sluchay.code_usl = T003.objects.get(kod=str(history['code_usl']).strip(),dateend=None) if history['code_usl'] != None and \
                                                                                         history[
                                                                                             'code_usl'] != None != '' else None
        except T003.DoesNotExist:
            sluchay.code_usl = None
        except T003.MultipleObjectsReturned:
            sluchay.code_usl = None

        try:
            sluchay.iddokt = Vra.objects.get(kod=history['iddoc'],dateend=None) if (
                        (history['iddoc'] != '') and (history['iddoc'] != None)) else None
        except Vra.DoesNotExist:
            sluchay.iddokt = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=history['iddoc'],dateend=None)[0]['id']
            sluchay.iddokt = Vra.objects.get(id=vra)

        sluchay.metod_hmp = history['metod_hmp']
        sluchay.vid_hmp = history['vid_hmp']
        try:
            sluchay.code_usl_vt = Tar_vt.objects.get(kod=history['code_usl_vt'],dateend=None)
        except Tar_vt.DoesNotExist:
            sluchay.code_usl_vt = None
        except Sluchay.MultipleObjectsReturned:
            sluchay.code_usl_vt = None

        sluchay.save()

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
            pass
            # if oper.oslo.count() > 0:
            #     oslos = oper.oslo.values('id')
            #     for o in oper:
            #         Oslo.objects.get(id=o['id']).delete()
        try:
            oper.save()
            sluchay.save()
        except:
            pass
        # 7.Трудоспособность
        try:
            sluchay.trs = Trs.objects.get(naim=str(history['trs']).upper(),dateend=None) if history['trs'] != None and history[
                'trs'] != '' else None
        except Trs.DoesNotExist:
            sluchay.trs = None

        sluchay.save()

        # 8.Манипуляции
        # print(history['manipulation'])
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
                    # print(history['manipulation'][m])
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

        sluchay.save()
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

        sluchay.save()

        # А.Патанатомический Ds
        try:
            sluchay.wskr_date = self.str_form(history['wskr_date']) if (
                        (history['wskr_date'] != None) and (history['wskr_date'] != "")) else None
        except ValidationError:
            sluchay.wskr_date = None
        sluchay.tm_let = history['tm_let'] if history['tm_let'] != None and history['tm_let'] != '' else None
        try:
            sluchay.pri = Prli.objects.get(naim=str(history['pri']).strip(),dateend=None) if history['pri'] != None and history[
                'pri'] != '' else None
        except Prli.DoesNotExist:
            sluchay.pri = None
        try:
            sluchay.ds_let = Ds.objects.get(kod=str(history['ds_let']['kod']).strip(),dateend=None) if history['ds_let'][
                                                                                              'kod'] != None and \
                                                                                          history['ds_let'][
                                                                                              'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.ds_let = None

        if history['wskr'] == "без вскрытия":
            sluchay.wskr = '1'
        elif history['wskr'] == "патологоанатом.":
            sluchay.wskr = '2'
        elif history['wskr'] == "судебное":
            sluchay.wskr = '3'

        try:
            sluchay.dspat = Ds.objects.get(kod=str(history['dspat']['kod']).strip(),dateend=None) if history['dspat'][
                                                                                            'kod'] != None and \
                                                                                        history['dspat'][
                                                                                            'kod'] != '' else None
        except Ds.DoesNotExist:
            sluchay.dspat = None

        if history['rasxp'] == "Да":
            sluchay.rasxp = '1'
        elif history['rasxp'] == "Нет":
            sluchay.rasxp = '2'
        try:
            sluchay.otd_y = otde.objects.get(naim=str(history['otd_y']).strip(),dateend=None) if history['otd_y'] != None else None
        except otde.DoesNotExist:
            sluchay.otd_y = None

        sluchay.save()

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

        sluchay.save()

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
            patient.udl = F011.objects.get(docname=str(history['udl']).strip(),dateend=None) if history['udl'] != None and history[
                'udl'] != '' else None
        except F011.DoesNotExist:
            patient.udl = None

        patient.s_pasp = str(history['s_pasp']).strip()
        patient.n_pasp = str(history['n_pasp']).strip()
        try:
            patient.docdate = self.str_form(history['docdate']) if (
                        (history['docdate'] != None) and (history['docdate'] != "")) else None
        except ValidationError:
            patient.docdate = None
        patient.docorg = str(history['docorg']).strip()
        patient.ss = str(history['ss']).strip()

        sluchay.save()
        patient.save()
        # D.Прерывание беременности
        if ((history['vb_a_datv'] != None and history['vb_a_datv'] != "") or (
                history['pria'] != None and history['pria'] != "") or (
                history['m_prer'] != None and history['m_prer'] != "")):
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

        sluchay.save()

        # E.Лист нетрудоспособности
        if ((history['dat_l1'] != None and history['dat_l1']) or (history['dat_l2'] != None and history['dat_l2'])):
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
        sluchay.save()

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

        patient.save()

        # G.Адрес проживания
        try:
            patient.c_oksm = Oksm.objects.get(naim=str(history['c_oksm']).strip(),dateend=None) if history['c_oksm'] != None and \
                                                                                      history['c_oksm'] != '' else None
        except Oksm.DoesNotExist:
            patient.c_oksm = None
        patient.kv = history['kv']
        patient.kp = history['kp']
        patient.stro = history['stro']
        try:
            patient.cj = CJ.objects.get(naim=str(history['cj']).strip(),dateend=None) if history['cj'] != None and history[
                'cj'] != '' else None
        except CJ.DoesNotExist:
            patient.cj = None

        try:
            patient.rai = [r for r in range(
                len(Patient.RPR_CHOICES)) if Patient.RPR_CHOICES[r][1] == str(history['rai'])][0]
        except IndexError:
            patient.rai = None

        # patient.okatog = history['okatog']
        # patient.okatop = history['okatop']

        patient.save()

        # I.Карта больного с ОНМК
        try:
            if ((sluchay.dskz != None and sluchay.dskz != '') and (sluchay.dskz.kod in ds_l) and (sluchay.otd.naim in otde_l)):
                
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
        except:
            pass

        sluchay.save()
        # J.Карта онкобольного
        try:
            if (str(sluchay.dskz.kod)[:1] == "C"):
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

        except IndexError:
            pass

        try:
            sluchay.c_zab = V027.objects.get(n_cz=str(history['c_zab']).strip(),dateend=None) if history['c_zab'] != None and \
                                                                                    history['c_zab'] != '' else None
        except V027.DoesNotExist:
            sluchay.c_zab = None

        sluchay.save()

        # K.Мо прикрепления
        try:
            sluchay.pmg = F003.objects.get(naim__icontains=str(history['pmg']).strip(),dateend=None) if history['pmg'] != None and history[
                'pmg'] != '' else None
        except F003.DoesNotExist:
            sluchay.pmg = None
        sluchay.save()

    def update_le_vr(self, le_vr, data, sluchay):
        le_vr.kd = int(data['le_vr']['N']) if ((data['le_vr']['N'] != None) and (data['le_vr']['N'] != "")) else None
        le_vr.aro = str(data['le_vr']['aro'])
        # if str(data['le_vr']['aro']) != '0' and str(data['le_vr']['aro']) != '':
        #     sluchay.gwf = data['gwf']
        #     sluchay.u_gwf = data['u_gwf']
        #     sluchay.sofa = data['sofa']
        #     sluchay.iwl = data['iwl']
        # else:
        #     sluchay.gwf = None
        #     sluchay.u_gwf = None
        #     sluchay.sofa = None
        #     sluchay.iwl = None
        try:
            le_vr.otd = otde.objects.get(naim=str(data['le_vr']['otd']).strip(),dateend=None) if data['le_vr']['otd'] != None and \
                                                                                    data['le_vr']['otd'] != '' else None
        except otde.DoesNotExist:
            le_vr.otd = None
        le_vr.otd = int(data['le_vr']['otd']) if (
                    (data['le_vr']['otd'] != None) and (data['le_vr']['otd'] != "")) else None
        try:
            le_vr.prof_k = V020.objects.get(k_prname=str(data['le_vr']['prof_k']).strip(),dateend=None) if data['le_vr'][
                                                                                                  'prof_k'] != None and \
                                                                                              data['le_vr'][
                                                                                                  'prof_k'] != '' else None
        except V020.DoesNotExist:
            le_vr.prof_k = None
        try:
            le_vr.kod = Vra.objects.get(kod=str(data['le_vr']['kod']).strip(),dateend=None) if data['le_vr']['kod'] != None and \
                                                                                  data['le_vr']['kod'] != '' else None
        except Vra.DoesNotExist:
            le_vr.kod = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=data['le_vr']['kod'],dateend=None)[0]['id']
            le_vr.kod = Vra.objects.get(id=vra)
        try:
            le_vr.spec = V021.objects.get(postname=str(data['le_vr']['spec']),dateend=None) if data['le_vr']['spec'] != None and \
                                                                                  data['le_vr']['spec'] != '' else None
        except V021.DoesNotExist:
            le_vr.spec = None
        try:
            le_vr.aro_n = int(data['le_vr']['aro_n']) if (data['le_vr']['aro_n'] != 0) else None
        except :
           pass
        
        try:

            if data['le_vr']['aro_let'] == "1.Да":
                le_vr.aro_let = True
            elif data['le_vr']['aro_let'] == "2.Нет":
                le_vr.aro_let = False
            else:
                le_vr.aro_let = None
        except:
            pass
        try:
            if data['le_vr']['aro_sofa'] == "1.Да":
                le_vr.aro_sofa = True
            elif data['le_vr']['aro_sofa'] == "2.Нет":
                le_vr.aro_sofa = False
            else:
                le_vr.aro_sofa = None
        except:
            pass
        try:
            if data['le_vr']['aro_ivl'] == "1.Да":
                le_vr.aro_ivl = True
            elif data['le_vr']['aro_ivl'] == "2.Нет":
                le_vr.aro_ivl = False
            else:
                le_vr.aro_ivl = None
        except:
            pass

    def update_oper(self, oper, data):
        try:
            oper.dato = self.str_form(data['dato']) if ((data['dato'] != None) and (data['dato'] != "")) else None
        except ValidationError:
            oper.dato = None
        oper.tm_o = data['tm_o'] if data['tm_o'] != '' else None
        try:
            oper.py = PY.objects.get(kod=str(data['py']).strip(),dateend=None) if (
                        (data['py'] != '') and (data['py'] != None)) else None
        except PY.DoesNotExist:
            oper.py = None
        try:
            oper.kod_op = V001.objects.get(kod=str(data['kod_op']).strip(),dateend=None) if (
                        (data['kod_op'] != '') and (data['kod_op'] != None)) else None
        except V001.DoesNotExist:
            oper.kod_op = None
        try:
            oper.goc = V014.objects.get(id_tip=str(data['goc']).strip(),dateend=None) if (
                        (data['goc'] != '') and (data['goc'] != None)) else None
        except V014.DoesNotExist:
            oper.goc = None
        try:
            oper.kodx = Vra.objects.get(kod=str(data['kodx']).strip(),dateend=None) if (
                        (data['kodx'] != '') and (data['kodx'] != None)) else None
        except Vra.DoesNotExist:
            oper.kodx = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=str(data['kodx']).strip(),dateend=None)[0]['id']
            oper.kodx = Vra.objects.get(id=vra)
        if data['pop'] == 'Да':
            oper.pop = True
        elif data['pop'] == 'Нет':
            oper.pop = False
        else:
            oper.pop = None
        pr_osob = dict(list(map(lambda p: p, PR_OSOB.objects.values_list('kod', 'id'))))
        if len(data['pr_osob']) != 0:
            if oper.pr_osob.count() != 0:
                oper.pr_osob.clear()
                for p in range(len(data['pr_osob'])):
                    pr = PR_OSOB.objects.get(id=pr_osob.get(data['pr_osob'][p]),dateend=None)
                    oper.pr_osob.add(pr.pk)
            else:
                for p in range(len(data['pr_osob'])):
                    pr = PR_OSOB.objects.get(id=pr_osob.get(data['pr_osob'][p]),dateend=None)
                    oper.pr_osob.add(pr.pk)
        else:
            oper.pr_osob.clear()

        oper.k_mm = data['k_mm'] if ((data['k_mm'] != '') and (data['k_mm'] != None)) else None
        try:
            oper.kodxa = Vra.objects.get(kod=str(data['kodxa']).strip(),dateend=None) if (
                        (data['kodxa'] != '') and (data['kodxa'] != None)) else None
        except Vra.DoesNotExist:
            oper.kodxa = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=str(data['kodxa']).strip(),dateend=None)[0]['id']
            oper.kodxa = Vra.objects.get(id=vra)
        try:
            oper.kodxa1 = Vra.objects.get(kod=str(data['kodxa1']).strip(),dateend=None) if (
                        (data['kodxa1'] != '') and (data['kodxa1'] != None)) else None
        except Vra.DoesNotExist:
            oper.kodxa1 = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=str(data['kodxa1']).strip(),dateend=None)[0]['id']
            oper.kodxa1 = Vra.objects.get(id=vra)
        try:
            oper.obz = anesthesia.objects.get(kod=str(data['obz']).strip(),dateend=None) if (
                        (data['obz'] != '') and (data['obz'] != None)) else None
        except anesthesia.DoesNotExist:
            oper.obz = None

        try:
            oper.obz_2 = anesthesia.objects.get(kod=str(data['obz_2']).strip(),dateend=None) if (
                        (data['obz_2'] != '') and (data['obz_2'] != None)) else None
        except anesthesia.DoesNotExist:
            oper.obz_2 = None

        try:
            oper.kodan = Vra.objects.get(kod=str(data['kodan']).strip(),dateend=None) if (
                        (data['kodan'] != '') and (data['kodan'] != None)) else None
        except Vra.DoesNotExist:
            oper.kodan = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=str(data['kodan']).strip(),dateend=None)[0]['id']
            oper.kodan = Vra.objects.get(id=vra)

    def update_oslo(self, oslo, data):
        try:
            oslo.inf_oper = V001.objects.get(kod=str(data['inf_oper']).strip(),dateend=None) if (
                        (data['inf_oper'] != None) and (data['inf_oper'] != '')) else None
        except V001.DoesNotExist:
            oslo.inf_oper = None
        try:
            oslo.tnvr = Vra.objects.get(kod=str(data['tnvr']).strip(),dateend=None) if (
                        (data['tnvr'] != '') and (data['tnvr'] != None)) else None
        except Vra.DoesNotExist:
            oslo.tnvr = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=data['tnvr'],dateend=None)[0]['id']
            oslo.tnvr = Vra.objects.get(id=vra)
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
        try:
            manpy.tnvr = Vra.objects.get(kod=str(data['tnvr']).strip(),dateend=None) if (
                        (data['tnvr'] != '') and (data['tnvr'] != None)) else None
        except Vra.DoesNotExist:
            manpy.tnvr = None
        except Vra.MultipleObjectsReturned:
            vra = Vra.objects.values('id').filter(kod=data['tnvr'],dateend=None)[0]['id']
            manpy.tnvr = Vra.objects.get(id=vra)
        try:
            manpy.kodmn = Ab_Obsh.objects.get(kod=str(data['kodmn']).strip(),dateend=None) if (
                        (data['kodmn'] != None) and (data['kodmn'] != "")) else None
        except Ab_Obsh.DoesNotExist:
            manpy.kodmn = None
        manpy.kol = data['kol']
        print(manpy.kol) 
        try:
            manpy.pl = [m for m in range(len(Manpy.PL_CHOICES)) if Manpy.PL_CHOICES[m][1] == str(data['pl']).strip()][0]
        except IndexError:
            manpy.pl = None

    def update_vb_s(self, vb_s, data):
        try:
            vb_s.kod_y = F003.objects.get(naim__icontains=str(data['kod_y']).strip(),dateend=None) if (
                        (data['kod_y'] != None) and (data['kod_y'] != "")) else None
        except F003.DoesNotExist:
            vb_s.kod_y = None
        try:
            vb_s.pr_per = PR_PER.objects.get(naim=str(data['pr_per']).strip(),dateend=None) if (
                        (data['pr_per'] != None) and (data['pr_per'] != "")) else None
        except PR_PER.DoesNotExist:
            vb_s.pr_per
        try:
            vb_s.dat_pe = self.str_form(data['dat_pe']) if (
                        (data['dat_pe'] != None) and (data['dat_pe'] != "")) else None
        except ValidationError:
            vb_s.dat_pe = None
        try:
            vb_s.potd = otde.objects.get(naim=str(data['potd']).strip(),dateend=None) if (
                        (data['potd'] != None) and (data['potd'] != "")) else None
        except otde.DoesNotExist:
            vb_s.potd = None
        try:
            vb_s.datv = self.str_form(data['vb_s_datv']) if (
                        (data['vb_s_datv'] != None) and (data['vb_s_datv'] != "")) else None
        except ValidationError:
            vb_s.datv = None

    def update_le_trv(self, le_trv, data):
        try:
            le_trv.details = Ds.objects.get(kod=str(data['details']['kod']).strip(),dateend=None) if (
                        (data['details']['kod'] != None) and (data['details']['kod'] != "")) else None
        except Ds.DoesNotExist:
            le_trv.details = None
        try:
            le_trv.t_trv = Trv.objects.get(naim=data['t_trv'],dateend=None) if (
                        (data['t_trv'] != None) and (data['t_trv'] != "")) else None
        except Trv.DoesNotExist:
            le_trv.t_trv = None
        try:
            le_trv.trav_ns = Trvnas.objects.get(naim=data['trav_ns'],dateend=None) if (
                        (data['trav_ns'] != None) and (data['trav_ns'] != "")) else None
        except Trvnas.DoesNotExist:
            le_trv.trav_ns = None

    def update_vds(self, vds, data):
        try:
            vds.vds = Isfin.objects.get(naim=str(data['vds']).strip(),dateend=None) if (
                        (data['vds'] != None) and (data['vds'] != "")) else None
        except Isfin.DoesNotExist:
            vds.vds = None
        vds.sctp = str(data['sctp']).strip() if ((data['sctp'] != None) and (data['sctp'] != "")) else None
        vds.nctp = str(data['nctp']).strip() if ((data['nctp'] != None) and (data['nctp'] != "")) else None
        try:
            vds.ctkom = Skom.objects.get(naim__icontains=str(data['ctkom']).strip(),dateend=None) if (
                        (data['ctkom'] != None) and (data['ctkom'] != "")) else None
        except Skom.DoesNotExist:
            vds.ctkom = None
        try:
            vds.t_pol = F008.objects.get(tip_name=str(data['t_pol']).strip(),dateend=None) if (
                        (data['t_pol'] != None) and (data['t_pol'] != "")) else None
        except F008.DoesNotExist:
            vds.t_pol = None

    def update_vb_a(self, vb_a, data):
        try:
            vb_a.datv = self.str_form(data['vb_a_datv']) if (
                        (data['vb_a_datv'] != None) and (data['vb_a_datv'] != "")) else None
        except ValidationError:
            vb_a.datv = None
        vb_a.srber = int(data['srber']) if ((data['srber'] != None) and (data['srber'] != "")) else None
        vb_a.n_ber = int(data['n_ber']) if ((data['n_ber'] != None) and (data['n_ber'] != "")) else None
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

        try:
            disability.dat_l2 = self.str_form(data['dat_l2']) if (
                        (data['dat_l2'] != None) and (data['dat_l2'] != "")) else None
        except ValidationError:
            disability.dat_l2 = None
        try:
            if data['ot_ln'] == "Да":
                disability.ot_ln = True
            elif data['ot_ln'] == "Нет":
                disability.ot_ln = False
        except:
            pass

        disability.vs_bol = data['vs_bol'] if ((data['ot_ln'] != None) and (data['ot_ln'] != "")) else None
        try:
            disability.sex_bol = V005.objects.get(polname=data['dis_sex_bol'],dateend=None) if (
                        (data['dis_sex_bol'] != None) and (data['dis_sex_bol'] != "")) else None
        except V005.DoesNotExist:
            disability.vs_bol = None

    def update_patient_p(self, patient_p, data):
        patient_p.fam_p = data['fam_p'] if ((data['fam_p'] != None) and (data['fam_p'] != "")) else None
        patient_p.im_p = data['im_p'] if ((data['im_p'] != None) and (data['im_p'] != "")) else None
        patient_p.ot_p = data['ot_p'] if ((data['ot_p'] != None) and (data['ot_p'] != "")) else None
        try:
            patient_p.pol = V005.objects.get(polname=str(data['sex_bol']).strip(),dateend=None) if (
                        (data['sex_bol'] != None) and (data['sex_bol'] != "")) else None
        except V005.DoesNotExist:
            patient_p.pol = None
        patient_p.m_roj = data['mp_roj'] if ((data['mp_roj'] != None) and (data['mp_roj'] != "")) else None
        try:
            patient_p.udl_p = F011.objects.get(docname=str(data['udl_p']).strip(),dateend=None) if (
                        (data['udl_p'] != None) and (data['udl_p'] != "")) else None
        except F011.DoesNotExist:
            patient_p.udl_p = None
        patient_p.sp_pasp = data['sp_pasp'] if ((data['sp_pasp'] != None) and (data['sp_pasp'] != "")) else None
        patient_p.np_pasp = data['np_pasp'] if ((data['np_pasp'] != None) and (data['np_pasp'] != "")) else None
        try:
            patient_p.skom_p = Skom.objects.get(naim=str(data['skom_p']).strip(),dateend=None) if (
                        (data['skom_p'] != None) and (data['skom_p'] != "")) else None
        except Skom.DoesNotExist:
            patient_p.skom_p = None
        try:
            patient_p.stat_p = F008.objects.get(tip_name=str(data['stat_p']).strip(),dateend=None) if (
                        (data['stat_p'] != None) and (data['stat_p'] != "")) else None
        except F008.DoesNotExist:
            patient_p.stat_p = None
        patient_p.s_pol = data['s_pol'] if ((data['s_pol'] != None) and (data['s_pol'] != "")) else None
        patient_p.n_pol = data['n_pol'] if ((data['n_pol'] != None) and (data['n_pol'] != "")) else None

        # patient_p.okatog_p = data['okatog_p']
        # patient_p.okatop_p = data['okatop_p']

    def update_onmk_sp(self, onmk_sp, data):
        onmk_sp.p001 = data['p001']
        onmk_sp.p002 = data['p002']
        onmk_sp.p003 = data['p003']
        onmk_sp.p004 = data['p004']
        onmk_sp.p005_1 = data['p005_1']
        onmk_sp.p005_2 = data['p005_2']
        onmk_sp.p006 = data['p006']
        onmk_sp.p007 = data['p007']
        onmk_sp.p008 = data['p008']
        onmk_sp.p009 = data['p009']
        onmk_sp.p010 = data['p010']
        onmk_sp.p011 = data['p011']
        onmk_sp.p012 = data['p012']
        onmk_sp.p013 = data['p013']
        onmk_sp.p014 = data['p014']
        onmk_sp.p015 = data['p015']
        onmk_sp.p016 = data['p016']

    def update_onmk_li(self, onmk_li, data):
        onmk_li.p001 = data['p001']
        onmk_li.p002 = data['p002']
        onmk_li.p003 = data['p003']
        onmk_li.p004 = data['p004']
        onmk_li.p005 = data['p005']
        onmk_li.p006 = data['p006']
        onmk_li.p007 = data['p007']
        onmk_li.p008 = data['p008']
        onmk_li.p009 = data['p009']
        onmk_li.p010 = data['p010']
        onmk_li.p011 = data['p011']
        onmk_li.p012 = data['p012']
        onmk_li.p013 = data['p013']
        onmk_li.p014 = data['p014']
        onmk_li.p015 = data['p015']
        onmk_li.p016 = data['p016']
        onmk_li.p017 = data['p017']
        onmk_li.p018 = data['p018']
        onmk_li.p019 = data['p019']
        onmk_li.p020 = data['p020']
        onmk_li.p021 = data['p021']
        onmk_li.p022 = data['p022']
        onmk_li.p023 = data['p023']

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

        try:
            onk_sl.mtstz = [m for m in range(len(Onk_sl.MTSTZ_CHOICES)) if Onk_sl.MTSTZ_CHOICES [m][1] == str(data['mtstz']).strip()][0]
        except IndexError:
            onk_sl.mtstz = None

        # onk_sl.mtstz = int(data['mtstz']) if ((data['mtstz'] != None) and (data['mtstz'] != "")) else None

    def update_b_diag(self, b_diag, data):
        try:
            b_diag.diag_date = self.str_form(data['diag_date']) if (
                        (data['diag_date'] != None) and (data['diag_date'] != "")) else None
        except ValidationError:
            b_diag.diag_date = None
        if data['diag_tip'] == 'Гистологический признак':
            b_diag.diag_tip = '1'
        elif data['diag_tip'] == 'Маркёр (ИГХ)':
            b_diag.diag_tip = '2'
        b_diag.diag_code = data['diag_code'] if ((data['diag_code'] != None) and (data['diag_code'] != "")) else None
        b_diag.diag_rslt = data['diag_rslt'] if ((data['diag_rslt'] != None) and (data['diag_rslt'] != "")) else None
        b_diag.rec_rslt = int(data['rec_rslt']) if ((data['rec_rslt'] != None) and (data['rec_rslt'] != "")) else None

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

    def update_napr(self, napr, data):
        try:
            napr.naprdate = self.str_form(data['naprdate']) if (
                        (data['naprdate'] != None) and (data['naprdate'] != "")) else None
        except ValidationError:
            napr.naprdate = None
        try:
            napr.napr_mo = F003.objects.get(naim__icontains=data['napr_mo'],dateend=None) if (
                        (data['napr_mo'] != None) and (data['napr_mo'] != "")) else None
        except F003.DoesNotExist:
            napr.napr_mo = None
        try:
            napr.napr_v = V028.objects.get(n_vn=str(data['napr_v']).strip(),dateend=None) if (
                        (data['napr_v'] != None) and (data['napr_v'] != "")) else None
        except V028.DoesNotExist:
            napr.napr_v = None
        try:
            napr.napr_issl = V029.objects.get(n_met=data['napr_issl'],dateend=None) if (
                        (data['napr_issl'] != None) and (data['napr_issl'] != "")) else None
        except V029.DoesNotExist:
            napr.napr_issl = None
        try:
            napr.napr_usl = V001.objects.get(kod=data['napr_usl'],dateend=None) if (
                        (data['napr_usl'] != None) and (data['napr_usl'] != "")) else None
        except V001.DoesNotExist:
            napr.napr_usl = None

    def str_form(self, st):
        st = str(st)
        if len(st) > 0:
            if len(st) != 8:
                date = "{}-{}-{}".format(st[6:10], st[3:5], st[0:2])
            else:
                date = "{}-{}-{}".format('20'+st[6:10], st[3:5], st[0:2])
            return date
        else:
            return None
