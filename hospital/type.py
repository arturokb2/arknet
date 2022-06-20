from graphene_django import DjangoObjectType
from okb2.models import (V005,otde,Rab_Ner,T004,F003,Vrzb,Oksm,Ds,V012,V009,V020,Vra,V021,
                         PR_OSOB,V001,T006,Ab_Obsh,Pope,Prli,Trv,Isfin,Skom,F008,F011,N018,
                         N002,N003,N004,N005,N007,N010,N008,
                         N011,N019,N013,N014,N001,V028,V029,V014,Prpg,PER,PR_PER,Tip_pb,Met_pb,V027,
                         Trvnas,V002,anesthesia,V018_bpoms,V019_bpoms,V018_sboms,V019_sboms,Tar_vt,group_kc_dkk,
                         Age_group,group_kc_group,Code_med_dev,T003,V036)
# from www.hospital import models
from graphene import Int



class V005Type(DjangoObjectType):
    class Meta:
        model = V005
        fields = ('id','polname',)

class OtdeType(DjangoObjectType):
    class Meta:
        model = otde
        fields = ('id','naim','kod')

class Rab_nerType(DjangoObjectType):
    class Meta:
        model = Rab_Ner
        fields = ('id','naim',)

class T004Type(DjangoObjectType):
    class Meta:
        model = T004
        fields = ('id','name',)

class F003Type(DjangoObjectType):
    class Meta:
        model = F003
        fields = ('id','naim',)

class VrzbType(DjangoObjectType):
    class Meta:
        model = Vrzb
        fields = ('id','naim',)

class OksmType(DjangoObjectType):
    class Meta:
        model = Oksm
        fields = ('id','naim',)

class DsType(DjangoObjectType):
    class Meta:
        model = Ds
        fields = ('id','kod','naim')

class V012Type(DjangoObjectType):
    class Meta:
        model = V012
        fields = ('id','iz_name','id_iz')


class V009Type(DjangoObjectType):
    class Meta:
        model = V009
        fields = ('id','tip_name','id_tip')

class V020Type(DjangoObjectType):
    class Meta:
        model = V020
        fields = ('id','k_prname',)

class VraType(DjangoObjectType):
    class Meta:
        model = Vra
        fields = ('id','kod','naim','v021','kod_spec','v002','n_spec')

class V021Type(DjangoObjectType):
    class Meta:
        model = V021
        fields = ('id','specname',)

class PR_OSOBType(DjangoObjectType):
    class Meta:
        model = PR_OSOB
        fields = ('id','kod','naim')

class V001Type(DjangoObjectType):
    class Meta:
        model = V001
        fields = ('id','kod','naim')

class T006Type(DjangoObjectType):
    class Meta:
        model = T006
        fields = ('id','code_usl_kz','ksg','code_usl','title')

class T003Type(DjangoObjectType):
    class Meta:
        model = T003
        fields = ('id','kod','name','code_usl_kz')

class Ab_ObshType(DjangoObjectType):
    class Meta:
        model = Ab_Obsh
        fields = ('id','kod','ima')

class PopeType(DjangoObjectType):
    class Meta:
        model = Pope
        fields = ('id','kod','naim')

class PrliType(DjangoObjectType):
    class Meta:
        model = Prli
        fields = ('id','naim','kod')

class TrvType(DjangoObjectType):
    class Meta:
        model = Trv
        fields = ('id','naim',)

class IsfinType(DjangoObjectType):
    class Meta:
        model = Isfin
        fields = ('id','naim',)

class SkomType(DjangoObjectType):
    class Meta:
        model = Skom
        fields = ('id','naim',)

class F008Type(DjangoObjectType):
    class Meta:
        model = F008
        fields = ('id','tip_name',)

class F011Type(DjangoObjectType):
    class Meta:
        model = F011
        fields = ('id','docname','id_doc')

class N018Type(DjangoObjectType):
    class Meta:
        model = N018
        fields = ('id','reas_name',)

class N002Type(DjangoObjectType):
    class Meta:
        model = N002
        fields = ('id','kod_st',)

