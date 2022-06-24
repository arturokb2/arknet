
from  openpyxl.styles import Font,Alignment,Border,Side

import hospital.models
from services.hospital.patient import Patients
from okb2.models import *
from datetime import datetime
import time
class Reports(Patients):
    def __init__(self,user,request):
        super().__init__(user, request)
    def filter(self,*args,**kwargs):
        filters,sluchays = args
        f = []
        # print(filters)
        # print(sluchays)
        for sluchay in sluchays:
            f_ = True
            if filters.get('datv',None) != None:
                datv_1,datv_2 = filters.get('datv').values()
                if datv_1 != '' and datv_2 != '':
                    datv_1 = datetime.strptime(datv_1, '%Y-%m-%d').date()
                    datv_2 = datetime.strptime(datv_2,'%Y-%m-%d').date()
                    f_ = datv_1 >= sluchay['sluchay'].datv <= datv_2
                    if f_ == False : continue
            if filters.get('datp',None) != None:
                datp_1,datp_2 = filters.get('datp').values()
                if datp_1 != '' and datp_2 != '':
                    datp_1 = datetime.strptime(datp_1, '%Y-%m-%d').date()
                    datp_2 = datetime.strptime(datp_2,'%Y-%m-%d').date()
                    f_ = datp_1 >= sluchay['sluchay'].datp <= datp_2
                    if f_ == False: continue
            if filters.get('otd', None) != None:
                if filters.get('otd')['otd'] != '':
                    f_ =  sluchay['sluchay'].otd.naim == filters.get('otd')['otd'] if sluchay['sluchay'].otd != None else False
                    if f_ == False: continue
            if filters.get('prof', None) != None:
                if sluchay['le_vr'] != None :
                    if filters.get('prof')['prof'] != '':
                        f_ = sluchay['le_vr'].prof_k.k_prname == filters.get('prof')['prof'] if sluchay['le_vr'].prof_k != None else False
                        if f_ == False: continue
            if filters.get('fam', None) != None:
                if filters.get('fam')['fam'] != '':
                    f_ = sluchay['patient'].fam == filters.get('fam')['fam']
                    if f_ == False: continue
            if filters.get('im', None) != None:
                if filters.get('im')['im'] != '':
                    f_ = sluchay['patient'].im == filters.get('im')['im']
                    if f_ == False: continue
            if filters.get('ot', None) != None:
                if filters.get('ot')['ot'] != '':
                    f_ = sluchay['patient'].ot == filters.get('ot')['ot']
                    if f_ == False: continue
            if filters.get('pol', None) != None:
                if filters.get('pol')['pol'] != '':
                    f_ = sluchay['patient'].pol.polname == filters.get('pol')['pol'] if sluchay['patient'].pol != None else False
                    if f_ == False: continue
            if filters.get('type_lgots',None) != None:
                pass
            if filters.get('in_t', None) != None:
                if filters.get('in_t')['in_t'] != '':
                    f_ = sluchay['patient'].in_t.name == filters.get('in_t')['in_t'] if sluchay['patient'].in_t != None else False
                    if f_ == False: continue
            if filters.get('r_n', None) != None:
                if filters.get('r_n')['r_n'] != '':
                    f_ = sluchay['patient'].r_n.naim == filters.get('r_n')['r_n'] if sluchay['patient'].r_n != None else False
                    if f_ == False: continue
            if filters.get('age_group',None) != None:
                if filters.get('age_group')['age_group'] != '':
                    age_group = Age_group.objects.get(name=filters.get('age_group')['age_group'])
                    f_ = self._age_group(sluchay['patient'].vs,
                                        sluchay['patient'].nvs,
                                        sluchay['patient'].datr,
                                        age_group)
                    if f_ == False: continue
            if filters.get('goc', None) != None:
                if filters.get('goc')['goc'] != '':
                    f_ = sluchay['sluchay'].goc.tip_name == filters.get('goc')['goc'] if sluchay['sluchay'].goc != None else False
                    if f_ == False: continue
            if filters.get('prpg', None) != None:
                if filters.get('prpg')['prpg'] != '':
                    f_ = sluchay['sluchay'].prpg.naim == filters.get('prpg')['prpg'] if sluchay['sluchay'].prpg != None else False
                    if f_ == False: continue
            if filters.get('vrez', None) != None:
                if filters.get('vrez')['vrez'] != '':
                    f_ = sluchay['sluchay'].vrez.naim == filters.get('vrez')['vrez'] if sluchay['sluchay'].vrez != None else False
                    if f_ == False: continue
            if filters.get('dskz',None) != None:
                dskz_1,dskz_2 = filters.get('dskz').values()
                if dskz_1 != '' and dskz_2 != '':
                    f_ = dskz_1 >= sluchay['sluchay'].dskz.naim <= dskz_2 if sluchay['sluchay'].dskz != None else False
                    if f_ == False: continue
            if filters.get('dsc', None) != None:
                if filters.get('dsc')['dsc'] != '':
                    dsc = filters.get('dsc')['dsc']
                    f_ = sluchay['sluchay'].dsc.naim == dsc if sluchay['sluchay'].dsc != None else False
                    if f_ == False: continue
            if filters.get('dspat', None) != None:
                if filters.get('dspat')['dspat'] != '':
                    dspat = filters.get('dspat')['dspat']
                    f_ = sluchay['sluchay'].dspat.naim == dspat if sluchay['sluchay'].dspat != None else False
                    if f_ == False: continue
            if filters.get('dson', None) != None:
                if filters.get('dson')['dson'] != '':
                    dson = filters.get('dson')['dson']
                    f_ = sluchay['sluchay'].dson.naim == dson if sluchay['sluchay'].dson != None else False
                    if f_ == False: continue
            if filters.get('c_oksm', None) != None:
                if filters.get('c_oksm')['c_oksm'] != '':
                    f_ = sluchay['patient'].c_oksm.naim == filters.get('c_oksm')['c_oksm'] if sluchay['patient'].c_oksm != None else False
                    if f_ == False: continue
            if filters.get('terr',None) != None:
                if filters.get('terr')['terr'] != '':
                    terr = filters.get('terr')['terr']
                    f_ = self._get_terr(sluchay['patient'].adr,
                                       terr)
                    if f_ == False: continue
            if filters.get('reg',None) != None:
                if filters.get('reg')['reg'] != '':
                    reg = filters.get('reg')['reg']
                    f_ = reg in sluchay['patient'].adr
                    if f_ == False: continue
            if filters.get('rai_in',None) != None:
                if filters.get('rai_in')['rai_in'] != '':
                    rai_in = filters.get('rai_in')['rai_in']
                    f_ = rai_in in sluchay['patient'].rai_display() if sluchay['patient'].rai != None else False
                    if f_ == False: continue
            if filters.get('cj',None) != None:
                if filters.get('cj')['cj'] != '':
                    f_ = sluchay['patient'].cj.naim == filters.get('cj')['cj'].lower() if sluchay['patient'].cj != None else False
                    if f_ == False: continue
            if filters.get('lpy',None) != None:
                if filters.get('lpy')['lpy'] != '':
                    f_ = sluchay['sluchay'].lpy.naim == filters.get('lpy')['lpy'] if sluchay['sluchay'].lpy !=  None else False
                    if f_ == False: continue

            if filters.get('vds',None) != None:
                if sluchay['vds'] != None :
                    if filters.get('vds')['vds'] != '':
                        f_ = sluchay['vds'].vds.naim == filters.get('vds')['vds'] if sluchay['vds'].vds != None else False
                    if f_ == False: continue

            # if filters.get('ctkom',None) != None:
            #     if sluchay['vds'] != None :
            #         if filters.get('ctkom')['ctkom'] != '':
            #             f_ = sluchay['vds'].ctkom.naim == filters.get('ctkom')['ctkom'] if sluchay['vds'].ctkom != None else False
            #         if f_ == False: continue
            
            if filters.get('icx',None) != None:
                if filters.get('icx')['icx'] != '':
                    f_ = sluchay['sluchay'].icx.iz_name == filters.get('icx')['icx'] if sluchay['sluchay'].icx != None else False
                    if f_ == False: continue
            if filters.get('otdel_let',None) != None:
                if filters.get('otdel_let')['otdel_let'] != '':
                    f_ =  sluchay['sluchay'].otd.naim == filters.get('otdel_let')['otdel_let'] if sluchay['sluchay'].otd != None else False
                    if f_ == False: continue
            if filters.get('kod_vra',None) != None:
                if sluchay['le_vr'] != None:
                    if filters.get('kod_vra')['vra'] != '':
                        kod_vra = filters.get('kod_vra')['vra']
                        f_ = sluchay['le_vr'].kod.kod == kod_vra if sluchay['le_vr'].kod != None else False
                        if f_ == False: continue
            if filters.get('kod_op',None) != None:
                if sluchay['oper'] != None:
                    if filters.get('kod_op')['kod_op'] != '':
                        for oper in sluchay['oper']:
                            f_ = oper.kod_op.kod == filters.get('kod_op')['kod_op'] if oper.kod_op != None else False
                        if f_ == False: continue
            if filters.get('pr_osob',None) != None:
                if sluchay['oper'] != None:
                    if filters.get('pr_osob')['pr_osob'] != '':
                        pr_osob = PR_OSOB.objects.get(naim=filters.get('pr_osob')['pr_osob'])
                        for oper in sluchay['oper']:
                            f_ = pr_osob.id in [i['id'] for i in oper.pr_osob.values('id')]
                        if f_ == False: continue
            if filters.get('t_trv',None) != None:
                if sluchay['le_trv'] != None :
                    if filters.get('t_trv')['t_trv'] != '':
                        if filters.get('t_trv')['t_trv'] != '':
                            f_ = sluchay['le_trv'].t_trv.naim == filters.get('t_trv')['t_trv'] if sluchay['le_trv'].t_trv != None else False
                            if f_ == False: continue
            if filters.get('trav_ns',None) != None:
                if sluchay['le_trv'] != None:
                    if filters.get('trav_ns')['trav_ns'] != '':
                        f_ = sluchay['le_trv'].trav_ns.naim == filters.get('trav_ns')['trav_ns'] if sluchay['le_trv'].trav_ns != None else False
                        if f_ == False: continue
            if filters.get('disability',None) != None:
                if sluchay['disability'] != None:
                    if sluchay['disability'].dat_l1 != None and sluchay['disability'].dat_l2 != None:
                        f_ = True
                    else:
                        f_ = False
                    if f_ == False: continue
            if filters.get('srber',None) != None:
                if sluchay['disability'] != None:
                    num_1,num_2 = filters.get('srber').values()
                    if num_1 != '' and num_2 != '':
                            f_ = num_1 <= sluchay['disability'].srber <= num_2 if sluchay['disability'].srber != None\
                                                                                  and sluchay['disability'].srber != 0 else False
                    if f_ == False: continue
            if filters.get('potd',None) != None:
                if sluchay['vb_s'] != None:
                    if filters.get('potd')['potd'] != '':
                        f_ = sluchay['vb_s'][0].potd.naim == filters.get('potd')['potd'] if sluchay['vb_s'][0].potd != None else False
                    if f_ == False: continue
            if filters.get('kod_y',None) != None:
                if sluchay['vb_s'] != None:
                    if filters.get('kod_y')['kod_y'] != '':
                        f_ = sluchay['vb_s'][0].kod_y.naim == filters.get('kod_y')['kod_y'] if sluchay['vb_s'][0].kod_y != None else False
                    if f_ == False: continue
            if filters.get('dskz_prich',None) != None:
                if filters.get('dskz_prich')['dskz_prich'] != None:
                    f_ = sluchay['sluchay'].dskz.naim == filters.get('dskz_prich')['dskz_prich'] if sluchay['sluchay'].dskz != None else False
                    if f_ == False: continue
            if filters.get('pr_per',None) != None:
                if sluchay['vb_s'] != None:
                    if filters.get('pr_per')['pr_per'] != None:
                        f_ = sluchay['vb_s'][0].pr_per.naim == filters.get('pr_per')['pr_per'] if sluchay['vb_s'][0].pr_per != None else False
                        if f_ == False: continue
            if filters.get('time_minuts_po',None) != None:
                if filters.get('time_minuts_po')['time_minuts_po'] != '':
                    time_minuts_po = filters.get('time_minuts_po')['time_minuts_po']
                    if sluchay['sluchay'].tm_otd != None and sluchay['sluchay'].tm_otd_1 != None:
                        tm_otd = time.strptime(sluchay['sluchay'].tm_otd,'%H:%M')
                        tm_otd_1 = time.strptime(sluchay['sluchay'].tm_otd_1, '%H:%M')
                        f_ = (tm_otd_1.tm_min - tm_otd.tm_min) == int(time_minuts_po)
                    if f_ == False: continue
            
            if  filters.get('abobsh_list',None)!= None:
                abobsh = filters.get('abobsh_list')
                if abobsh['abobsh'] != '':
                    if sluchay['manpy'] != None:
                       for manpy in sluchay['manpy']:
                            f_ = abobsh['abobsh'] == manpy.kodmn.kod if manpy.kodmn != None else False
                    if f_ == False: continue
            if filters.get('kod_vra_man',None) != None:
                vra = filters.get('kod_vra_man')
                if vra['vra'] != '':
                    for manpy in sluchay['manpy']:
                        f_ = vra['vra'] == manpy.tnvr.kod if manpy.tnvr != None else False

                if f_ == False: continue

            if f_ != False:
                f.append(sluchay)

            # print(f)

        return f
    def _age_group(self,*args):
        vs,nvs,datr,age_group = args
        if age_group.name == 'до 1 года':
            return  nvs in ['Д','М']
        elif age_group.name == '1 - до 7 лет':
            return  nvs == 'Л' and (1<=vs<=7)
        elif age_group.name == '7 - 14 лет':
            return  nvs == 'Л' and (7<=vs<=14)
        elif age_group.name == 'подростки 15 лет':
            return  nvs == 'Л' and (vs==15)
        elif age_group.name == '18 - 19 лет':
            return  nvs == 'Л' and (18<=vs<=19)
        elif age_group.name == '20 - 29 лет':
            return  nvs == 'Л' and (20<=vs<=29)
        elif age_group.name == '30 - 39 лет':
            return  nvs == 'Л' and (30<=vs<=39)
        elif age_group.name == '40 - 49 лет':
            return  nvs == 'Л' and (40<=vs<=49)
        elif age_group.name == '50 - 59 лет':
            return  nvs == 'Л' and (50<=vs<=59)
        elif age_group.name == '60 - 69 лет':
            return  nvs == 'Л' and (60<=vs<=69)
        elif age_group.name == '70 - 79 лет':
            return  nvs == 'Л' and (70<=vs<=79)
        elif age_group.name == '80 и старше лет':
            return  nvs == 'Л' and (80<=vs)
        elif age_group.name == 'от 0 до 17 лет':
            return  nvs == 'Л' and (0<=vs<=17)
        elif age_group.name == 'старше 60 и старше':
            return  nvs == 'Л' and (60<=vs)
        elif age_group.name == '70 лет и старше':
            return  nvs == 'Л' and (70<=vs)
        elif age_group.name == 'до 65 лет':
            return  nvs == 'Л' and (65>=vs)
        elif age_group.name == '18 - 59 лет':
            return  nvs == 'Л' and (18<=vs<=59)
        elif age_group.name == '1968 - 1983 г.':
            return  nvs == 'Л' and (1968<=datr.year<=1983)
        elif age_group.name == '30 - 50 лет':
            return  nvs == 'Л' and (30<=vs<=50)
        elif age_group.name == 'трудоспособные':
            return  nvs == 'Л' and ((18<=vs<=55) or (18<=vs<=60))
        elif age_group.name == 'нетрудоспособные':
            return  nvs == 'Л' and ((18<=vs<=56) or (18<=vs<=61))
        elif age_group.name == 'до 50 лет':
            return  nvs == 'Л' and (50>=vs)
        elif age_group.name == '15 - 16 лет':
            return  nvs == 'Л' and (15<=vs<=16)
        elif age_group.name == 'с 18 по 50 лет':
            return  nvs == 'Л' and (18<=vs<=50)
        elif age_group.name == '55 лет и старше':
            return  nvs == 'Л' and (55<=vs)
        elif age_group.name == 'от 40 до 55 лет':
            return  nvs == 'Л' and (40<=vs<=55)
        elif age_group.name == 'с 17 по 26 лет':
            return  nvs == 'Л' and (17<=vs<=26)
        elif age_group.name == 'с 10 до 14 лет':
            return  nvs == 'Л' and (10<=vs<=14)
        elif age_group.name == '18 лет и старше':
            return  nvs == 'Л' and (18<=vs)
        elif age_group.name == 'с 18 до 27 лет':
            return  nvs == 'Л' and (18<=vs<=27)
        elif age_group.name == 'от 40 до 60 лет':
            return  nvs == 'Л' and (40<=vs<=60)
    def _get_terr(self,*args):
        adr, terr = args
        if terr == 'г.Тюменю':
            return 'Тюмень' in adr
        elif terr == 'Юг Тюм.обл.кроме Тюм.р-н':
            return (('Тюменская обл' in adr) or ('обл. Тюменская' in adr) or ('ОБЛ ТЮМЕНСКАЯ' in adr))\
                   and (('Тюменский р-н' not in adr) or ('р-н. Тюменский' not in adr))
        elif terr == 'Тюменский р-н':
            return 'Тюменский р-н' in adr or 'р-н. Тюменский' in adr
        elif terr == 'Ханты-Мансйский АО':
            return 'Ханты-Мансийский' in adr
        elif terr == 'Ямало-Немецкий АО':
            return 'Ямало-Ненецкий' in adr
        elif terr == 'Др.регионы Россий':
            return (('Тюменская обл' not in adr) and ('обл. Тюменская' not in adr) and ('ОБЛ ТЮМЕНСКАЯ' not in adr))\
                   and (('Тюменский р-н' not in adr) and ('р-н. Тюменский' not in adr))
   
    def filetr_sluchays(self,filters,sluchays,sluchays_old=None):
        rez = []
        if len(filters) > 0:
            if sluchays_old != None:
                sluchays = sluchays_old.copy()
            else:
                sluchays = sluchays
            
            for slych in sluchays:
                temp = []
                for filter in filters:
                    if filter == 'otd':
                        temp.append(slych['sluchay'].otd.naim if slych['sluchay'].otd != None else '')
                    if filter == 'count_sluchay':
                        temp.append(1 if slych['sluchay'] != None else 0)
                    elif filter == 'manpy':
                        temp.append(len(slych['manpy']) if slych['manpy'] != None else 0)
                    elif filter == 'goc_ek':
                        temp.append(1 if slych['sluchay'].goc != None and slych['sluchay'].goc.tip_name == 'Экстренная' else 0)
                    elif filter == 'goc_pl':
                        temp.append(1 if slych['sluchay'].goc != None and slych['sluchay'].goc.tip_name == 'Плановая' else 0)
                    elif filter == 'adr_not_tum_obl_rn':
                        temp.append(1 if slych['patient'].adr != '' and ((('Тюменская обл' not in slych['patient'].adr) and (
                            'обл. Тюменская' not in slych['patient'].adr) and ('ОБЛ ТЮМЕНСКАЯ' not in slych['patient'].adr)) \
                            and (('Тюменский р-н' not in slych['patient'].adr) and ('р-н. Тюменский' not in slych['patient'].adr))) else 0)
                    elif filter == 'adr_tumen':
                        temp.append(1 if slych['patient'].adr != '' and 'Тюмень' in slych['patient'].adr else 0)
                    elif filter == 'adr_tum_obl_rn':
                        temp.append(1 if slych['patient'].adr != '' and ((('Тюменская обл' in slych['patient'].adr) or (
                            'обл. Тюменская' in slych['patient'].adr) or ('ОБЛ ТЮМЕНСКАЯ' in slych['patient'].adr)) \
                            and (('Тюменский р-н' not in slych['patient'].adr) or ('р-н. Тюменский' not in slych['patient'].adr))) else 0)
                    elif filter == 'adr_tumen_rn':
                        temp.append(1 if slych['patient'].adr != '' and 'Тюменский р-н' in slych[
                                    'patient'].adr or 'р-н. Тюменский' in slych['patient'].adr else 0)
                    elif filter == 'adr_hm':
                        temp.append(1 if slych['patient'].adr != '' and 'Ханты-Мансийский' in slych['patient'].adr else 0)
                    elif filter == 'adr_im':
                        temp.append(1 if slych['patient'].adr != '' and 'Ямало-Ненецкий' in slych['patient'].adr else 0)
                    elif filter == 'not_obl_rn_tum':
                        temp.append(1 if slych['patient'].adr != '' and ((('Тюменская обл' not in slych['patient'].adr) and (
                                    'обл. Тюменская' not in slych['patient'].adr) and ('ОБЛ ТЮМЕНСКАЯ' not in slych['patient'].adr)) \
                                    and (('Тюменский р-н' not in slych['patient'].adr) and ('р-н. Тюменский' not in slych['patient'].adr))) else 0)
                    elif filter == 'oksm_not_643':
                        temp.append(1 if slych['patient'].c_oksm != None and slych['patient'].c_oksm.kod != 643 else 0)
                    elif filter == 'prof_k':
                        temp.append(slych['le_vr'].prof_k.k_prname if slych['le_vr'].prof_k != None else '')
                    elif filter == 'prof_k_n':
                        temp.append(slych['le_vr'].otd if slych['le_vr'].otd != None and slych['le_vr'].otd != '' else 0)
                        if slych['le_vr'].otd != '' and slych['le_vr'].otd != None:
                            print(slych['le_vr'].otd)
                    elif filter == 'rez_umer':
                        temp.append(1 if (slych['sluchay'].rslt != None and slych['sluchay'].rslt.id_tip == 105) or (slych['sluchay'].rslt != None and slych['sluchay'].rslt.id_tip == 106) else 0)
                        # if slych['sluchay'].rslt != None:
                        #     pass
                            # print(slych['sluchay'].rslt)
                            # print(slych['sluchay'].nib)
                    elif filter == 'rez_umer_goc_ek':
                        temp.append(1 if ((slych['sluchay'].rslt!= None and slych['sluchay'].rslt.id_tip == 105) or (slych['sluchay'].rslt != None and slych['sluchay'].rslt.id_tip == 106)) and \
                             (slych['sluchay'].goc != None and slych['sluchay'].goc.tip_name == 'Экстренная') else 0)
                    elif filter == 'count_oper':
                        temp.append(1 if slych['sluchay'].oper != None else 0)
                    elif filter == 'count_oper_all':
                        temp.append(slych['sluchay'].oper.count() if slych['sluchay'].oper != None else 0)
                    elif filter == 'goc_ek_oper':
                        temp.append(1 if (slych['sluchay'].goc != None and slych['sluchay'].goc.tip_name == 'Экстренная') and (slych['sluchay'].oper != None) else 0 )

                    elif filter == 'rez_umer_goc_ek_sr':
                        temp.append(slych['le_vr'].kd if ((slych['le_vr'] != None) and (slych['sluchay'].rslt != None and slych['sluchay'].rslt.id_tip == 105) or (slych['sluchay'].rslt != None and slych['sluchay'].rslt.id_tip == 106)) and \
                                         (slych['sluchay'].goc != None and slych['sluchay'].goc.tip_name == 'Экстренная') else 0)

                rez.append(temp)
        return rez





