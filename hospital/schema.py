import graphene
from django.db.models import Max
from  .type import *
# request == info.context
from okb2.models import (V005, otde, Rab_Ner, T004, F003, Vrzb, Oksm, Ds,V012,V009,V020,Vra,V021,
                         PR_OSOB,V001,T006,MyUser,Ab_Obsh,Pope,Prli,Trv,Isfin,Skom,F008,F011,N018,
                         N002,N003,N004,N005,N007,N010,N008,
                         N011, N019, N013, N014, N001, V028, V029, V014, Prpg, PER, PR_PER, Tip_pb, Met_pb, V027,
                         Trvnas, V002, anesthesia,Tar_vt, group_kc_dkk,
                         Age_group,Code_med_dev,T003)

from django.db.models import Q
from django.db.models import Count
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.conf import settings


class Query(graphene.ObjectType):
    V005 = graphene.List(V005Type)
    Otde = graphene.List(OtdeType)
    Rab_ner = graphene.List(Rab_nerType)
    T004 = graphene.List(T004Type)
    F003 = graphene.List(F003Type)
    Vrzb = graphene.List(VrzbType)
    Oksm = graphene.List(OksmType)
    Ds_list = graphene.List(DsType,ds=graphene.String())
    Ds_name = graphene.List(DsType,ds=graphene.String())
    V012 = graphene.List(V012Type)
    V009 = graphene.List(V009Type)
    V020 = graphene.List(V020Type)
    Vra = graphene.List(VraType,otd=graphene.String())
    Vra_name = graphene.List(VraType,kod=graphene.String())
    V021_name = graphene.List(V021Type,spec=graphene.String())
    PR_OSOB = graphene.List(PR_OSOBType)
    V001 = graphene.List(V001Type)
    T006 = graphene.List(T006Type)
    Ab_Obsh = graphene.List(Ab_ObshType)
    V001_name = graphene.List(V001Type,kod=graphene.String())
    Pope = graphene.List(PopeType)
    Pope_name = graphene.List(PopeType,kod=graphene.String())
    Ab_Obsh_name = graphene.List(Ab_ObshType,kod=graphene.String())
    Prli = graphene.List(PrliType)
    Trv = graphene.List(TrvType)
    Isfin = graphene.List(IsfinType)
    Skom = graphene.List(SkomType)
    F008 = graphene.List(F008Type)
    F011 = graphene.List(F011Type)
    N018 = graphene.List(N018Type)
    N002 = graphene.List(N002Type,ds=graphene.String())
    N003 = graphene.List(N003Type,ds=graphene.String())
    N004 = graphene.List(N004Type,ds=graphene.String())
    N005 = graphene.List(N005Type,ds=graphene.String())
    N007 = graphene.List(N007Type)
    N010 = graphene.List(N010Type)
    N008 = graphene.List(N008Type)
    N011 = graphene.List(N011Type)
    N019 = graphene.List(N019Type)
    N013 = graphene.List(N013Type)
    N014 = graphene.List(N014Type)
    N001 = graphene.List(N001Type)
    V028 = graphene.List(V028Type)
    V029 = graphene.List(V029Type)
    V014 = graphene.List(V014Type)
    Prpg = graphene.List(PrpgType)
    PER = graphene.List(PERType)
    PR_PER = graphene.List(PR_PERType)
    Tip_pb = graphene.List(Tip_pbType)
    Met_pb = graphene.List(Met_pbType)
    V027 = graphene.List(V027Type)
    Trvnas = graphene.List(TrvnasType)
    F011_doc = graphene.List(F011Type,name=graphene.String())
    V002 = graphene.List(V002Type)
    anesthesia = graphene.List(anesthesiaType)
    # V018_bpoms = graphene.List(V018_bpomsType)
    # V019_bpoms = graphene.List(V019_bpomsType)
    # V018_sboms
    # V019_sboms = graphene.List(V019_sbomsType)
    Tar_vt = graphene.List(Tar_vtType,isf=graphene.String(),
                            kod_stat=graphene.String(),
                            metod=graphene.String()
                           )
    Tar_vt_List = graphene.List(Tar_vtType,isf=graphene.String())
    group_kc_dkk = graphene.List(group_kc_dkkType,ksg=graphene.String())
    T006_ksg_code_usl_title = graphene.List(T006Type,ksg=graphene.String())
    Age_group = graphene.List(Age_groupType)

    Vra_list = graphene.List(VraType,vra=graphene.String())
    Vra_list_kod_name = graphene.List(VraType)
    V001_list = graphene.List(V001Type,kod=graphene.String())
    DS_mod = graphene.List(DsType,ds=graphene.String())
    DS_mod_sop = graphene.List(DsType,ds=graphene.String())
    group_kc_group_get_ksg = graphene.List(group_kc_groupType,ksg=graphene.String())
    group_kc_group = graphene.List(group_kc_groupType)
    Otde_one = graphene.List(OtdeType,name=graphene.String())
    Code_med_dev_list = graphene.List(Code_med_dev_groupType)
    T003_ksg = graphene.List(T003Type,ksg=graphene.String())
    group_kc_group_ksg = graphene.List(group_kc_groupType,ksg=graphene.String())
    V036_list = graphene.List(V036_groupType)


    def resolve_V005(*args, **kwargs):
        if 'V005_hospital' in cache:
            return cache.get('V005_hospital')
        else:
            cache.set('V005_hospital', V005.objects.filter(dateend=None).all(), timeout=60 * 360)
            return V005.objects.filter(dateend=None).all()
    def resolve_Otde(self,info,*args, **kwargs):
        # if 'Otde_hospital' in cache:
        #     return cache.get('Otde_hospital')
        # else:
        #     cache.set('Otde_hospital', otde.objects.filter(dateend=None).all(), timeout=60 * 360)
        #     return otde.objects.filter(dateend=None).all()
        user = MyUser.objects.get(user=info.context.user.id)
        if user.ws.kod == 1:
            return otde.objects.filter(dateend=None,tipe=1).all()
        elif user.ws.kod == 2:
            return otde.objects.filter(dateend=None,tipe=2).all()

    def resolve_Rab_ner(*args,**kwargs):
        if 'Rab_ner_hospital' in cache:
            return cache.get('Rab_ner_hospital')
        else:
            cache.set('Rab_ner_hospital', Rab_Ner.objects.filter(dateend=None).all(), timeout=60*360)
            return Rab_Ner.objects.filter(dateend=None).all()

    def resolve_T004(*args,**kwargs):
        if 'T004_hospital' in cache:
            return cache.get('T004_hospital')
        else:
            cache.set('T004_hospital', T004.objects.filter(dateend=None).all(), timeout=60 * 360)
            return T004.objects.filter(dateend=None).all()

    def resolve_F003(*args,**kwargs):
        if 'F003_hospital' in cache:
            return cache.get('F003_hospital')
        else:
            cache.set('F003_hospital', F003.objects.filter(dateend=None).all(), timeout=60 * 360)
            return F003.objects.filter(dateend=None).all()

    def resolve_Vrzb(*args,**kwargs):
        if 'Vrzb_hospital' in cache:
            return cache.get('Vrzb_hospital')
        else:
            cache.set('Vrzb_hospital', Vrzb.objects.filter(dateend=None).order_by('-id').all(), timeout=60 * 360)
            return Vrzb.objects.filter(dateend=None).order_by('-id').all()

    def resolve_Oksm(*args, **kwargs):
        if 'Oksm_hospital' in cache:
            return cache.get('Oksm_hospital')
        else:
            cache.set('Oksm_hospital', Oksm.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Oksm.objects.filter(dateend=None).all()

    def resolve_Ds_list(*args, **kwargs):
        ds = kwargs.get('ds',None)
        return Ds.objects.filter(kod__icontains=ds,dateend=None).all()[:10]

    def resolve_Ds_name(*args,**kwargs):
        ds = kwargs.get('ds',None)
        return Ds.objects.filter(kod=ds, dateend=None).all()[:10]

    def resolve_V012(*args, **kwargs):
        if 'V012_hospital' in cache:
            return cache.get('V012_hospital')
        else:
            cache.set('V012_hospital', V012.objects.filter(id_iz__istartswith='1',dateend=None).all(), timeout=60 * 360)
            return V012.objects.filter(id_iz__istartswith='1',dateend=None).all()

    def resolve_V009(*args, **kwargs):
        if 'V009_hospital' in cache:
            return cache.get('V009_hospital')
        else:
            cache.set('V009_hospital', V009.objects.filter(id_tip__istartswith='1',dateend=None).all(),timeout=60 * 360)
            return V009.objects.filter(id_tip__istartswith='1',dateend=None).all()

    def resolve_V020(*args, **kwargs):
        if 'V020_hospital' in cache:
            return cache.get('V020_hospital')
        else:
            cache.set('V020_hospital', V020.objects.filter(dateend=None).all(),timeout=60 * 360)
            return V020.objects.filter(dateend=None).all()

    def resolve_Vra(*args, **kwargs):
        otd = kwargs.get('otd')
        if otd != "":
            return Vra.objects.filter(kod_ot=otd,dateend=None).all()
        return Vra.objects.filter(dateend=None).all()

    def resolve_Vra_name(*args,**kwargs):
        kod = kwargs.get('kod',None)
        return Vra.objects.filter(kod=kod,dateend=None).all()[:1]
    
    def resolve_Vra_list_kod_name(*args,**kwargs):
        return Vra.objects.filter(dateend=None).all().order_by('naim')

    def resolve_V021_name(*args,**kwargs):
        spec = kwargs.get('spec',None)
        return V021.objects.filter(id_spec=spec,dateend=None).all()

    def resolve_PR_OSOB(*args, **kwargs):
        if 'PR_OSOB_hospital' in cache:
            return cache.get('PR_OSOB_hospital')
        else:
            cache.set('PR_OSOB_hospital', PR_OSOB.objects.filter(dateend=None).order_by('-kod').all(), timeout=60 * 360)
            return PR_OSOB.objects.filter(dateend=None).order_by('-kod').all()


    def resolve_V001(*args,**kwargs):
        if 'V001_hospital' in cache:
            return cache.get('V001_hospital')
        else:
            cache.set('V001_hospital', V001.objects.filter(dateend=None).order_by('kod').all(), timeout=60 * 360)
            return V001.objects.filter(dateend=None).order_by('kod').all()


    def resolve_T006(root,info,*args, **kwargs):
        if 'T006_hospital' in cache:
            return cache.get('T006_hospital')
        else:
            cache.set('T006_hospital', T006.objects.filter(ksg__icontains='st', dateend=None).all(), timeout=60 * 360)
            return T006.objects.filter(ksg__icontains='st', dateend=None).all()
        # user = MyUser.objects.get(user=info.context.user.id)
        # if user.ws.kod == 1:
        #     return T006.objects.filter(ksg__icontains='st',dateend=None).all()
        # elif user.ws.kod == 2:
        #     return T006.objects.filter(ksg__icontains='ds', dateend=None).all()

    def resolve_Ab_Obsh(*args,**kwargs):
        if 'Ab_Obsh_hospital' in cache:
            return cache.get('Ab_Obsh_hospital')
        else:
            cache.set('Ab_Obsh_hospital', Ab_Obsh.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Ab_Obsh.objects.filter(dateend=None).all()

    def resolve_V001_name(*args,**kwargs):
        kod = kwargs.get('kod',None)
        return V001.objects.filter(kod=kod,dateend=None).all()

    def resolve_Pope(*args,**kwargs):
        if 'Pope_hospital' in cache:
            return cache.get('Pope_hospital')
        else:
            cache.set('Pope_hospital', Pope.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Pope.objects.filter(dateend=None).all()

    def resolve_Pope_name(*args,**kwargs):
        kod = kwargs.get('kod',None)
        return Pope.objects.filter(kod=kod,dateend=None).all()

    def resolve_Ab_Obsh_name(*args,**kwargs):
        kod = kwargs.get('kod',None)
        return Ab_Obsh.objects.filter(kod=kod,dateend=None).all()

    def resolve_Prli(*args,**kwargs):
        if 'Prli_hospital' in cache:
            return cache.get('Prli_hospital')
        else:
            cache.set('Prli_hospital', Prli.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Prli.objects.filter(dateend=None).all()

    def resolve_Trv(*args,**kwargs):
        if 'Trv_hospital' in cache:
            return cache.get('Trv_hospital')
        else:
            cache.set('Trv_hospital', Trv.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Trv.objects.filter(dateend=None).all()

    def resolve_Isfin(*args,**kwargs):
        if 'Isfin_hospital' in cache:
            return cache.get('Isfin_hospital')
        else:
            cache.set('Isfin_hospital', Isfin.objects.filter(dateend=None).order_by("num_filter").all(), timeout=60 * 360)
            return Isfin.objects.filter(dateend=None).order_by("num_filter").all()

    def resolve_Skom(*args,**kwargs):
        if 'Skom_hospital' in cache:
            return cache.get('Skom_hospital')
        else:
            cache.set('Skom_hospital', Skom.objects.filter(dateend=None).order_by("num_filter","naim").all(), timeout=60 * 360)
            return Skom.objects.filter(dateend=None).order_by("num_filter","naim").all()

    def resolve_F008(*args,**kwargs):
        if 'F008_hospital' in cache:
            return cache.get('F008_hospital')
        else:
            cache.set('F008_hospital', F008.objects.filter(id__in=[1,2,3],dateend=None).all(), timeout=60 * 360)
            return F008.objects.filter(dateend=None).all()

    def resolve_F011(*args,**kwargs):
        if 'F011_hospital' in cache:
            return cache.get('F011_hospital')
        else:
            cache.set('F011_hospital', F011.objects.filter(dateend=None).all(), timeout=60 * 360)
            return F011.objects.filter(dateend=None).all()

    def resolve_N018(*args,**kwargs):
        if 'N018_hospital' in cache:
            return cache.get('N018_hospital')
        else:
            cache.set('N018_hospital', N018.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N018.objects.filter(dateend=None).all()

    def resolve_N002(*args,**kwargs):
        ds = kwargs.get('ds',None)
        return N002.objects.filter(ds_st=ds,dateend=None).all()

    def resolve_N003(*args, **kwargs):
        ds = kwargs.get('ds', None)
        return N003.objects.filter(ds_t=ds, dateend=None).all()

    def resolve_N004(*args, **kwargs):
        ds = kwargs.get('ds', None)
        return N004.objects.filter(ds_n=ds, dateend=None).all()

    def resolve_N005(*args, **kwargs):
        ds = kwargs.get('ds', None)
        return N005.objects.filter(ds_m=ds, dateend=None).all()

    def resolve_N007(*args,**kwargs):
        if 'N007_hospital' in cache:
            return cache.get('N007_hospital')
        else:
            cache.set('N007_hospital', N007.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N007.objects.filter(dateend=None).all()

    def resolve_N010(*args,**kwargs):
        if 'N010_hospital' in cache:
            return cache.get('N010_hospital')
        else:
            cache.set('N010_hospital', N010.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N010.objects.filter(dateend=None).all()

    def resolve_N008(*args,**kwargs):
        if 'N008_hospital' in cache:
            return cache.get('N008_hospital')
        else:
            cache.set('N008_hospital', N008.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N008.objects.filter(dateend=None).all()

    def resolve_N011(*args,**kwargs):
        if 'N011_hospital' in cache:
            return cache.get('N011_hospital')
        else:
            cache.set('N011_hospital', N011.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N011.objects.filter(dateend=None).all()

    def resolve_N019(*args,**kwargs):
        if 'N019_hospital' in cache:
            return cache.get('N019_hospital')
        else:
            cache.set('N019_hospital', N019.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N019.objects.filter(dateend=None).all()

    def resolve_N013(*args,**kwargs):
        if 'N013_hospital' in cache:
            return cache.get('N013_hospital')
        else:
            cache.set('N013_hospital', N013.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N013.objects.filter(dateend=None).all()

    def resolve_N014(*args,**kwargs):
        if 'N014_hospital' in cache:
            return cache.get('N014_hospital')
        else:
            cache.set('N014_hospital', N014.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N014.objects.filter(dateend=None).all()

    def resolve_N001(*args,**kwargs):
        if 'N001_hospital' in cache:
            return cache.get('N001_hospital')
        else:
            cache.set('N001_hospital', N001.objects.filter(dateend=None).all(), timeout=60 * 360)
            return N001.objects.filter(dateend=None).all()

    def resolve_V028(*args,**kwargs):
        if 'V028_hospital' in cache:
            return cache.get('V028_hospital')
        else:
            cache.set('V028_hospital', V028.objects.filter(dateend=None).all(), timeout=60 * 360)
            return V028.objects.filter(dateend=None).all()

    def resolve_V029(*args,**kwargs):
        if 'V029_hospital' in cache:
            return cache.get('V029_hospital')
        else:
            cache.set('V029_hospital', V029.objects.filter(dateend=None).all(), timeout=60 * 360)
            return V029.objects.filter(dateend=None).all()

    def resolve_V014(*args,**kwargs):
        if 'V014_hospital' in cache:
            return cache.get('V014_hospital')
        else:
            cache.set('V014_hospital', V014.objects.filter(dateend=None).exclude(id=2).all(), timeout=60 * 360)
            return V014.objects.filter(dateend=None).exclude(id=2).all()

    def resolve_Prpg(*args,**kwargs):
        if 'Prpg_hospital' in cache:
            return cache.get('Prpg_hospital')
        else:
            cache.set('Prpg_hospital', Prpg.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Prpg.objects.filter(dateend=None).all()

    def resolve_PER(*args,**kwargs):
        if 'PER_hospital' in cache:
            return cache.get('PER_hospital')
        else:
            cache.set('PER_hospital', PER.objects.filter(dateend=None).all(), timeout=60 * 360)
            return PER.objects.filter(dateend=None).all()

    def resolve_PR_PER(*args,**kwargs):
        if 'PR_PER_hospital' in cache:
            return cache.get('PR_PER_hospital')
        else:
            cache.set('PR_PER_hospital', PR_PER.objects.filter(dateend=None).all(), timeout=60 * 360)
            return PR_PER.objects.filter(dateend=None).all()

    def resolve_Tip_pb(*args,**kwargs):
        if 'Tip_pb_hospital' in cache:
            return cache.get('Tip_pb_hospital')
        else:
            cache.set('Tip_pb_hospital', Tip_pb.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Tip_pb.objects.filter(dateend=None).all()

    def resolve_Met_pb(*args,**kwargs):
        if 'Met_pb_hospital' in cache:
            return cache.get('Met_pb_hospital')
        else:
            cache.set('Met_pb_hospital', Met_pb.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Met_pb.objects.filter(dateend=None).all()

    def resolve_V027(*args,**kwargs):
        if 'V027_hospital' in cache:
            return cache.get('V027_hospital')
        else:
            cache.set('V027_hospital', V027.objects.filter(dateend=None).all(), timeout=60 * 360)
            return V027.objects.filter(dateend=None).all()

    def resolve_Trvnas(*args,**kwargs):
        if 'Trvnas_hospital' in cache:
            return cache.get('Trvnas_hospital')
        else:
            cache.set('Trvnas_hospital', Trvnas.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Trvnas.objects.filter(dateend=None).all()

    def resolve_F011_doc(*args,**kwargs):
        name = kwargs.get('name',None)
        return F011.objects.filter(docname=name,dateend=None).all()

    def resolve_V002(*args,**kwargs):
        if 'V002_hospital' in cache:
            return cache.get('V002_hospital')
        else:
            cache.set('V002_hospital', V002.objects.filter(dateend=None).all(), timeout=60 * 360)
            return V002.objects.filter(dateend=None).all()

    def resolve_anesthesia(*args,**kwargs):
        if 'anesthesia_hospital' in cache:
            return cache.get('anesthesia_hospital')
        else:
            cache.set('anesthesia_hospital', anesthesia.objects.filter(dateend=None).all(), timeout=60 * 360)
            return anesthesia.objects.filter(dateend=None).all()

    # def resolve_V018_bpoms(*args,**kwargs):
    #     if 'V018_bpoms_hospital' in cache:
    #         return cache.get('V018_bpoms_hospital')
    #     else:
    #         cache.set('V018_bpoms_hospital', V018_bpoms.objects.filter(dateend=None).all(), timeout=60 * 360)
    #         return V018_bpoms.objects.filter(dateend=None).all()

    # def resolve_V019_bpoms(*args,**kwargs):
    #     if 'V019_bpoms_hospital' in cache:
    #         return cache.get('V019_bpoms_hospital')
    #     else:
    #         dateend__max = V019_bpoms.objects.aggregate(Max('dateend'))['dateend__max']
    #         cache.set('V018_bpoms_hospital',V019_bpoms.objects.filter(dateend=dateend__max).all(), timeout=60 * 360)
    #         return V019_bpoms.objects.filter(dateend=dateend__max).all()

    # def resolve_V019_sboms(*args,**kwargs):
    #     if 'V019_sboms_hospital' in cache:
    #         return cache.get('V019_sboms_hospital')
    #     else:
    #         cache.set('V019_sboms_hospital',V019_sboms.objects.exclude(idhvid=None).filter(dateend=None).all().distinct(), timeout=60 * 360)
    #         return V019_sboms.objects.exclude(idhvid=None).filter(dateend=None).all().distinct()

    def resolve_Tar_vt(*args,**kwargs):
        isf = kwargs.get('isf',None)
        kod_stat = kwargs.get('kod_stat',None)
        metod = kwargs.get('metod',None)
        if isf == 'Д':
            return Tar_vt.objects.filter(isf=isf,kod_stat=kod_stat,metod__icontains=metod,dateend=None).all()
        else:
            return Tar_vt.objects.filter(kod_stat=kod_stat,metod__icontains=metod,dateend=None).exclude(isf='Д').all()

    def resolve_Tar_vt_List(self,*args,**kwargs):
        isf = kwargs.get('isf', None)
        if isf == 'Д':
            return Tar_vt.objects.filter(isf__icontains=isf,dateend=None).all()
        return Tar_vt.objects.exclude(isf='Д')

    def resolve_group_kc_dkk(*args,**kwargs):
        ksg = kwargs.get('ksg',None)
        return group_kc_dkk.objects.filter(ksg_1=ksg,dateend=None).all()

    def resolve_T006_ksg_code_usl_title(root,info,*args, **kwargs):
        ksg = kwargs.get('ksg',None)
        user = MyUser.objects.get(user=info.context.user.id)
        return T006.objects.filter(ksg__icontains='st', code_usl_kz=ksg, dateend=None).all()
        # if user.ws.kod == 1:
        #     return T006.objects.filter(ksg__icontains='st',code_usl_kz=ksg, dateend=None).all()
        # elif user.ws.kod == 2:
        #     return T006.objects.filter(ksg__icontains='ds',code_usl_kz=ksg, dateend=None).all()
    
    def resolve_Age_group(*args,**kwsrgs):
        if 'Age_group_sboms_hospital' in cache:
            return cache.get('Age_group_sboms_hospital')
        else:
            cache.set('Age_group_sboms_hospital',Age_group.objects.all().order_by('id'), timeout=60 * 360)
            return Age_group.objects.all().order_by('id')

    def resolve_Vra_list(*args,**kwargs):
        vra = kwargs.get('vra',None)
        return Vra.objects.filter(kod__icontains=vra, dateend=None).all()[:10]
    
    def resolve_V001_list(*args,**kwargs):
        kod = kwargs.get('kod',None)
        return V001.objects.filter(kod__icontains=kod,dateend=None).all()[:10]
    

    def resolve_DS_mod(*args,**kwargs):
        ds = kwargs.get('ds',None)
        ds_list = list(Ds.objects.filter(Q(kod__range=('D55','D61.9')) | Q(kod__istartswith='D64') | Q(kod__istartswith='D74') | Q(kod__range=('D65','D69.9'))
                                        |Q(kod__range=('I20','I23.8')) | Q(kod__range=('J11','J18.9')) |Q(kod__range=('K40','K46.9'))
                                        | Q(kod__istartswith='K85') |Q(kod__istartswith='M86') |Q(kod__istartswith='U07')).values_list('kod'))
        ds_list = [ds[0] for ds in ds_list]
        # ds_sop = list(Ds.objects.filter(Q(kod__range=('A40','A41')) | Q(kod__istartswith='A48') | Q(kod__istartswith='D62') | Q(kod__istartswith='I26')).values_list('kod'))
        # ds_sop = [ds[0] for ds in ds_sop]

        if ds in ds_list:
            return Ds.objects.filter(kod=ds)
        # elif ds in ds_sop:
        #     return Ds.objects.filter(kod=ds)
        return []
    
    def resolve_DS_mod_sop(*args,**kwargs):
        ds = kwargs.get('ds',None)
        ds_sop = list(Ds.objects.filter(Q(kod__range=('A40','A41.9')) | Q(kod__istartswith='A48') | Q(kod__istartswith='D62') | Q(kod__istartswith='I26')).values_list('kod'))
        ds_sop = [ds[0] for ds in ds_sop]
        if ds in ds_sop:
            return Ds.objects.filter(kod=ds)
        return []
    
    def resolve_group_kc_group(info,*args,**kwargs):
        if 'kc_group_hospital' in cache:
            return cache.get('kc_group_hospital')
        else:
            data = group_kc_group.objects.values('code_usl_kz').filter(ksg__icontains='st')
            rez = list(set(map(lambda r:r['code_usl_kz'],data)))
            list_id = list(map(lambda r:group_kc_group.objects.values('id').filter(code_usl_kz=r)[:1][0]['id'],rez))
            cache.set('kc_group_hospital', group_kc_group.objects.filter(id__in=list_id), timeout=60*360)
            return group_kc_group.objects.filter(id__in=list_id)



    def resolve_Otde_one(*args,**kwargs):
        name = kwargs.get('name',None)
        return otde.objects.filter(naim=name,dateend=None)

    def resolve_Code_med_dev_list(self,*args, **kwargs):
        if 'Code_med_dev_list_hospital' in cache:
            return cache.get('Code_med_dev_list_hospital')
        else:
            cache.set('Code_med_dev_list_hospital', Code_med_dev.objects.filter(dateend=None).all(), timeout=60 * 360)
            return Code_med_dev.objects.filter(dateend=None).all()

    def resolve_T003_ksg(self,*args, **kwargs):
        ksg = kwargs.get('ksg', None)
        return T003.objects.filter(vidpom=1,usl_ok=1,dateend=None,code_usl_kz=ksg)

    def resolve_group_kc_group_get_ksg(self,*args, **kwargs):
        ksg = kwargs.get('ksg', None)
        return group_kc_group.objects.filter(code_usl_kz=ksg)[:1]

    def resolve_V036_list(self,*args, **kwargs):
        if 'V036_list_hospital' in cache:
            return cache.get('V036_list_hospital')
        else:
            cache.set('V036_list_hospital', V036.objects.filter(dateend=None).all(), timeout=60 * 360)
            return V036.objects.filter(dateend=None).all()





schema = graphene.Schema(query=Query)