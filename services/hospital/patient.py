import os

import time

from hospital.models import *
from okb2.models import MyUser
from datetime import datetime
from django.conf import settings
from django import db
# from django_thread import Thread
# from threading import RLock,Lock

import multiprocessing
from django.core.cache import cache
from itertools import zip_longest
import copy
class Patients:
    def __init__(self,user,request):
        self._user = MyUser.objects.get(user=user)
        self._request = request
        self._date_1 = datetime.strptime(self._request.get('date_1'),'%Y-%m-%d').date()
        self._date_2 = datetime.strptime(self._request.get('date_2'), '%Y-%m-%d').date()


    def _path(self):
        if not os.path.isdir(settings.MEDIA_ROOT + '/temp/' + f'{str(self._user.id)}/'):
            os.mkdir(settings.MEDIA_ROOT + '/temp/' + f'{str(self._user.id)}/')
        self._dir = settings.MEDIA_ROOT + '/temp/' + f'{str(self._user.id)}/'

    @staticmethod
    def func_chunk_itertools(lst):
        i_ = iter(lst)
        return list(zip_longest(i_, i_, i_, i_, i_, i_, i_, i_, i_, i_))

    def get_sluchays(self):
        # sluchay_list = Sluchay.objects.values('id').filter(datp__gte=self._date_1,
        #                                                    datv__lte=self._date_2,
        #                                                    statistics_type=self._user.statistics_type)
        # sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self._date_1,self._date_2),statistics_type=self._user.statistics_type)

        # sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self._date_1, self._date_2),
        #                                                    statistics_type=self._user.statistics_type)

        if self._user.statistics_type.id == 2:
            # sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self._date_1, self._date_2),nib__istartswith='0201').exclude(update_user=None)
            sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self._date_1, self._date_2),otd__tipe=1).exclude(update_user=None)
        else:
            sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self._date_1, self._date_2),otd__tipe=2).exclude(update_user=None)

        self.patients = []
        # threads = []
        # chunk = self.func_chunk_itertools(sluchay_list)
        for s in sluchay_list:
            self._get_data(s['id'])

        # for sluch in sluchay_list:
        #     t = Thread(target=self._get_data,args=(sluch['id'],))
        #     threads.append(t)
        #     t.start()
        # for t in threads:
        #     t.join()
        # else:
        #     # db.close_old_connections()
        #     return self._patients

    #     for c in chunk:
    #         t = Thread(target=self.chunk_threads, args=(c,))
    #         threads.append(t)
    #         t.start()
    #     for t in threads:
    #         t.join()
    #
    #
    # def chunk_threads(self,sluchay_list):
    #     for sluch in sluchay_list:
    #         if sluch:
    #             try:
    #                 self._get_data(sluch['id'])
    #             except:
    #                 pass

    def _get_data(self,id):
        sluchay = Sluchay.objects.get(id=id)
        patient = Sluchay.objects.get(id=sluchay.id).patient.all()[0]
        patient_p = patient.patient_p
        vb_s = list(Sluchay.objects.get(id=sluchay.id).vb_s.all())
        vb_a = sluchay.vb_a
        vds = sluchay.vds
        le_vr = sluchay.le_vr
        le_trv = sluchay.le_trv
        oper = list(Sluchay.objects.get(id=sluchay.id).oper.all())
        oslo = list([Oper.objects.get(id=o.id).oslo.all() for o in oper][0]) if len(oper) > 0 else None
        manpy = list(Sluchay.objects.get(id=sluchay.id).manpy.all())
        disability = sluchay.disability
        napr = sluchay.napr
        cons = sluchay.cons if sluchay.cons != None else None
        onk_sl = sluchay.onk_sl if sluchay.onk_sl != None else None
        b_diag = sluchay.b_diag if sluchay.b_diag != None else None
        b_prot = sluchay.b_prot if sluchay.b_prot != None else None
        onk_usl = sluchay.onk_usl if sluchay.onk_usl != None else None
        ksg_kpg = list(Sluchay.objects.get(id=sluchay.id).ksg_kpg.all())

        temp_d = dict()
        temp_d['patient'] = patient
        temp_d['patient_p'] = patient_p
        temp_d['sluchay'] = sluchay
        temp_d['vb_s'] = vb_s if len(vb_s) > 0 else None
        temp_d['vb_a'] = vb_a
        temp_d['vds'] = vds
        temp_d['le_vr'] = le_vr
        temp_d['le_trv'] = le_trv
        temp_d['oper'] = oper if len(oper) > 0 else None
        temp_d['oslo'] = oslo
        temp_d['manpy'] = manpy if len(manpy) > 0 else None
        temp_d['disability'] = disability
        temp_d['napr'] = napr
        temp_d['cons'] = cons
        temp_d['onk_sl'] = onk_sl
        temp_d['b_diag'] = b_diag
        temp_d['b_prot'] = b_prot
        temp_d['onk_usl'] = onk_usl
        temp_d['ksg_kpg'] = ksg_kpg if len(ksg_kpg) > 0 else None
        self.patients.append(temp_d)