class Specification:
    def is_satisfied(self,item):
        pass

    # def __and__(self, other):
    #     return AndSpecification(self, other)

    def __xor__(self, other):
        return AndSpecificationList(self,other)

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))

class AndSpecificationList(Specification):
    def __init__(self,*args):
        self.args = args
    def is_satisfied(self,item):
        return list(map(lambda spec: spec.is_satisfied(item), self.args))

class OtdSpecification(Specification):
    # otd
    def __init__(self,otd=None):
        self.otd = otd
    def is_satisfied(self,item):
        if self.otd is not None:
            return  item.sluchay.otd is not None and item.sluchay.otd.naim == self.otd
        return item.sluchay.otd.naim if item.sluchay.otd is not None else ''

class ProfkSpecification(Specification):
#prof_k
    def __init__(self,prof_k=None):
        self.prof_k = prof_k
    def is_satisfied(self,item):
        if self.prof_k is not None:
            return item.le_vr.prof_k is not None and item.le_vr.prof_k.k_prname == self.prof_k
        return item.le_vr.prof_k.k_prname if item.le_vr != None and item.le_vr.prof_k is not None else ''

class CountSluchaySpecification(Specification):
#count_sluchay
    def is_satisfied(self,item):
        return 1 if item.sluchay is not None else 0