class N003Type(DjangoObjectType):
    class Meta:
        model = N003
        fields = ('id','kod_t',)

class N004Type(DjangoObjectType):
    class Meta:
        model = N004
        fields = ('id','kod_n',)

class N005Type(DjangoObjectType):
    class Meta:
        model = N005
        fields = ('id','kod_m',)

class N007Type(DjangoObjectType):
    class Meta:
        model = N007
        fields = ('id','mrf_name',)

class N010Type(DjangoObjectType):
    class Meta:
        model = N010
        fields = ('id','kod_igh','igh_name')


class N008Type(DjangoObjectType):
    class Meta:
        model = N008
        fields = ('id','r_m_name',)

class N011Type(DjangoObjectType):
    class Meta:
        model = N011
        fields = ('id','r_i_name',)

class N019Type(DjangoObjectType):
    class Meta:
        model = N019
        fields = ('id','cons_name',)

class N013Type(DjangoObjectType):
    class Meta:
        model = N013
        fields = ('id','tlech_name',)

class N014Type(DjangoObjectType):
    class Meta:
        model = N014
        fields = ('id','thir_name',)

class N001Type(DjangoObjectType):
    class Meta:
        model = N001
        fields = ('id','prot_name',)

class V028Type(DjangoObjectType):
    class Meta:
        model = V028
        fields = ('id','n_vn',)

class V029Type(DjangoObjectType):
    class Meta:
        model = V029
        fields = ('id','n_met',)

class V014Type(DjangoObjectType):
    class Meta:
        model = V014
        fields = ('id','tip_name',)

class PrpgType(DjangoObjectType):
    class Meta:
        model = Prpg
        fields = ('id','naim',)

class PERType(DjangoObjectType):
    class Meta:
        model = PER
        fields = ('id','naim',)

class PR_PERType(DjangoObjectType):
    class Meta:
        model = PR_PER
        fields = ('id','naim',)

class Tip_pbType(DjangoObjectType):
    class Meta:
        model = Tip_pb
        fields = ('id','naim',)

class Met_pbType(DjangoObjectType):
    class Meta:
        model = Met_pb
        fields = ('id','naim',)

class V027Type(DjangoObjectType):
    class Meta:
        model = V027
        fields = ('id','n_cz',)


class TrvnasType(DjangoObjectType):
    class Meta:
        model = Trvnas
        fields = ('id','naim',)

class V002Type(DjangoObjectType):
    class Meta:
        model = V002
        fields = ('id','id_pr',)


class anesthesiaType(DjangoObjectType):
    class Meta:
        model = anesthesia
        fields = ('id','kod',)

class V018_bpomsType(DjangoObjectType):
    class Meta:
        model = V018_bpoms
        fields = ('id','idhvid',)

class V019_bpomsType(DjangoObjectType):
    class Meta:
        model = V019_bpoms
        fields = ('id','hvid',)


# class V018_sbomsType(DjangoObjectType):
#     class Meta:
#         model = V018_sboms
#         fields = ('hvid',)

class V019_sbomsType(DjangoObjectType):
    class Meta:
        model = V019_sboms
        fields = ('id','idhvid',)


class Tar_vtType(DjangoObjectType):
    class Meta:
        model = Tar_vt
        fields = ('id','kod','naim','kod_stat','metod')



# class T006Type(DjangoObjectType):
#     class Meta:
#         model = T006
#         fields = ('ksg','code_usl','title')

class group_kc_dkkType(DjangoObjectType):
    class Meta:
        model = group_kc_dkk
        fields = ('id','kod',)

class Age_groupType(DjangoObjectType):
    class Meta:
        model = Age_group
        fields = ('id','name',)



class group_kc_groupType(DjangoObjectType):
    class Meta:
        model = group_kc_group
        fields = ('id','code_usl_kz','ksg','ikk')

class Code_med_dev_groupType(DjangoObjectType):
    class Meta:
        model = Code_med_dev
        fields = ('kod_id','rzn','name',)

class V036_groupType(DjangoObjectType):
    class Meta:
        model = V036
        fields = ('s_code',)