class PatientsData:
    def __init__(self,date_1,date_2,user):
        self.date_1 = date_1
        self.date_2 = date_2
        self.user = user
        self.patients = []
        # self.locker = Lock()
    @staticmethod
    def func_chunk_itertools(lst):
        i_ = iter(lst)
        return list(zip_longest(i_, i_, i_, i_,i_, i_, i_, i_,i_, i_))

    def sluchays(self,cah=False):
        if cah:
            self.patients = copy.deepcopy(cache.get('hospital_data'))
            return None

        else:
            if self.user.statistics_type.id == 2:
                sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self.date_1, self.date_2),otd__tipe=1).exclude(update_user=None)
            else:
                sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self.date_1, self.date_2),otd__tipe=2).exclude(update_user=None)

        # sluchay_list = Sluchay.objects.values('id').filter(datv__range=(self.date_1, self.date_2))

        # chunk = self.func_chunk_itertools(sluchay_list)
        # threads = []
        #
        # for c in chunk:
        #     t = Thread(target=self.chunk_threads, args=(c,))
        #     threads.append(t)
        #     t.start()
        # for t in threads:
        #     t.join()

        for s in sluchay_list:
            self.get_data(s['id'])

        cache.set('hospital_data', self.patients, timeout=60 * 660)



    # def chunk_threads(self,sluchay_list):
    #     for sluch in sluchay_list:
    #         if sluch:
    #             try:
    #                 self.get_data(sluch['id'])
    #             except:
    #                 pass


    def get_data(self,id):
        # self.locker.acquire()
        try:
            sluchay = Sluchay.objects.get(id=id)
            patient = Sluchay.objects.get(id=sluchay.id).patient.all()[0]
            patient_p = patient.patient_p
            vb_s = list(Sluchay.objects.get(id=sluchay.id).vb_s.all())
            vb_a = sluchay.vb_a
            vds = sluchay.vds
            le_vr = sluchay.le_vr
            le_trv = sluchay.le_trv
            oper = list(Sluchay.objects.get(id=sluchay.id).oper.all())
            oslo = list([Oper.objects.get(id=o.id).oslo.all() for o in oper][0]) if len(oper) > 0 else None
            manpy = list(Sluchay.objects.get(id=sluchay.id).manpy.all())
            disability = sluchay.disability
            napr = sluchay.napr
            cons = sluchay.cons if sluchay.cons != None else None
            onk_sl = sluchay.onk_sl if sluchay.onk_sl != None else None
            b_diag = sluchay.b_diag if sluchay.b_diag != None else None
            b_prot = sluchay.b_prot if sluchay.b_prot != None else None
            onk_usl = sluchay.onk_usl if sluchay.onk_usl != None else None
            ksg_kpg = list(Sluchay.objects.get(id=sluchay.id).ksg_kpg.all())
            med_dev = list(Sluchay.objects.get(id=sluchay.id).med_dev.all())

            # med_dev = list(Sluchay.objects.get(i))med_dev
            self.patients.append(
                PatientMedDevBuilder().set_patient(patient)\
                                      .set_patient_p(patient_p)\
                                      .set_sluchay(sluchay)\
                                      .set_vb_s(vb_s if len(vb_s) > 0 else None)\
                                      .set_vb_a(vb_a)\
                                      .set_vds(vds)\
                                      .set_le_vr(le_vr)\
                                      .set_le_trv(le_trv)\
                                      .set_oper(oper if len(oper) > 0 else None)\
                                      .set_oslo(oslo)\
                                      .set_manpy(manpy if len(manpy) > 0 else None)\
                                      .set_disability(disability)\
                                      .set_napr(napr)\
                                      .set_cons(cons)\
                                      .set_onk_sl(onk_sl)\
                                      .set_b_diag(b_diag)\
                                      .set_b_prot(b_prot)\
                                      .set_onk_usl(onk_usl)\
                                      .set_ksg_kpg(ksg_kpg)\
                                      .set_med_dev(med_dev)\
                                      .build()
            )
        finally:
            pass
            # self.locker.release()