class CountSluchayPlanSpecification(Specification):
    def is_satisfied(self,item):
        return 1 if item.sluchay.goc != None and item.sluchay.goc.tip_name == 'Плановая' else 0


class ProfKNSpecification(Specification):
#prof_k_n
    def is_satisfied(self,item):
        return item.le_vr.kd if item.le_vr is not None and item.le_vr.kd is not '' else 0

class GocEkSpecification(Specification):
#goc_ek
    def is_satisfied(self,item):
        return 1 if item.sluchay.goc is not None and item.sluchay.goc.tip_name == 'Экстренная' else 0

class GocEkNSpecification(Specification):
#goc_ek_n
    def is_satisfied(self,item):
        return item.le_vr.kd if item.le_vr is not None  and item.sluchay.goc is not None and item.sluchay.goc.tip_name == 'Экстренная' else 0

class RezUmerSpecification(Specification):
#rez_umer
    def is_satisfied(self,item):
        return 1 if item.sluchay.rslt is not None and item.sluchay.rslt.id_tip in [105,106] else 0
        
class RezUmerOperSpecification(Specification):
    def is_satisfied(self, item):
        if  item.sluchay.oper.count() > 0:
            return 1 if item.sluchay.rslt is not None and item.sluchay.rslt.id_tip in [105,106] else 0
        return 0

