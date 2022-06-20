from hospital.models import (Sluchay, Patient, otde, V020, Le_Vr, Oper,
                             V001, Vra, Oslo, Manpy, Vb_s, Le_trv, Vds, Vb_a,
                             Onmk_sp, Onmk_li, B_diag,Onk_sl,Med_dev)
import datetime


class History:
    def __init__(self, pk):
        self.pk = pk

    def get_History_data(self):
        data = dict()
        sluchay = Sluchay.objects.get(id=self.pk)
        patient = Patient.objects.get(sluchay=sluchay)
        data['err'] = sluchay.err
        data['err_text'] = sluchay.err_text
        data['sl_id'] = sluchay.id
        data['tip_oms'] = sluchay.tip_oms
        # Шапка
        data['history'] = sluchay.nib
        data['fam'] = patient.fam.upper() if patient.fam != None else ''
        data['im'] = patient.im.upper() if patient.im != None else ''
        data['ot'] = patient.ot.upper() if patient.ot != None else ''
        data['pol'] = patient.pol.polname if patient.pol != None else ''
        data['datp'] = self.format_date_m(str(sluchay.datp)) if sluchay.datp != None else ''
        data['tm_otd'] = sluchay.tm_otd if sluchay.tm_otd != None else ''

        data['datv'] = self.format_date_m(
            str(sluchay.datv)) if sluchay.datv != None else ''
        data['datr'] = self.format_date(
            str(patient.datr)) if patient.datr != None else ''
        ###

        # Персональные данные
        data['otd'] = sluchay.otd.naim if sluchay.otd != None else ''
        data['vec'] = patient.vec if patient.vec != '0'  and patient.vec != None and patient.vec != '' else ''
        data['rab'] = patient.rab if patient.rab != None else ''
        data['prof'] = patient.prof if patient.prof != None else ''
        data['r_n'] = patient.r_n.naim if patient.r_n != None else ''
        data['in_t'] = patient.in_t.name if patient.in_t != None else ''
        data['lpy'] = sluchay.lpy.naim if sluchay.lpy != None else ''

        data['npr_num'] = sluchay.npr_num if sluchay.npr_num != None else ''
        data['npr_date'] = self.format_date_m(
            str(sluchay.npr_date)) if sluchay.npr_date != None else ''
        data['alg'] = sluchay.alg_display() if sluchay.alg != None else ''
        data['alg_c'] = Sluchay.ALG_CHOICES
        data['goc'] = sluchay.goc.tip_name if sluchay.goc != None else ''
        data['prpg'] = sluchay.prpg.naim if sluchay.prpg != None else ''
        data['vrez'] = sluchay.vrez.naim if sluchay.vrez != None else ''

        data['p_per'] = sluchay.p_per.naim if sluchay.p_per != None else ''

        ##

        # # Адрес
        data['c_oksm'] = patient.c_oksm.naim if patient.c_oksm != None else 'РОССИЯ'

        # 2.Сведения о диагнозах

        data['dsny'] = {'kod': sluchay.dsny.kod if sluchay.dsny != None else '',
                        'naim': sluchay.dsny.naim[:50] if sluchay.dsny != None else ''}

        data['ds_0'] = {'kod': sluchay.ds_0.kod if sluchay.ds_0 != None else '',
                        'naim': sluchay.ds_0.naim[:50] if sluchay.ds_0 != None else ''}

        data['dsk'] = {'kod': sluchay.dsk.kod if sluchay.dsk != None else '',
                       'naim': sluchay.dsk.naim[:50] if sluchay.dsk != None else ''}

        data['dskz'] = {'kod': sluchay.dskz.kod if sluchay.dskz != None else '',
                        'naim': sluchay.dskz.naim[:50] if sluchay.dskz != None else ''}

        data['dskz2'] = {'kod': sluchay.dskz2.kod if sluchay.dskz2 != None else '',
                        'naim': sluchay.dskz2.naim[:50] if sluchay.dskz2 != None else ''}

        data['ds_osl'] = {'kod': sluchay.ds_osl.kod if sluchay.ds_osl != None else '',
                          'naim': sluchay.ds_osl.naim[:50] if sluchay.ds_osl != None else ''}

        data['dsc'] = {'kod': sluchay.dsc.kod if sluchay.dsc != None else '',
                       'naim': sluchay.dsc.naim[:50] if sluchay.dsc != None else ''}

        data['dson'] = {'kod': sluchay.dson.kod if sluchay.dson != None else '',
                        'naim': sluchay.dson.naim[:50] if sluchay.dson != None else ''}

        data['dat_otd'] = self.format_date_m(
            str(sluchay.dat_otd)) if sluchay.dat_otd != None else ''
        data['tm_otd_d'] = sluchay.tm_otd_1 if sluchay.tm_otd_1 != None else ''
        data['icx'] = sluchay.icx.iz_name + ' ' + \
                      str(sluchay.icx.id_iz) if sluchay.icx != None else ''
        data['rslt'] = sluchay.rslt.tip_name + ' ' + \
                       str(sluchay.rslt.id_tip) if sluchay.rslt != None else ''
        ##

        # 3.Койко-дни

        if sluchay.le_vr != None:
            le_vr_obj = sluchay.le_vr
            le_vr = {}
            # if le_vr_obj.kd != None:
            #     le_vr['N'] = le_vr_obj.kd
            # else:
            #     if (sluchay.datv != None) and (sluchay.datp != None):
            #         if sluchay.datv != sluchay.datp:
            #             le_vr['N'] = str(
            #                 sluchay.datv - sluchay.datp).split(' ')[0]
            #         else:
            #             le_vr['N'] = 0
            #     else:
            #         le_vr['N'] = 0

            if (sluchay.datv != None) and (sluchay.datp != None):
                if sluchay.datv != sluchay.datp:
                    le_vr['N'] = str(
                        sluchay.datv - sluchay.datp).split(' ')[0]
                else:
                    le_vr['N'] = 1

            le_vr['aro'] = le_vr_obj.aro if le_vr_obj.aro != None else ''
            le_vr['otd'] = le_vr_obj.otd if le_vr_obj.otd != None else ''
            le_vr['prof_k'] = le_vr_obj.prof_k.k_prname if le_vr_obj.prof_k != None else ''
            le_vr['kod'] = le_vr_obj.kod.kod if le_vr_obj.kod != None else ''
            le_vr['naim'] = le_vr_obj.kod.naim if le_vr_obj.kod != None else ''
            le_vr['spec'] = le_vr_obj.kod.n_spec if le_vr_obj.kod != None else ''
            le_vr['aro_n'] = le_vr_obj.aro_n if le_vr_obj.aro_n != None else ''
            le_vr['aro_let'] = le_vr_obj.aro_let_display() if le_vr_obj.aro_let_display() != None else ''
            # manpys_d['pl'] = obj.pl_display() if obj.pl_display() != None else ''
            # if le_vr_obj.aro_let != None:
            #     if le_vr_obj.aro_let:
            #         le_vr['aro_let'] = "1.Да"
            #     else:
            #         le_vr['aro_let'] = "2.Нет"
            # else:
            #     le_vr['aro_let'] = ''

            if le_vr_obj.aro_sofa != None:
                if le_vr_obj.aro_sofa:
                    le_vr['aro_sofa'] = "1.Да"
                else:
                    le_vr['aro_sofa'] = "2.Нет"
            else:
                le_vr['aro_sofa'] = ''
        
            if le_vr_obj.aro_ivl != None:
                if le_vr_obj.aro_ivl:
                    le_vr['aro_ivl'] = "1.Да"
                else:
                    le_vr['aro_ivl'] = "2.Нет"
            else:
                le_vr['aro_ivl'] = ''
            data['le_vr'] = le_vr
        else:
            data['le_vr'] = ''

        data['gwf'] = sluchay.gwf if sluchay.gwf != None else ''
        data['u_gwf'] = sluchay.u_gwf if sluchay.u_gwf != None else ''
        data['sofa'] = sluchay.sofa if sluchay.sofa != None else ''
        data['iwl'] = sluchay.iwl if sluchay.iwl != None else ''

        # 4.Операции
        oper_list = []
        if sluchay.oper != None:
            oper = list(map(lambda o: o, sluchay.oper.values('id').order_by('-pop')))
            for o in range(len(oper)):
                oper_d = {}
                obj = Oper.objects.get(id=oper[o]['id'])
                oper_d['dato'] = self.format_date_m(
                    str(obj.dato)) if obj.dato != None else ''
                oper_d['tm_o'] = obj.tm_o if obj.tm_o != None and obj.tm_o != 'None' else ''
                oper_d['py'] = obj.py.kod if obj.py != None else ''
                oper_d['kod_op'] = obj.kod_op.kod if obj.kod_op != None else ''
                if obj.kod_op != None:
                    try:
                        oper_d['kod_op_name'] = V001.objects.values(
                            'naim').filter(kod=obj.kod_op.kod)[0]['naim']
                    except IndexError:
                        oper_d['kod_op_name'] = None
                else:
                    oper_d['kod_op_name'] = None
                oper_d['goc'] = obj.goc.kod if obj.goc != None else ''
                oper_d['kodx'] = obj.kodx.kod if obj.kodx != None else ''
                if obj.kodx != None:
                    try:
                        oper_d['kodx_naim'] = Vra.objects.values(
                            'naim').filter(kod=obj.kodx.kod)[0]['naim']
                    except IndexError:
                        oper_d['kodx_naim'] = None
                else:
                    oper_d['kodx_naim'] = None

                if(len(oper)) == 1:
                    oper_d['pop'] = 'Да'
                else:
                    if obj.pop != None:
                        if obj.pop:
                            oper_d['pop'] = 'Да'
                        else:
                            oper_d['pop'] = 'Нет'
                    else:
                        oper_d['pop'] = 'Неизвестно'

                try:
                    oper_d['pr_osob'] = list(
                        map(lambda p: p[0], obj.pr_osob.values_list('kod')))
                    if len(oper_d['pr_osob']) == 0:
                        oper_d['pr_osob'] = []
                except (AttributeError, IndexError):
                    oper_d['pr_osob'] = []

                oper_d['k_mm'] = obj.k_mm if obj.k_mm != None else ''
                oper_d['kodxa'] = obj.kodxa.kod if obj.kodxa != None else ''
                oper_d['kodxa1'] = obj.kodxa1.kod if obj.kodxa1 != None else ''
                oper_d['obz'] = obj.obz.kod if obj.obz != None else ''
                oper_d['obz_2'] = obj.obz_2.kod if obj.obz_2 != None else ''
                oper_d['kodan'] = obj.kodan.kod if obj.kodan != None else ''

                oper_list.append(oper_d)
            data['oper'] = oper_list
        else:
            data['oper'] = []
        # 4.1 Импланты
        med_dev_list = []
        if sluchay.med_dev != None:
            med_dev = list(map(lambda o: o, sluchay.med_dev.values('id')))
            for m in range(len(med_dev)):
                med_dev_d = {}
                obj = Med_dev.objects.get(id=med_dev[m]['id'])
                # med_dev_d['date'] = self.format_date_m(obj.date) if obj.date != None else ''
                med_dev_d['date'] = self.format_date_m(str(obj.date)) if obj.date != None else ''
                med_dev_d['code'] = obj.code.rzn if obj.code != None else ''
                med_dev_d['number_ser'] = obj.number_ser if obj.number_ser != None else ''
                med_dev_list.append(med_dev_d)
            else:
                data['med_dev'] = med_dev_list
        else:
            data['med_dev'] = []
        # 5.Клинико-стат.гр.заболев-я

        data['ksg_osn'] = sluchay.ksg_osn.code_usl_kz if sluchay.ksg_osn != None else ''
        data['ksg_osn_all'] = sluchay.ksg_osn.ksg if sluchay.ksg_osn != None else ''
        data['ksg_osn_helper'] = ''
        data['ksg_sop'] = sluchay.ksg_sop.code_usl_kz if sluchay.ksg_sop != None else ''
        data['ksg_sop_helper'] = ''
        data['iddoc'] = sluchay.iddokt.kod if sluchay.iddokt != None else ''
        data['oopkk'] = sluchay.oopkk.kod if sluchay.oopkk != None else ''
        data['code_usl'] = sluchay.code_usl.kod if sluchay.code_usl != None else ''
        data['code_usl_name'] = sluchay.code_usl.name if sluchay.code_usl != None else ''
        data['ksg_sop_code_usl'] = sluchay.ksg_osn.code_usl if sluchay.ksg_osn != None else ''
        data['code_usl_vt'] = sluchay.code_usl_vt.kod if sluchay.code_usl_vt != None else ''
        data['code_usl_vt_name'] = sluchay.code_usl_vt.naim if sluchay.code_usl_vt != None else ''
        data['id_metod_hmp'] = sluchay.id_metod_hmp
        data['metod_hmp'] = sluchay.metod_hmp
        data['id_vid_hmp'] = sluchay.id_vid_hmp
        data['vid_hmp'] = sluchay.vid_hmp

        # 6.Oсложнение
        oslo_list = []
        # print(oper)
        for o in range(len(oper)):
            op = Oper.objects.get(id=oper[o]['id'])
            oslo_values = op.oslo.values('id')
            if len(oslo_values) != 0:
                for os in range(len(oslo_values)):
                    oslo_d = {}
                    obj_oslo = Oslo.objects.get(id=oslo_values[os]['id'])
                    oslo_d['inf_oper'] = obj_oslo.inf_oper.kod if obj_oslo.inf_oper != None else ''
                    oslo_d['tnvr'] = obj_oslo.tnvr.kod if obj_oslo.tnvr != None else ''
                    oslo_d['tnvr_fio'] = obj_oslo.tnvr.naim if obj_oslo.tnvr != None else ''
                    oslo_d['dato'] = self.format_date_m(
                        str(obj_oslo.dato)) if obj_oslo.dato != None else ''
                    oslo_d['osl'] = obj_oslo.osl.kod if obj_oslo.osl != None else ''
                    oslo_d['osl_naim'] = obj_oslo.osl.naim if obj_oslo.osl != None else ''
                    oslo_d['xosl'] = obj_oslo.xosl.naim if obj_oslo.xosl != None else ''
                    oslo_d['posl'] = obj_oslo.posl.naim if obj_oslo.posl != None else ''
                    oslo_d['aosl'] = obj_oslo.aosl.naim if obj_oslo.aosl != None else ''
                    oslo_list.append(oslo_d)
           

        if len(oslo_list) != 0:
            data['oslo'] = oslo_list
        else:
            data['oslo'] = []

        # # 7.Трудоспособность
        data['trs'] = sluchay.trs.naim.capitalize(
        ) if sluchay.trs != None else None

        # 8.Манипуляции
        manpys_list = []
        manpys = sluchay.manpy.values('id') if sluchay.manpy != None else ''
        for m in range(len(manpys)):
            obj = Manpy.objects.get(id=manpys[m]['id'])
            manpys_d = {}
            manpys_d['datm'] = self.format_date_m(
                str(obj.datm)) if obj.kodmn != None else ''
            manpys_d['tnvr'] = obj.tnvr.kod if obj.tnvr != None else ''
            manpys_d['tnvr_fam'] = obj.tnvr.naim if obj.tnvr != None else ''
            manpys_d['kodmn'] = obj.kodmn.kod if obj.kodmn != None else ''
            manpys_d['kodmn_naim'] = obj.kodmn.ima if obj.kodmn != None else ''
            manpys_d['kol'] = obj.kol if obj.kol != None else ''
            manpys_d['pl'] = obj.pl_display(
            ) if obj.pl_display() != None else ''

            manpys_list.append(manpys_d)
        if len(manpys_list) > 0:
            data['manipulation'] = manpys_list
        else:
            data['manipulation'] = []

        # 9.Переводы
        if sluchay.vb_s != None:
            try:
                vb_s = Vb_s.objects.get(id=sluchay.vb_s.values('id')[0]['id'])
                data['kod_y'] = vb_s.kod_y.naim if vb_s.kod_y != None else ''
                data['pr_per'] = vb_s.pr_per.naim if vb_s.pr_per != None else ''
                data['dat_pe'] = self.format_date_m(
                    str(vb_s.dat_pe)) if vb_s.dat_pe != None else ''
                data['potd'] = vb_s.potd.naim if vb_s.potd != None else ''
                data['vb_s_datv'] = self.format_date(
                    str(vb_s.datv)) if vb_s.datv != None else ''
            except IndexError:
                data['kod_y'] = ''
                data['pr_per'] = ''
                data['dat_pe'] = ''
                data['potd'] = ''
                data['vb_s_datv'] = ''
        else:
            data['kod_y'] = ''
            data['pr_per'] = ''
            data['dat_pe'] = ''
            data['potd'] = ''
            data['vb_s_datv'] = ''
        # A.Патанатомический Ds
        data['tm_let'] = sluchay.tm_let if sluchay.tm_let != None else ''
        data['pri'] = sluchay.pri.naim if sluchay.pri != None else ''
        data['ds_let'] = {'kod': sluchay.ds_let.kod if sluchay.ds_let != None else '',
                          'naim': sluchay.ds_let.naim if sluchay.ds_let != None else ''}

        data['wskr'] = sluchay.wskr_display(
        ) if sluchay.wskr_display() != None else ''
        data['wskr_date'] = self.format_date_m(
            str(sluchay.wskr_date)) if sluchay.wskr_date != None else ''
        data['wskr_l'] = Sluchay.TIP_WSK_CHOICES
        data['dspat'] = {'kod': sluchay.dspat.kod if sluchay.dspat != None else '',
                         'naim': sluchay.dspat.naim if sluchay.dspat != None else ''}
        data['rasxp'] = sluchay.rasxp_display(
        ) if sluchay.rasxp_display() != None else ''
        data['otd_y'] = sluchay.otd_y.naim if sluchay.otd_y != None else ''

        # # B.Сведения о травмах
        if sluchay.le_trv != None:
            le_trv = sluchay.le_trv

            data['details'] = {'kod': le_trv.details.kod if le_trv.details != None else '',
                               'naim': le_trv.details.naim if le_trv.details != None else ''}
            data['t_trv'] = le_trv.t_trv.naim if le_trv.t_trv != None else ''
            if le_trv.trav_ns == True:
                data['trav_ns'] = "Да"
            elif le_trv.trav_ns == False:
                 data['trav_ns'] = "Нет"

        else:

            data['details'] = {'kod': None, 'naim': None}
            data['t_trv'] = ''
            data['trav_ns'] = ''

        # C.Полис/Документ/Снилс
        if sluchay.vds != None:
            try:
                # Полис
                vds = sluchay.vds
                data['vds'] = vds.vds.naim if vds.vds != None else ''
                data['sctp'] = vds.sctp
                data['nctp'] = vds.nctp
                data['ctkom'] = vds.ctkom.naim if vds.ctkom != None else ''
                data['t_pol'] = vds.t_pol.tip_name if vds.t_pol != None else ''
                # Документ
                data['udl'] = patient.udl.docname if patient.udl != None else ''
                data['s_pasp'] = patient.s_pasp
                data['n_pasp'] = patient.n_pasp
                data['docdate'] = self.format_date(
                    str(patient.docdate)) if patient.docdate != None else ''
                data['docorg'] = patient.docorg if patient.docorg != None else ''
                data['m_roj'] = patient.m_roj if patient.m_roj != None else ''
                # Снилс
                data['ss'] = patient.ss if patient.ss != None else ''
            except IndexError:
                data['vds'] = ''
                data['sctp'] = ''
                data['nctp'] = ''
                data['ctkom'] = ''
                data['t_pol'] = ''

                data['udl'] = ''
                data['s_pasp'] = ''
                data['n_pasp'] = ''
                data['docdate'] = ''
                data['docorg'] = ''
                data['m_roj'] = ''

                data['ss'] = ''
        else:
            data['vds'] = ''
            data['sctp'] = ''
            data['nctp'] = ''
            data['ctkom'] = ''
            data['t_pol'] = ''
            data['udl'] = ''
            data['s_pasp'] = ''
            data['n_pasp'] = ''
            data['docdate'] = ''
            data['docorg'] = ''
            data['m_roj'] = ''
            data['ss'] = ''

        # D.Прерывание беременности

        if sluchay.vb_a != None:
            # data['vb_a_datv'] = self.format_date_m(
            #     str(sluchay.vb_a.datv)) if sluchay.vb_a.datv != None else ''
            data['srber'] = sluchay.vb_a.srber
            data['n_ber'] = sluchay.vb_a.n_ber
            data['pria'] = sluchay.vb_a.pria.naim if sluchay.vb_a.pria != None else ''
            data['m_prer'] = sluchay.vb_a.m_prer.naim if sluchay.vb_a.m_prer != None else ''
        else:
            # data['vb_a_datv'] = ''
            data['srber'] = ''
            data['n_ber'] = ''
            data['pria'] = ''
            data['m_prer'] = ''

        # E.Лист нетрудоспособности
        if sluchay.disability != None:
            data['dat_l1'] = self.format_date_m(
                str(sluchay.disability.dat_l1)) if sluchay.disability.dat_l1 != None else ''
            data['dat_l2'] = self.format_date_m(
                str(sluchay.disability.dat_l2)) if sluchay.disability.dat_l2 != None else ''
            if sluchay.disability.ot_ln == True:
                data['ot_ln'] = "Да"
            elif sluchay.disability.ot_ln == False:
                data['ot_ln'] = "Нет"
            else:
                data['ot_ln'] = ''
            data['vs_bol'] = sluchay.disability.vs_bol
            data['dis_sex_bol'] = sluchay.disability.sex_bol.polname if sluchay.disability.sex_bol != None else ''
        else:
            data['dat_l1'] = ''
            data['dat_l2'] = ''
            data['ot_ln'] = ''
            data['vs_bol'] = ''
            data['dis_sex_bol'] = ''

        # F.Представитель пациента

        if patient.patient_p != None:
            data['fam_p'] = patient.patient_p.fam_p.upper()
            data['im_p'] = patient.patient_p.im_p.upper()
            data['ot_p'] = patient.patient_p.ot_p.upper()
            data['sex_bol'] = patient.patient_p.pol.polname if patient.patient_p.pol != None else ''
            data['datr_p'] = self.format_date(str(patient.patient_p.datr)) if patient.patient_p.datr != None else ''
            data['mp_roj'] = patient.patient_p.m_roj
            data['udl_p'] = patient.patient_p.udl_p.docname if patient.patient_p.udl_p != None else ''
            data['sp_pasp'] = patient.patient_p.sp_pasp
            data['np_pasp'] = patient.patient_p.np_pasp
            data['skom_p'] = patient.patient_p.skom_p.naim if patient.patient_p.skom_p != None else ''
            data['stat_p'] = patient.patient_p.stat_p.tip_name if patient.patient_p.stat_p != None else ''
            data['s_pol'] = patient.patient_p.s_pol
            data['n_pol'] = patient.patient_p.n_pol
            data['okatog_p'] = patient.patient_p.okatog
            data['okatop_p'] = patient.patient_p.okatop
        else:
            data['fam_p'] = ''
            data['im_p'] = ''
            data['ot_p'] = ''
            data['sex_bol'] = ''
            data['datr_p'] = ''
            data['mp_roj'] = ''
            data['udl_p'] = ''
            data['sp_pasp'] = ''
            data['np_pasp'] = ''
            data['skom_p'] = ''
            data['stat_p'] = ''
            data['s_pol'] = ''
            data['n_pol'] = ''

        # # G.Адрес проживания
        data['m_roj'] = patient.m_roj if patient.m_roj != None and patient.m_roj != "" else patient.adr if patient.adr != "" else ''
        data['adr'] = patient.adr if patient.adr != None and patient.adr != "" else ''
        data['kv'] = patient.kv if patient.kv != None and patient.kv != "" else ''
        data['kp'] = patient.kp if patient.kp != None and patient.kp != "" else ''
        data['stro'] = patient.stro if patient.stro != None and patient.stro != "" else ''
        data['cj'] = patient.cj.naim if patient.cj != None else ''

        # data['rai'] = patient.rai_display() if patient.rai != None and patient.rai != '' else ''

        if patient.rai == '1':
            data['rai'] = 'Центральный АО'
        elif patient.rai == '2':
            data['rai'] = 'Ленинский АО'
        elif patient.rai == '3':
            data['rai'] = 'Калининский АО'
        elif patient.rai == '4':
            data['rai'] = 'Восточный АО'
        else:
            data['rai'] = ''

        data['okatog'] = patient.okatog if patient.okatog != None and patient.okatog != "" else ''
        data['okatop'] = patient.okatop if patient.okatop != None and patient.okatop != "" else ''

        # I.Карта больного с ОНМК
        onmk_sp = dict()
        if sluchay.onmk_sp != None:
            onmk_sp['p001'] = sluchay.onmk_sp.p001
            onmk_sp['p002'] = sluchay.onmk_sp.p002
            onmk_sp['p003'] = sluchay.onmk_sp.p003
            onmk_sp['p004'] = sluchay.onmk_sp.p004
            onmk_sp['p005_1'] = sluchay.onmk_sp.p005_1
            onmk_sp['p005_2'] = sluchay.onmk_sp.p005_2
            onmk_sp['p006'] = sluchay.onmk_sp.p006
            onmk_sp['p007'] = sluchay.onmk_sp.p007
            onmk_sp['p008'] = sluchay.onmk_sp.p008
            onmk_sp['p009'] = sluchay.onmk_sp.p009
            onmk_sp['p010'] = sluchay.onmk_sp.p010
            onmk_sp['p011'] = sluchay.onmk_sp.p011
            onmk_sp['p012'] = sluchay.onmk_sp.p012
            onmk_sp['p013'] = sluchay.onmk_sp.p013
            onmk_sp['p014'] = sluchay.onmk_sp.p014
            onmk_sp['p015'] = sluchay.onmk_sp.p015
            onmk_sp['p016'] = sluchay.onmk_sp.p016
        else:
            onmk_sp['p001'] = None
            onmk_sp['p002'] = None
            onmk_sp['p003'] = None
            onmk_sp['p004'] = None
            onmk_sp['p005_1'] = None
            onmk_sp['p005_2'] = None
            onmk_sp['p006'] = None
            onmk_sp['p007'] = None
            onmk_sp['p008'] = None
            onmk_sp['p009'] = None
            onmk_sp['p010'] = None
            onmk_sp['p011'] = None
            onmk_sp['p012'] = None
            onmk_sp['p013'] = None
            onmk_sp['p014'] = None
            onmk_sp['p015'] = None
            onmk_sp['p016'] = None

        onmk_sp['p001_c'] = Onmk_sp.P001_CHOICES
        onmk_sp['p002_c'] = Onmk_sp.P002_CHOICES
        onmk_sp['p003_c'] = Onmk_sp.P003_CHOICES
        onmk_sp['p004_c'] = Onmk_sp.P004_CHOICES
        onmk_sp['p005_1_c'] = Onmk_sp.P005_CHOICES
        onmk_sp['p005_2_c'] = Onmk_sp.P005_2_CHOICES
        onmk_sp['p006_c'] = Onmk_sp.P006_CHOICES
        onmk_sp['p007_c'] = Onmk_sp.P007_CHOICES
        onmk_sp['p008_c'] = Onmk_sp.P008_CHOICES
        onmk_sp['p009_c'] = Onmk_sp.P009_CHOICES
        onmk_sp['p010_c'] = Onmk_sp.P010_CHOICES
        onmk_sp['p011_c'] = Onmk_sp.P011_CHOICES
        onmk_sp['p012_c'] = Onmk_sp.P012_CHOICES
        onmk_sp['p013_c'] = Onmk_sp.P013_CHOICES
        onmk_sp['p014_c'] = Onmk_sp.P014_CHOICES
        onmk_sp['p015_c'] = Onmk_sp.P015_CHOICES
        onmk_sp['p016_c'] = Onmk_sp.P016_CHOICES

        data['onmk_sp'] = onmk_sp
        onmk_li = dict()
        if sluchay.onmk_li != None:
            onmk_li['p001'] = sluchay.onmk_li.p001
            onmk_li['p002'] = sluchay.onmk_li.p002
            onmk_li['p003'] = sluchay.onmk_li.p003
            onmk_li['p004'] = sluchay.onmk_li.p004
            onmk_li['p005'] = sluchay.onmk_li.p005
            onmk_li['p006'] = sluchay.onmk_li.p006
            onmk_li['p007'] = sluchay.onmk_li.p007
            onmk_li['p008'] = sluchay.onmk_li.p008
            onmk_li['p009'] = sluchay.onmk_li.p009
            onmk_li['p010'] = sluchay.onmk_li.p010
            onmk_li['p011'] = sluchay.onmk_li.p011
            onmk_li['p012'] = sluchay.onmk_li.p012
            onmk_li['p013'] = sluchay.onmk_li.p013
            onmk_li['p014'] = sluchay.onmk_li.p014
            onmk_li['p015'] = sluchay.onmk_li.p015
            onmk_li['p016'] = sluchay.onmk_li.p016
            onmk_li['p017'] = sluchay.onmk_li.p017
            onmk_li['p018'] = sluchay.onmk_li.p018
            onmk_li['p019'] = sluchay.onmk_li.p019
            onmk_li['p020'] = sluchay.onmk_li.p020
            onmk_li['p021'] = sluchay.onmk_li.p021
            onmk_li['p022'] = sluchay.onmk_li.p022
            onmk_li['p023'] = sluchay.onmk_li.p023
        else:
            onmk_li['p001'] = None
            onmk_li['p002'] = None
            onmk_li['p003'] = None
            onmk_li['p004'] = None
            onmk_li['p005'] = None
            onmk_li['p006'] = None
            onmk_li['p007'] = None
            onmk_li['p008'] = None
            onmk_li['p009'] = None
            onmk_li['p010'] = None
            onmk_li['p011'] = None
            onmk_li['p012'] = None
            onmk_li['p013'] = None
            onmk_li['p014'] = None
            onmk_li['p015'] = None
            onmk_li['p016'] = None
            onmk_li['p017'] = None
            onmk_li['p018'] = None
            onmk_li['p019'] = None
            onmk_li['p020'] = None
            onmk_li['p021'] = None
            onmk_li['p022'] = None
            onmk_li['p023'] = None

        onmk_li['p001_c'] = Onmk_li.P001_CHOICES
        onmk_li['p002_c'] = Onmk_li.P002_CHOICES
        onmk_li['p003_c'] = Onmk_li.P003_CHOICES
        onmk_li['p004_c'] = Onmk_li.P004_CHOICES
        onmk_li['p005_c'] = Onmk_li.P005_CHOICES
        onmk_li['p006_c'] = Onmk_li.P006_CHOICES
        onmk_li['p007_c'] = Onmk_li.P007_CHOICES
        onmk_li['p008_c'] = Onmk_li.P008_CHOICES
        onmk_li['p009_c'] = Onmk_li.P009_CHOICES
        onmk_li['p010_c'] = Onmk_li.P010_CHOICES
        onmk_li['p011_c'] = Onmk_li.P011_CHOICES
        onmk_li['p012_c'] = Onmk_li.P012_CHOICES
        onmk_li['p013_c'] = Onmk_li.P013_CHOICES
        onmk_li['p014_c'] = Onmk_li.P014_CHOICES
        onmk_li['p015_c'] = Onmk_li.P015_CHOICES
        onmk_li['p016_c'] = Onmk_li.P016_CHOICES
        onmk_li['p017_c'] = Onmk_li.P017_CHOICES
        onmk_li['p018_c'] = Onmk_li.P018_CHOICES
        onmk_li['p019_c'] = Onmk_li.P019_CHOICES
        onmk_li['p020_c'] = Onmk_li.P020_CHOICES
        onmk_li['p021_c'] = Onmk_li.P021_CHOICES
        onmk_li['p022_c'] = Onmk_li.P022_CHOICES
        onmk_li['p023_c'] = Onmk_li.P023_CHOICES

        data['onmk_li'] = onmk_li

        # J.Карта онкобольного
        if sluchay.onk_sl != None:
            data['ds1_t'] = sluchay.onk_sl.ds1_t.reas_name if sluchay.onk_sl.ds1_t != None else ''
            data['stad'] = sluchay.onk_sl.stad.kod_st if sluchay.onk_sl.stad != None else ''
            data['onk_t'] = sluchay.onk_sl.onk_t.kod_t if sluchay.onk_sl.onk_t != None else ''
            data['onk_n'] = sluchay.onk_sl.onk_n.kod_n if sluchay.onk_sl.onk_n != None else ''
            data['onk_m'] = sluchay.onk_sl.onk_m.kod_m if sluchay.onk_sl.onk_m != None else ''
            # data['mtstz'] = sluchay.onk_sl.mtstz
            if sluchay.onk_sl.mtstz == '1':
                data['mtstz'] = 'впервые'
            elif sluchay.onk_sl.mtstz == '2':
                data['mtstz'] = 'ранее'
            else:
                data['mtstz'] = ''
        else:
            data['ds1_t'] = ''
            data['stad'] = ''
            data['onk_t'] = ''
            data['onk_n'] = ''
            data['onk_m'] = ''
            data['mtstz'] = ''
        data['mtstz_list'] = Onk_sl.MTSTZ_CHOICES
        data['c_zab'] = sluchay.c_zab.n_cz if sluchay.c_zab != None else ''

        if sluchay.b_diag != None:
            data['diag_date'] = self.format_date_m(
                str(sluchay.b_diag.diag_date)) if sluchay.b_diag.diag_date != None else ''
            data['diag_tip'] = sluchay.b_diag.diag_tip_display(
            ) if sluchay.b_diag.diag_tip != None else ''
            data['diag_tip_l'] = B_diag.DIAG_TIP_CHOICES
            data['diag_code'] = sluchay.b_diag.diag_code
            data['diag_rslt'] = sluchay.b_diag.diag_rslt
            data['rec_rslt'] = sluchay.b_diag.rec_rslt
        else:
            data['diag_date'] = ''
            data['diag_tip'] = ''
            data['diag_tip_l'] = B_diag.DIAG_TIP_CHOICES
            data['diag_code'] = ''
            data['diag_rslt'] = ''
            data['rec_rslt'] = ''

        if sluchay.cons != None:
            data['pr_cons'] = sluchay.cons.pr_cons.cons_name if sluchay.cons.pr_cons != None else ''
            data['dt_cons'] = self.format_date_m(
                str(sluchay.cons.dt_cons)) if sluchay.cons.dt_cons != None else ''
        else:
            data['pr_cons'] = ''
            data['dt_cons'] = ''

        if sluchay.onk_usl != None:
            data['usl_tip'] = sluchay.onk_usl.usl_tip.tlech_name if sluchay.onk_usl.usl_tip != None else ''
            data['hir_tip'] = sluchay.onk_usl.hir_tip.thir_name if sluchay.onk_usl.hir_tip != None else ''
        else:
            data['usl_tip'] = ''
            data['hir_tip'] = ''

        if sluchay.b_prot != None:
            data['prot'] = sluchay.b_prot.prot.prot_name if sluchay.b_prot.prot != None else ''
            data['d_prot'] = self.format_date_m(
                str(sluchay.b_prot.d_prot)) if sluchay.b_prot.d_prot != None else ''
        else:
            data['prot'] = ''
            data['d_prot'] = ''

        if sluchay.napr != None:
            data['naprdate'] = self.format_date_m(
                str(sluchay.napr.naprdate)) if sluchay.napr.naprdate != None else ''
            data['napr_mo'] = sluchay.napr.napr_mo.naim if sluchay.napr.napr_mo != None else ''
            data['napr_v'] = sluchay.napr.napr_v.n_vn if sluchay.napr.napr_v != None else ''
            data['napr_issl'] = sluchay.napr.napr_issl.n_met if sluchay.napr.napr_issl != None else ''
            data['napr_usl'] = sluchay.napr.napr_usl.kod if sluchay.napr.napr_usl != None else ''
        else:
            data['naprdate'] = ''
            data['napr_mo'] = ''
            data['napr_v'] = ''
            data['napr_issl'] = ''
            data['napr_usl'] = ''

        # K.Мо прикрепления
        data['pmg'] = sluchay.pmg.naim if sluchay.pmg != None else ''

        return data

    def format_date(self, date):
        if date != 'None':
            try:
                y, m, d = date.split('-')
                date = '{}-{}-{}'.format(d, m, y)
                return date
            except:
                return None
        return None
    
    def format_date_m(self, date):
        if date != 'None':
            try:
                y, m, d = date.split('-')
                date = '{}-{}-{}'.format(d, m, y[2:])
                return date
            except:
                return None
        return None