class PatientData:
    def __init__(self):
        self.patient = None
        self.patient_p = None
        self.sluchay = None
        self.vb_s = None
        self.vb_a = None
        self.vds = None
        self.le_vr = None
        self.le_trv = None
        self.oper = None
        self.oslo = None
        self.manpy = None
        self.disability = None
        self.napr = None
        self.cons = None
        self.onk_sl = None
        self.b_diag = None
        self.b_prot = None
        self.onk_usl = None
        self.ksg_kpg = None
        self.med_dev = None

    @staticmethod
    def new():
        return PatientBuilder()

class PatientBuilder:
    def __init__(self):
        self.patient = PatientData()

    def build(self):
        return self.patient

class PatientPatientBuilder(PatientBuilder):
    def set_patient(self,patient):
        self.patient.patient = patient
        return self

class PatientPatientPBuilder(PatientPatientBuilder):
    def set_patient_p(self,patient_p):
        self.patient.patient_p = patient_p
        return self

class PatientSluchayBuilder(PatientPatientPBuilder):
    def set_sluchay(self,sluchay):
        self.patient.sluchay = sluchay
        return self

class PatientVbSBuilder(PatientSluchayBuilder):
    def set_vb_s(self,vb_s):
        self.patient.vb_s = vb_s
        return self

class PatientVbABuilder(PatientVbSBuilder):
    def set_vb_a(self,vb_a):
        self.patient.vb_a = vb_a
        return self

class PatientVdsBuilder(PatientVbABuilder):
    def set_vds(self,vds):
        self.patient.vds = vds
        return self

class PatientLeVrBuilder(PatientVdsBuilder):
    def set_le_vr(self,le_vr):
        self.patient.le_vr = le_vr
        return self

class PatientLeTrvBuilder(PatientLeVrBuilder):
    def set_le_trv(self,le_trv):
        self.patient.le_trv = le_trv
        return self

class PatientOperBuilder(PatientLeTrvBuilder):
    def set_oper(self,oper):
        self.patient.oper = oper
        return self

class PatientOsloBuilder(PatientOperBuilder):
    def set_oslo(self,oslo):
        self.patient.oslo = oslo
        return self

class PatientManpyBuilder(PatientOsloBuilder):
    def set_manpy(self,manpy):
        self.patient.manpy = manpy
        return self

class PatientDisabilityBuilder(PatientManpyBuilder):
    def set_disability(self,disability):
        self.patient.disability = disability
        return self

class PatientNaprBuilder(PatientDisabilityBuilder):
    def set_napr(self,napr):
        self.patient.napr = napr
        return self

class PatientConsBuilder(PatientNaprBuilder):
    def set_cons(self,cons):
        self.patient.cons = cons
        return self

class PatientOnkSlBuilder(PatientConsBuilder):
    def set_onk_sl(self,onk_sl):
        self.patient.onk_sl = onk_sl
        return self

class PatientBDiagBuilder(PatientOnkSlBuilder):
    def set_b_diag(self,b_diag):
        self.patient.b_diag = b_diag
        return self

class PatientBProtBuilder(PatientBDiagBuilder):
    def set_b_prot(self,b_prot):
        self.patient.b_prot = b_prot
        return self

class PatientOnkUsl(PatientBProtBuilder):
    def set_onk_usl(self,onk_usl):
        self.patient.onk_usl = onk_usl
        return self

class PatientKsgKpgBuilder(PatientOnkUsl):
    def set_ksg_kpg(self,ksg_kpg):
        self.patient.ksg_kpg = ksg_kpg
        return self

class PatientMedDevBuilder(PatientKsgKpgBuilder):
    def set_med_dev(self,med_dev):
        self.patient.med_dev = med_dev
        return self