class RezUmerOperKDSpecification(Specification):
    def is_satisfied(self, item):
        if  item.sluchay.oper.count() > 0:
            return item.le_vr.kd if item.sluchay.rslt is not None and item.sluchay.rslt.id_tip in [105,106] else 0
        return 0

class RezUmerKdSpecification(Specification):
#rez_umer_kd
    def is_satisfied(self,item):
        return item.le_vr.kd if item.le_vr is not None and item.sluchay.rslt is not None and item.sluchay.rslt.id_tip in [105,106] else 0

class RezUmerGocEkSpecification(Specification):
#rez_umer_goc_ek
    def is_satisfied(self,item):
        return 1 if item.sluchay.rslt is not None and item.sluchay.goc is not None\
                    and item.sluchay.rslt.id_tip in [105,106] and item.sluchay.goc.tip_name == 'Экстренная' else 0

class RezUmerGocEkSrSpecification(Specification):
#rez_umer_goc_ek_sr
    def is_satisfied(self,item):
        return  item.le_vr.kd if item.le_vr is not None and item.sluchay.rslt is not None and item.sluchay.goc is not None\
                and item.sluchay.rslt.id_tip in [105,106] and item.sluchay.goc.tip_name == 'Экстренная' else 0


class RezUmerDetSpecification(Specification):
#rez_umer_det
    def is_satisfied(self,item):
        return 1 if item.sluchay.rslt is not None and item.sluchay.rslt.id_tip in [105,106] and \
            item.patient.nvs in ['М','Д'] else 0

