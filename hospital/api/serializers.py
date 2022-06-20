from pyexpat import model
from hospital.models import Sluchay,Patient,Le_Vr,Oper
from okb2.models import (Ds,V012,V009,V005,Rab_Ner,Oksm, Vra,otde,
                         F003,V014,Prpg,Vrzb,PER,T004,V021,V020,V001,
                         anesthesia,PR_OSOB)
from rest_framework import serializers

class SearchPatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['fam','im','ot','datr']



class SearchHistorySerializers(serializers.ModelSerializer):
    patient = SearchPatientSerializers(many=True)
    class Meta:
        model = Sluchay
        fields = ['id','nib','datp','patient']

class DcSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ds
        fields = ['id','kod','naim',]

class V012Serializers(serializers.ModelSerializer):
    class Meta:
        model = V012
        fields = ['id','iz_name','id_iz']

class V009Serializers(serializers.ModelSerializer):
    class Meta:
        model = V009
        fields = ['id','tip_name','id_tip']

class V005Serializers(serializers.ModelSerializer):
    class Meta:
        model = V005
        fields = ['id','polname']

class Rab_NerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rab_Ner
        fields = ['id','naim']

class OksmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oksm
        fields = ['id','naim']

class otdeSerializers(serializers.ModelSerializer):
    class Meta:
        model = otde
        fields = ['id','naim']

class profkSerializers(serializers.ModelSerializer):
    class Meta:
        model = V020
        fields = ['id','k_prname']


class F003Serializers(serializers.ModelSerializer):
    class Meta:
        model = F003
        fields = ['id','naim']

class V014Serializers(serializers.ModelSerializer):
    class Meta:
        model = V014
        fields = ['id','tip_name']

class PrpgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prpg
        fields = ['id','naim']

class VrezSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vrzb
        fields = ['id','naim']

class PERSerializers(serializers.ModelSerializer):
    class Meta:
        model = PER
        fields = ['id','naim']

class T004Serializers(serializers.ModelSerializer):
    class Meta:
        model = T004
        fields = ['id','name']

class VraNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vra
        fields = ['id','naim']

class VrakodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vra
        fields = ['id','kod']

class V020Serializers(serializers.ModelSerializer):
    class Meta:
        model = V020
        fields = ['id','k_prname']


class V001Serializers(serializers.ModelSerializer):
    class Meta:
        model = V001
        fields = ['id','naim']

class anesthesiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = anesthesia
        fields = ['id','kod']

class PR_OSOBSerializers(serializers.ModelSerializer):
    class Meta:
        model = PR_OSOB
        fields = ['id','kod']


class Le_VrSerializers(serializers.ModelSerializer):
    prof_k = V020Serializers(read_only=True)
    kod = VraNameSerializers(read_only=True)
    class Meta:
        model = Le_Vr
        fields = ['id','kd','aro','prof_k','kod','spec',
                  'aro_n','aro_let','aro_sofa','aro_ivl']




class OperSerializers(serializers.ModelSerializer):
    kod_op = V001Serializers(read_only=True)
    kodx = VraNameSerializers(read_only=True)
    pr_osob = PR_OSOBSerializers(many=True)
    kodxa = VrakodSerializers(read_only=True)
    kodxa1 = VrakodSerializers(read_only=True)
    obz = anesthesiaSerializers(read_only=True)
    obz_2 = anesthesiaSerializers(read_only=True)
    kodan = VrakodSerializers(read_only=True)

    class Meta:
        model = Oper
        fields = ['id','dato','tm_o','py','kod_op','goc','kodx',
                  'pop','pr_osob','k_mm','kodxa','kodxa1','obz','obz_2','kodan']


class PatientSerializers(serializers.ModelSerializer):
    pol = V005Serializers(read_only=True)
    r_n = Rab_NerSerializers(read_only=True)
    c_oksm = OksmSerializers(read_only=True)
    in_t = T004Serializers(read_only=True)
    class Meta:
        model = Patient
        fields = ['id','fam','im','ot','pol','datr','vec','m_roj','adr','rab',
                  'prof','r_n','in_t','c_oksm'
                  ]

class HistorySerializers(serializers.ModelSerializer):
    patient = PatientSerializers(many=True)
    otd = otdeSerializers(read_only=True)
    lpy = F003Serializers(read_only=True)
    alg_name = serializers.CharField(source='alg_display')
    goc = V014Serializers(read_only=True)
    prpg = PrpgSerializers(read_only=True)
    vrez = VrezSerializers(read_only=True)
    p_per = PERSerializers(read_only=True)

    dsny = DcSerializers(read_only=True)
    ds_0 = DcSerializers(read_only=True)
    dsk = DcSerializers(read_only=True)
    ds_osl = DcSerializers(read_only=True)
    dsc = DcSerializers(read_only=True)
    dson = DcSerializers(read_only=True)
    icx = V012Serializers(read_only=True)
    rslt = V009Serializers(read_only=True)

    le_vr = Le_VrSerializers(read_only=True)
    oper = OperSerializers(many=True)

    class Meta:
        model = Sluchay
        fields = [
                  'id','nib','otd','datp','tm_otd','datv','otd','lpy','npr_num',
                  'npr_date','alg','alg_name','goc','prpg','vrez','p_per',
                  'dsny','ds_0','dsk','ds_osl','dsc','dson',
                  'dat_otd','tm_otd_1','icx','rslt',
                  #
                  'patient',
                  'le_vr',
                  'oper'
        ]


class PatientUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['fam','im','ot','pol','datr']

class SluchayUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sluchay
        fields = ['datp','tm_otd','datv']




# class Form7Serializers(serializers.ModelSerializer):
#     otd = otdeSerializers(read_only=True)
#     prof_k = profkSerializers(many=True)
#     class Meta:
#         model = Form_7
#         fields = '__all__'