class RezUmerKdDetSpecification(Specification):
#rez_umer_kd_det
    def is_satisfied(self,item):
        return item.le_vr.kd if item.le_vr is not None and item.sluchay.rslt is not None and \
                                item.sluchay.rslt.id_tip in [105,106] and item.patient.nvs in ['М','Д'] else 0

class OperCountSpecification(Specification):
#oper_count
    def is_satisfied(self,item):
        return 1 if item.sluchay.oper.count() != 0  else 0

class OperCountGocEkSpecification(Specification):
    def is_satisfied(self,item):
        return 1 if item.sluchay.oper.count() != 0 and  item.sluchay.goc is not None\
                    and item.sluchay.goc.tip_name == 'Экстренная' else 0

class OperAllCountSpecification(Specification):
#oper_all_count
    def is_satisfied(self,item):
        return item.sluchay.oper.count()

class OperAllCountGocEkSpecification(Specification):
    def is_satisfied(self,item):
        return item.sluchay.oper.count() if item.sluchay.oper.count() != 0 and item.sluchay.goc is not None\
                    and item.sluchay.goc.tip_name == 'Экстренная' else 0

class OperAllKdSpecification(Specification):
#oper_all_kd
    def is_satisfied(self,item):
        return item.le_vr.kd if item.le_vr is not None and item.sluchay.oper.count() != 0 else 0

class PredOperKdSpecification(Specification):
    def is_satisfied(self,item):
        if item.sluchay.oper.count() != 0 and item.sluchay.goc != None and item.sluchay.goc.tip_name == 'Плановая':
            oper = item.sluchay.oper.filter(pop=True)
            if oper.count() > 0:
                day = (oper[0].dato - item.sluchay.datp).days if oper[0].dato != None else 0
                return day
            return 0
        return 0

class PredOperKdAllSpecification(Specification):
    def is_satisfied(self,item):
        if item.sluchay.oper.count() != 0:
            oper = item.sluchay.oper.filter(pop=True)
            if oper.count() > 0:
                day = (oper[0].dato - item.sluchay.datp).days if oper[0].dato != None else 0
                return day
            return 0
        return 0

class PredOperSpecification(Specification):
    def is_satisfied(self,item):
        if item.sluchay.oper.count() != 0 and item.sluchay.goc != None and item.sluchay.goc.tip_name == 'Плановая':
            oper = item.sluchay.oper.filter(pop=True)
            if oper.count() > 0:
                o = (oper[0].dato - item.sluchay.datp).days if oper[0].dato != None else 0
                return 1 if o != 0 else 0
                # if o != 0:
                #     return 1
            return 0
        return 0

class EndosOper(Specification):
    def is_satisfied(self,item):
        return  item.sluchay.oper.filter(pr_osob__in=[23]).count()

class PoslOperKdSpecification(Specification):
#oper_posl
    def is_satisfied(self,item):
        if item.sluchay.oper.count() != 0:
            oper = item.sluchay.oper.filter(pop=True)
            if oper.count() > 0:
                day = (item.sluchay.datv - oper[0].dato).days if oper[0].dato != None else 0
                return day
            return 0
        return 0
            


class OsloCountAllSpecification(Specification):
    def is_satisfied(self,item):
        # if item.sluchay.oper.count() > 0:
        #     oslos = item.sluchay.oper.exclude(oslo=None)
        #     if oslos.count() > 0:
        #         return oslos.count()
        #     return 0
        # return 0
        if item.sluchay.oslo.count() > 0:
            return item.sluchay.oslo.count()
        return 0

class AgeSpecification(Specification):
    def is_satisfied(self, item):
        return datetime.now().year-item.patient.datr.year

class NibSpecification(Specification):
    def is_satisfied(self, item):
        print(item.sluchay.nib)
        return item.sluchay.nib

# class DSTSpecification(Specification):
#     def __init__(self,typ=None,ds=None,r=None):
#         self.typ = typ
#         self.ds = ds
#         self.r = r
#     def is_satisfied(self, item):
#         per = item.patient
#         dskz = item.sluchay.dskz.kod if item.sluchay.dskz else None
#         ds_osl = item.sluchay.ds_osl.kod if item.sluchay.ds_osl else None
#         rslt = item.sluchay.rslt.id_tip if  item.sluchay.rslt else None

#         ds_list_T51 = ['T51','T51.0','T51.1','T51.2','T51.3','T51.4','T51.5','T51.6','T51.7','T51.8','T51.9']
#         ds_list_T40 = ['T40','T40.0','T40.1','T40.2','T40.3','T40.4','T40.5','T40.6','T40.7','T40.8','T40.9']
#         ds_list_T40_6 = ['T40.6']
#         ds_list_T43 = ['T43','T43.0','T43.1','T43.2','T43.3','T43.4','T43.5','T43.6','T43.7','T43.8','T43.9']
#         ds_list_T39 = ['T39','T39.0','T39.1','T39.2','T39.3','T39.4','T39.5','T39.6','T39.7','T39.8','T39.9']
#         not_ds = ds_list_T51+ds_list_T40+ds_list_T40_6+ds_list_T43+ds_list_T39

#         ds_list = []
#         if self.ds == 'T51':
#             ds_list = ds_list_T51
#         elif self.ds == 'T40':
#             ds_list = ds_list_T40
#         elif self.ds == 'T40.6':
#             ds_list = ds_list_T40_6
#         elif self.ds == 'T43':
#             ds_list = ds_list_T43
#         elif self.ds == 'T39':
#             ds_list = ds_list_T39
#         else:
#             ds_list = not_ds



#         if self.typ == 'all':
#             if self.r == 'g':
#                 if self.ds != None:
#                     if self.ds in ds_list:
#                         return 1 if 'р-н' not in per.m_roj else 0
                    
#             elif self.r == 't':
#                 return 1 if 'р-н' in per.m_roj else 0

#         elif self.typ == 'zhe':
#             if self.r == 'g':
#                 if per.pol and per.pol.id_pol == 2:
#                     return 1 if 'р-н' not in per.m_roj else 0
#                 return 0
#             elif self.r == 't':
#                 if per.pol and per.pol.id_pol == 2:
#                     return 1 if 'р-н' in per.m_roj else 0
#                 return 0

class IsfinKastSpecification(Specification):
    def __init__(self,typ=None,p=None):
        self.typ = typ
        self.p = p
    def is_satisfied(self, item):
        vds = item.sluchay.vds
        le_vr = item.sluchay.le_vr
        oper = item.sluchay.oper
        if self.p == None:
            if self.typ == 'all':
                return 1
            elif self.typ == 'kd':
                return item.le_vr.kd
            elif self.typ == 'oper':
                return 1 if oper.count() > 0 else 0
            elif self.typ == 'oper_count':
                return oper.count()
            elif self.typ == 'ymer':
                return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
        elif self.p == 'tym_oms':
            if vds.vds and vds.vds.kod == '1':
                if vds.ctkom and vds.ctkom.naim.find('ТЮМ') != -1:
                    if self.typ == 'all':
                        return 1
                    elif self.typ == 'kd':
                        return item.le_vr.kd
                    elif self.typ == 'oper':
                        return 1 if oper.count() > 0 else 0
                    elif self.typ == 'oper_count':
                        return oper.count()
                    elif self.typ == 'ymer':
                        return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
                return 0
            return 0
        elif self.p == 'bez_polis':
            if vds.ctkom and vds.ctkom.naim.find('БЕЗ') != -1:
                if self.typ == 'all':
                    return 1
                elif self.typ == 'kd':
                    return item.le_vr.kd
                elif self.typ == 'oper':
                    return 1 if oper.count() > 0 else 0
                elif self.typ == 'oper_count':
                    return oper.count()
                elif self.typ == 'ymer':
                    return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
            return 0
        elif self.p == 'dr_oms':
            if vds.vds and vds.vds.kod == '1':
                if vds.ctkom and vds.ctkom.naim.find('ТЮМ') == -1:
                    if self.typ == 'all':
                        return 1
                    elif self.typ == 'kd':
                        return item.le_vr.kd
                    elif self.typ == 'oper':
                        return 1 if oper.count() > 0 else 0
                    elif self.typ == 'oper_count':
                        return oper.count()
                    elif self.typ == 'ymer':
                        return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
                return 0
            return 0
        elif self.p == 'vmp_sb':
            if vds.vds and vds.vds.kod == 'Д':
                if self.typ == 'all':
                    return 1
                elif self.typ == 'kd':
                    return item.le_vr.kd
                elif self.typ == 'oper':
                    return 1 if oper.count() > 0 else 0
                elif self.typ == 'oper_count':
                    return oper.count()
                elif self.typ == 'ymer':
                    return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
            return 0
        elif self.p == 'vmp_sv':
            if vds.vds and vds.vds.kod == '5':
                if self.typ == 'all':
                    return 1
                elif self.typ == 'kd':
                    return item.le_vr.kd
                elif self.typ == 'oper':
                    return 1 if oper.count() > 0 else 0
                elif self.typ == 'oper_count':
                    return oper.count()
                elif self.typ == 'ymer':
                    return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
            return 0
        elif self.p == 'dms':
            if vds.vds and vds.vds.kod == '2':
                if self.typ == 'all':
                    return 1
                elif self.typ == 'kd':
                    return item.le_vr.kd
                elif self.typ == 'oper':
                    return 1 if oper.count() > 0 else 0
                elif self.typ == 'oper_count':
                    return oper.count()
                elif self.typ == 'ymer':
                    return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
            return 0
        elif self.p == 'fss':
            if vds.vds and vds.vds.kod == '6':
                if self.typ == 'all':
                    return 1
                elif self.typ == 'kd':
                    return item.le_vr.kd
                elif self.typ == 'oper':
                    return 1 if oper.count() > 0 else 0
                elif self.typ == 'oper_count':
                    return oper.count()
                elif self.typ == 'ymer':
                    return 1 if item.sluchay.rslt and  item.sluchay.rslt.id_tip in [105,106] else 0
            return 0


            # elif self.p == 'kd':
            #     return item.le_vr.kd
            # elif self.p == 'oper':
            #     return 1 if oper.count() > 0 else 0
            # elif self.p == 'oper_count':
            #     return oper.count()
        # if self.typ == 'tym_oms':
        #     if item.sluchay.vds:
        #         vds = item.sluchay.vds
        #         if vds.vds.kod == '1'  :
        #             if vds.ctkom and vds.ctkom.naim.find('ТЮМ') != -1:
        #                 if self.p == None:
        #                     return 1

        #             return 0
        #         return 0
        #     return 0
        # elif self.typ == 'bez_oms'





class Filter:
    def filter(self,items,spec):
        pass


class BetterFilter(Filter):
    def filter(self,items,spec):
        yield spec.is_satisfied(items)
    def format_list(self,data):
        data = str(data)
        data = data.replace('[', '')
        data = data.replace(']', '')
        data = data.split(',')
        return [d.replace("'","").strip() for d in data]


