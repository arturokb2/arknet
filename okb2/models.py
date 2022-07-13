from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
from django.conf import settings

class MyUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,blank=True,null=True)
    ws = models.ForeignKey('Ws',on_delete=models.SET_NULL,blank=True,null=True)
    statistics_type = models.ForeignKey('Statistics_type',on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f"{self.user}-{self.statistics_type}"

# Таблица справочников
class Statistics_type(models.Model):
    name = models.CharField(max_length=254,blank=True,null=True)

    def __str__(self):
        return self.name

#Классификатор типов документов, подтверждающих факт страхования по ОМС
class F008(models.Model):
    id_tip = models.IntegerField()
    tip_name = models.CharField(max_length=254,verbose_name='Тип документа')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.tip_name
    
    class Meta:
        ordering = ['id_tip']

#Классификатор условий оказания медицинской помощи
class V006(models.Model):
    id_tip = models.IntegerField()
    tip_name = models.CharField(max_length=254,verbose_name='Тип оказания мед.помощи')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tip_name

#Классификатор видов медицинской помощи
class V008(models.Model):
    id_tip = models.IntegerField()
    tip_name = models.CharField(max_length=254,verbose_name='Вид медицинской помощи')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tip_name
   


#Классификатор форм оказания медицинской помощи
class V014(models.Model):
    id_tip = models.IntegerField()
    tip_name = models.CharField(max_length=254,verbose_name='Классификатор форм оказания мед.помощи')
    kod = models.CharField(max_length=1,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tip_name

#Единый реестр медицинских организаций, осуществляющих деятельность в сфере ОМС
class F003(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=120,blank=True,null=True)
    mo = models.CharField(max_length=10,blank=True,null=True)
    naim_r = models.CharField(max_length=120,blank=True,null=True)
    adr = models.CharField(max_length=50,blank=True,null=True)
    rshet = models.CharField(max_length=70,blank=True,null=True)
    bik = models.CharField(max_length=30,blank=True,null=True)
    ksh = models.CharField(max_length=30,blank=True,null=True)
    inn = models.CharField(max_length=30,blank=True,null=True)
    okonx = models.CharField(max_length=30,blank=True,null=True)
    okpo = models.CharField(max_length=30,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.naim
#Классификатор результатов обращения за медицинской помощью
class V009(models.Model):
    id_tip = models.IntegerField()
    tip_name = models.CharField(max_length=254,verbose_name='Классификатор результатов обращения за мед.помощью')
    dl_uslov = models.IntegerField()
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tip_name + ' ' + str(self.id_tip)

#Классификатор исходов заболеваний
class V012(models.Model):
    id_iz = models.IntegerField()
    iz_name = models.CharField(max_length=254,verbose_name='Классификатор исходов заболеваний')
    dl_uslov = models.IntegerField()
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.iz_name + ' ' +str(self.id_iz)

#Классификатор способов оплаты медицинской помощи
class V010(models.Model):
    id_sp = models.IntegerField()
    spname = models.CharField(max_length=254,verbose_name='Классификатор исходов заболеваний')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.spname

#Классификатор профилей оказанной медицинской помощи
class V002(models.Model):
    id_pr = models.IntegerField()
    prname = models.CharField(max_length=500,verbose_name='Классификатор профилей оказанной медицинской помощи')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.prname

#Классификатор профилей коек
class V020(models.Model):
    idk_pr = models.IntegerField()
    k_prname = models.CharField(max_length=254,verbose_name='Классификатор профилей коек')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.k_prname

#Классификатор целей посещения
class V025(models.Model):
    id_pc = models.IntegerField()
    n_pc = models.CharField(max_length=254,verbose_name='Классификатор целей посещения')
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.n_pc

#Классификатор медицинских специальностей
class V021(models.Model):
    id_spec = models.IntegerField()
    specname = models.CharField(max_length=500,blank=True,null=True)
    postname = models.CharField(max_length=500,blank=True,null=True)
    id_post_mz = models.IntegerField(blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.specname

#Классификатор клинико-статистические группы
class V023(models.Model):
    id_ump = models.IntegerField()
    k_ksg = models.CharField(max_length=254,blank=True,null=True)
    n_ksg = models.CharField(max_length=300,blank=True,null=True)
    koef_z = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id_ump)

#Классификатор клинико-профильных групп (KPG)
class V026(models.Model):
    id_ump = models.IntegerField()
    k_kpg = models.CharField(max_length=350)
    n_kpg = models.CharField(max_length=500)
    koef_z = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id_ump)

#Классификатор классификационных критериев (DopKr)
class V024(models.Model):
    id_dkk = models.CharField(max_length=254)
    dkkname = models.CharField(max_length=500)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.id_dkk




#Территориальный классификатор услуг
class T003(models.Model):
    kod = models.CharField(max_length=254)
    name = models.CharField(max_length=1024)
    vidpom = models.IntegerField()
    usl_ok = models.IntegerField()
    title = models.CharField(max_length=254,blank=True,null=True)
    idsp = models.IntegerField()
    active = models.CharField(max_length=254,blank=True,null=True)
    code_usl_kz = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.kod

class T004(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class T005(models.Model):
    okato = models.CharField(max_length=8,blank=True,null=True)
    code_mo = models.CharField(max_length=8,blank=True,null=True)
    id_dokt = models.CharField(max_length=30,blank=True,null=True)
    fam = models.CharField(max_length=80,blank=True,null=True)
    im = models.CharField(max_length=80,blank=True,null=True)
    ot = models.CharField(max_length=80,blank=True,null=True)
    dr = models.CharField(max_length=30,blank=True,null=True)
    snils = models.CharField(max_length=30,blank=True,null=True)
    ogrn = models.CharField(max_length=30,blank=True,null=True)
    code_dokt = models.CharField(max_length=20,blank=True,null=True)
    code_vc = models.IntegerField(blank=True,null=True)
    name_1 = models.CharField(max_length=1000,blank=True,null=True)
    dokt_sp = models.CharField(max_length=150,blank=True,null=True)
    name_2 = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)
    comment = models.CharField(max_length=200,blank=True,null=True)

class Vra(models.Model):
    kod = models.CharField(max_length=10,blank=True,null=True)
    naim = models.CharField(max_length=25,blank=True,null=True)
    ini = models.CharField(max_length=2,blank=True,null=True)
    kod_ot = models.CharField(max_length=5,blank=True,null=True)
    t005 = models.CharField(max_length=8,blank=True,null=True)
    kodvr = models.CharField(max_length=8,blank=True,null=True)
    kod_spec = models.CharField(max_length=10,blank=True,null=True)
    v004 = models.CharField(max_length=10,blank=True,null=True)
    v002 = models.CharField(max_length=10,blank=True,null=True)
    v003 = models.CharField(max_length=10,blank=True,null=True)
    v015 = models.CharField(max_length=15,blank=True,null=True)
    v021 = models.CharField(max_length=10,blank=True,null=True)
    n_spec = models.CharField(max_length=50,blank=True,null=True)
    kod_lpy = models.CharField(max_length=5,blank=True,null=True)
    xar_s = models.CharField(max_length=5,blank=True,null=True)
    npb = models.CharField(max_length=15,blank=True,null=True)
    norma = models.CharField(max_length=10,blank=True,null=True)
    zaw = models.CharField(max_length=5,blank=True,null=True)
    kod_u = models.CharField(max_length=10,blank=True,null=True)
    kod_pro = models.CharField(max_length=10,blank=True,null=True)
    naim_t = models.CharField(max_length=15,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - ({} {})'.format(self.kod,self.naim,self.ini)




class T006(models.Model):
    usl_ok = models.CharField(max_length=500,blank=True,null=True)
    n_n = models.CharField(max_length=500,blank=True,null=True)
    ksg = models.CharField(max_length=500,blank=True,null=True)
    code_usl = models.CharField(max_length=500,blank=True,null=True)
    title = models.CharField(max_length=500,blank=True,null=True)
    kpg = models.CharField(max_length=500,blank=True,null=True)
    name = models.CharField(max_length=500,blank=True,null=True)
    code_usl_kz = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ksg

#Справочник СМО РФ
# class F002(models.Model):
#     pass

#Номенклатура медицинских услуг (вид медицинского вмешательства)
class V001(models.Model):
    kod = models.CharField(max_length=30,blank=True,null=True)
    naim = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return str(self.kod)

# Манипуляции и Операции (hospital)(V001)
class Ab_Obsh(models.Model):
    kod = models.CharField(max_length=10,blank=True,null=True)
    gr = models.CharField(max_length=5,blank=True,null=True)
    ima = models.CharField(max_length=150,blank=True,null=True)
    ksl = models.CharField(max_length=40,blank=True,null=True)
    nor = models.IntegerField(blank=True,null=True)
    prm = models.CharField(max_length=5,blank=True,null=True)
    pro = models.CharField(max_length=5,blank=True,null=True)
    tnz = models.IntegerField(blank=True,null=True)
    prib = models.IntegerField(blank=True,null=True)
    sum = models.CharField(max_length=50,blank=True,null=True)
    gr_tar = models.CharField(max_length=15,blank=True,null=True)
    pr_dor = models.CharField(max_length=10,blank=True,null=True)
    pr_osob = models.CharField(max_length=10,blank=True,null=True)
    kod_v001 = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.kod + ' ' + self.ima

	



#Классификатор видов высокотехнологичной медицинской помощи

# class V018_sboms(models.Model):
#     idhvid = models.CharField(max_length=100,blank=True,null=True)
#     x = models.CharField(max_length=30,blank=True,null=True)
#     hvidname = models.CharField(max_length=3000,blank=True,null=True)
#     datebeg = models.DateField(blank=True,null=True)
#     dateend = models.DateField(blank=True,null=True)

#     def __str__(self):
#         return self.idhvid



class V018_bpoms(models.Model):
    type = models.CharField(max_length=100,blank=True,null=True)
    version = models.CharField(max_length=100,blank=True,null=True)
    date = models.CharField(max_length=100,blank=True,null=True)
    idhvid = models.CharField(max_length=100,blank=True,null=True)
    hvidname = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.idhvid

class V018_sboms(models.Model):
    old_idhvid = models.CharField(max_length=100,blank=True,null=True)
    idhvid = models.CharField(max_length=100,blank=True,null=True)
    hvidname = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.idhvid

    





#Классификатор методов высокотехнологичной медицинской помощи
class V019_bpoms(models.Model):
    idhm = models.CharField(max_length=1000,blank=True,null=True)
    hmname = models.CharField(max_length=4000,blank=True,null=True)
    diag = models.CharField(max_length=4000,blank=True,null=True)
    hvid = models.CharField(max_length=1000,blank=True,null=True)
    hgr = models.CharField(max_length=1000,blank=True,null=True)
    hmodp = models.CharField(max_length=1000,blank=True,null=True)
    idmodp = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.idhm

class V019_sboms(models.Model):
    tp_oms = models.CharField(max_length=100,blank=True,null=True)
    idhm = models.CharField(max_length=100,blank=True,null=True)
    idhvid = models.CharField(max_length=100,blank=True,null=True)
    hmname = models.CharField(max_length=2000,blank=True,null=True)
    usl_ok = models.CharField(max_length=100,blank=True,null=True)
    diag = models.CharField(max_length=1000,blank=True,null=True)
    old_idhm = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.idhvid

#Характер заболевания (C_ZAB)
class V027(models.Model):
    id_cz = models.IntegerField()
    n_cz = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.n_cz

#Классификатор видов направления (NAPR_V)
class V028(models.Model):
    id_vn = models.IntegerField()
    n_vn = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.n_vn

#V029 Классификатор методов диагностического исследования (MET_ISSL)
class V029(models.Model):
    id_met = models.IntegerField()
    n_met = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.n_met

#N019 Классификатор целей консилиума (OnkCons)
class N019(models.Model):
    id_cons = models.IntegerField()
    cons_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.cons_name

#N018 Классификатор поводов обращения (OnkReas)
class N018(models.Model):
    id_reas = models.IntegerField()
    reas_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.reas_name

#N002 Классификатор стадий
class N002(models.Model):
    id_st = models.IntegerField()
    ds_st = models.CharField(max_length=254,blank=True,null=True)
    kod_st = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.kod_st

#N003 Классификатор Tumor
class N003(models.Model):
    id_t = models.IntegerField()
    ds_t = models.CharField(max_length=500,blank=True,null=True)
    kod_t = models.CharField(max_length=500,blank=True,null=True)
    t_name = models.CharField(max_length=500,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.kod_t

#N005 Классификатор Metastasis
class N005(models.Model):
    id_m = models.IntegerField()
    ds_m = models.CharField(max_length=254,blank=True,null=True)
    kod_m = models.CharField(max_length=254,blank=True,null=True)
    m_name = models.CharField(max_length=500,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.kod_m

#N007 Классификатор гистологии
class N007(models.Model):
    id_mrf = models.IntegerField()
    mrf_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id_mrf)

#N008 Классификатор результатов гистологических исследований (OnkMrfRt)
class N008(models.Model):
    id_r_m = models.IntegerField()
    id_mrf = models.IntegerField()
    r_m_name = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id_r_m)

#N010 Классификатор маркёров
class N010(models.Model):
    id_igh = models.IntegerField()
    kod_igh = models.CharField(max_length=254)
    igh_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id_igh)


#N011 Классификатор значений маркёров
class N011(models.Model):
    id_r_i = models.IntegerField()
    id_igh = models.IntegerField()
    kod_r_i = models.CharField(max_length=254)
    r_i_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id_r_i)

#N001 Код противопоказания или отказа
class N001(models.Model):
    id_prot = models.IntegerField()
    prot_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.prot_name

#N013 Классификатор типов лечения
class N013(models.Model):
    id_tlech = models.IntegerField()
    tlech_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tlech_name

#N014 Классификатор типов хирургического лечения
class N014(models.Model):
    id_thir = models.IntegerField()
    thir_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.thir_name
    
#Классификатор линий лекарственной терапии
class N015(models.Model):
    id_tlek = models.IntegerField()
    tlek_name_l = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tlek_name_l

#Классификатор циклов лекарственной терапии
class N016(models.Model):
    id_tlek_v = models.IntegerField()
    tlek_name_v = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tlek_name_v

#Классификатор типов лучевой терапии
class N017(models.Model):
    id_tluch = models.IntegerField()
    tluch_name = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tluch_name

#Классификатор лекарственных препаратов, применяемых при проведении лекарственной терапии (OnkLekp)
class N020(models.Model):
    id_lekp = models.CharField(max_length=1024,blank=True,null=True)
    mnn = models.CharField(max_length=1024,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.id_lekp

class dtrule(models.Model):
    rule = models.IntegerField()
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.rule)

#Классификатор типов диспансеризации
class V016(models.Model):
    iddt = models.CharField(max_length=254,blank=True,null=True)
    dtname = models.CharField(max_length=254,blank=True,null=True)
    id_dtrule = models.ManyToManyField(dtrule,blank=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.iddt)

#Классификатор пола застрахованного
class V005(models.Model):
    id_pol = models.IntegerField()
    polname = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.polname

#Классификатор результатов диспансеризации
class V017(models.Model):
    id_dr = models.IntegerField()
    drname = models.CharField(max_length=254)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.drname

#N004 Классификатор Nodus
class N004(models.Model):
    id_n = models.IntegerField()
    ds_n = models.CharField(max_length=512,blank=True,null=True)
    kod_n = models.CharField(max_length=512,blank=True,null=True)
    n_name = models.CharField(max_length=512,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.kod_n

#Классификатор типов документов, удостоверяющих личность
class F011(models.Model):
    id_doc = models.IntegerField()
    docname = models.CharField(max_length=254,blank=True,null=True)
    docser = models.CharField(max_length=254,blank=True,null=True)
    docnum = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True,null=True)
    dateend = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.docname


# Отделения
class otde(models.Model):
    npp = models.CharField(max_length=200,blank=True,null=True)
    kod = models.CharField(max_length=200,blank=True,null=True)
    kod_ot = models.CharField(max_length=300,blank=True,null=True)
    naim = models.CharField(max_length=200,blank=True,null=True)
    xar = models.CharField(max_length=200,blank=True,null=True)
    zav = models.CharField(max_length=200,blank=True,null=True)
    pr_otd = models.CharField(max_length=100,blank=True,null=True)
    nkd = models.CharField(max_length=100,blank=True,null=True)
    t007 = models.CharField(max_length=100,blank=True,null=True)
    t013 = models.CharField(max_length=150,blank=True,null=True)
    kod_w = models.CharField(max_length=100,blank=True,null=True)
    zamgv = models.CharField(max_length=100,blank=True,null=True)
    pl = models.CharField(max_length=200,blank=True,null=True)
    plb = models.CharField(max_length=200,blank=True,null=True)
    s1 = models.CharField(max_length=200,blank=True,null=True)
    s2 = models.CharField(max_length=200,blank=True,null=True)
    s3 = models.CharField(max_length=200,blank=True,null=True)
    s4 = models.CharField(max_length=200,blank=True,null=True)
    x_s = models.CharField(max_length=100,blank=True,null=True)
    npb = models.CharField(max_length=200,blank=True,null=True)
    nman = models.CharField(max_length=200,blank=True,null=True)
    kodi = models.CharField(max_length=200,blank=True,null=True)
    noper = models.CharField(max_length=200,blank=True,null=True)
    kod_u = models.CharField(max_length=300,blank=True,null=True)
    kod_ud = models.CharField(max_length=300,blank=True,null=True)
    kod_pr = models.CharField(max_length=300,blank=True,null=True)
    zagl1 = models.CharField(max_length=500,blank=True,null=True)
    naim_s = models.CharField(max_length=100,blank=True,null=True)
    tipe = models.IntegerField(blank=True,null=True)
    number_beds = models.IntegerField(blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

# Диагноз
class Ds(models.Model):
    kod = models.CharField(max_length=10,blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    naim_1 = models.CharField(max_length=100,blank=True,null=True)
    naim_2 = models.CharField(max_length=100,blank=True,null=True)
    naim_3 = models.CharField(max_length=100,blank=True,null=True)
    pr_pgg = models.CharField(max_length=10,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.kod

class Rab_Ner(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=30,blank=True,null=True)
    kod_o = models.IntegerField(blank=True,null=True)
    kod_r = models.IntegerField(blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim



#Классификатор стран мира
class Oksm(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=150,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Kladr(models.Model):
    naim = models.CharField(max_length=100,blank=True,null=True)
    socr = models.CharField(max_length=20,blank=True,null=True)
    code = models.CharField(max_length=20,blank=True,null=True)
    index = models.CharField(max_length=15,blank=True,null=True)
    gninmb = models.CharField(max_length=10,blank=True,null=True)
    uno = models.CharField(max_length=10,blank=True,null=True)
    ocatd = models.CharField(max_length=15,blank=True,null=True)
    status = models.CharField(max_length=3,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class Kladr_T(models.Model):
    naim = models.CharField(max_length=100,blank=True,null=True)
    socr = models.CharField(max_length=20,blank=True,null=True)
    code = models.CharField(max_length=20,blank=True,null=True)
    index = models.CharField(max_length=15,blank=True,null=True)
    gninmb = models.CharField(max_length=10,blank=True,null=True)
    uno = models.CharField(max_length=10,blank=True,null=True)
    ocatd = models.CharField(max_length=15,blank=True,null=True)
    status = models.CharField(max_length=3,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class Street(models.Model):
    naim = models.CharField(max_length=100,blank=True,null=True)
    socr = models.CharField(max_length=20,blank=True,null=True)
    code = models.CharField(max_length=25,blank=True,null=True)
    index = models.CharField(max_length=15,blank=True,null=True)
    gninmb = models.CharField(max_length=10,blank=True,null=True)
    uno = models.CharField(max_length=10,blank=True,null=True)
    ocatd = models.CharField(max_length=15,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)


class Street_T(models.Model):
    naim = models.CharField(max_length=100,blank=True,null=True)
    socr = models.CharField(max_length=20,blank=True,null=True)
    code = models.CharField(max_length=25,blank=True,null=True)
    index = models.CharField(max_length=15,blank=True,null=True)
    gninmb = models.CharField(max_length=10,blank=True,null=True)
    uno = models.CharField(max_length=10,blank=True,null=True)
    ocatd = models.CharField(max_length=15,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)



class Vrzb(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=50,blank=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class CJ(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=50,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim
#Тип льготы
class V_LGOTY(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    nain = models.CharField(max_length=50,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nain

#Страховые компании
class Skom(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=60,blank=True,null=True)
    ter = models.CharField(max_length=100,blank=True,null=True)
    kter = models.CharField(max_length=20,blank=True,null=True)
    smo = models.CharField(max_length=50,blank=True,null=True)
    smo_okato = models.CharField(max_length=50,blank=True,null=True)
    k_sotr = models.CharField(max_length=60,blank=True,null=True)
    ws = models.CharField(max_length=100,blank=True,null=True)
    naim_n = models.CharField(max_length=200,blank=True,null=True)
    ogrn = models.CharField(max_length=15,blank=True,null=True)
    ptf_l = models.CharField(max_length=10,blank=True,null=True)
    adres = models.CharField(max_length=100,blank=True,null=True)
    tsch = models.CharField(max_length=70,blank=True,null=True)
    ksch = models.CharField(max_length=50,blank=True,null=True)
    bik = models.CharField(max_length=100,blank=True,null=True)
    inn = models.CharField(max_length=100,blank=True,null=True)
    okonk = models.CharField(max_length=20,blank=True,null=True)
    okpo = models.CharField(max_length=100,blank=True,null=True)
    adr_b = models.CharField(max_length=50,blank=True,null=True)
    kod_r = models.CharField(max_length=100,blank=True,null=True)
    okato = models.CharField(max_length=15,blank=True,null=True)
    kpp = models.CharField(max_length=100,blank=True,null=True)
    okopf = models.CharField(max_length=20,blank=True,null=True)
    ktawr = models.CharField(max_length=20,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    num_filter = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.naim
    

class Prpg(models.Model):
    #Госпитализация
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=30,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Ws(models.Model):
    #Код подразделения
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=30,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim 

class PR_PER(models.Model):
    #Причина перевода
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=150,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Trv(models.Model):
    #Тип травм
    kod = models.CharField(max_length=10,blank=True,null=True)
    kod_o = models.CharField(max_length=10,blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim
        
class Trvnas(models.Model):
    kod = models.CharField(max_length=2,blank=True,null=True)
    naim = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class PY(models.Model):
    #место проведения операции
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class PR_OSOB(models.Model):
    #Отметка особенностей операции
    kod = models.CharField(max_length=10,blank=True,null=True)
    naim = models.CharField(max_length=300,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Xosl(models.Model):
    #Характер осложнения
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Posl(models.Model):
    #Причина осложнения
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Aosl(models.Model):
    #Экспертиза
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Trs(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=120,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim

class Pope(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=255,blank=True,null=True)
    tip = models.IntegerField(blank=True,null=True)
    naim_t = models.CharField(max_length=255,blank=True,null=True)
    organ = models.CharField(max_length=10,blank=True,null=True)
    naim_o = models.CharField(max_length=255,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim
#Причины летального исхода
class Prli(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.kod) + ' ' + self.naim


# class Tip_wsk(models.Model):


class Isfin(models.Model):
    kod = models.CharField(max_length=10,blank=True,null=True)
    naim = models.CharField(max_length=254,blank=True,null=True)
    npp = models.CharField(max_length=10,blank=True,null=True)
    naim_r = models.CharField(max_length=40,blank=True,null=True)
    pr = models.CharField(max_length=1,blank=True,null=True)
    miac = models.CharField(max_length=40,blank=True,null=True)
    miac_l = models.CharField(max_length=40,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    num_filter = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.naim
#Показания для прерывания беременности
class Tip_pb(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.kod)+ ' ' + self.naim
#Методы прерывания беременности
class Met_pb(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.kod) + ' ' + self.naim

class PER(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    naim = models.CharField(max_length=100,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.naim


class group_kc_ksg(models.Model):
    n = models.CharField(max_length=100,blank=True,null=True)
    ksg = models.CharField(max_length=100,blank=True,null=True)
    name_ksg = models.CharField(max_length=500,blank=True,null=True)
    kz = models.CharField(max_length=10,blank=True,null=True)
    prof_kod = models.CharField(max_length=10,blank=True,null=True)
    prof_name = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class group_kc_mkb_10(models.Model):
    kod = models.CharField(max_length=40,blank=True,null=True)
    name = models.CharField(max_length=500,blank=True,null=True)
    ksg_1 = models.CharField(max_length=20,blank=True,null=True)
    ksg_2 = models.CharField(max_length=20,blank=True,null=True)
    ksg_3 = models.CharField(max_length=20,blank=True,null=True)
    ksg_4 = models.CharField(max_length=20,blank=True,null=True)
    ksg_5 = models.CharField(max_length=20,blank=True,null=True)
    ksg_6 = models.CharField(max_length=20,blank=True,null=True)
    ksg_7 = models.CharField(max_length=20,blank=True,null=True)
    ksg_8 = models.CharField(max_length=20,blank=True,null=True)
    ksg_9 = models.CharField(max_length=20,blank=True,null=True)
    ksg_10 = models.CharField(max_length=20,blank=True,null=True)
    ksg_11 = models.CharField(max_length=20,blank=True,null=True)
    ksg_12 = models.CharField(max_length=20,blank=True,null=True)
    ksg_13 = models.CharField(max_length=20,blank=True,null=True)
    ksg_14 = models.CharField(max_length=20,blank=True,null=True)
    ksg_15 = models.CharField(max_length=20,blank=True,null=True)
    ksg_16 = models.CharField(max_length=20,blank=True,null=True)
    ksg_17 = models.CharField(max_length=20,blank=True,null=True)
    ksg_18 = models.CharField(max_length=20,blank=True,null=True)
    ksg_19 = models.CharField(max_length=20,blank=True,null=True)
    ksg_20 = models.CharField(max_length=20,blank=True,null=True)
    ksg_21 = models.CharField(max_length=20,blank=True,null=True)
    ksg_22 = models.CharField(max_length=20,blank=True,null=True)
    ksg_23 = models.CharField(max_length=20,blank=True,null=True)
    ksg_24 = models.CharField(max_length=20,blank=True,null=True)
    ksg_25 = models.CharField(max_length=20,blank=True,null=True)
    ksg_26 = models.CharField(max_length=20,blank=True,null=True)
    ksg_27 = models.CharField(max_length=20,blank=True,null=True)
    ksg_28 = models.CharField(max_length=20,blank=True,null=True)
    ksg_29 = models.CharField(max_length=20,blank=True,null=True)
    ksg_30 = models.CharField(max_length=20,blank=True,null=True)
    ksg_31 = models.CharField(max_length=20,blank=True,null=True)
    ksg_32 = models.CharField(max_length=20,blank=True,null=True)
    ksg_33 = models.CharField(max_length=20,blank=True,null=True)
    ksg_34 = models.CharField(max_length=20,blank=True,null=True)
    ksg_35 = models.CharField(max_length=20,blank=True,null=True)
    ksg_36 = models.CharField(max_length=20,blank=True,null=True)
    ksg_37 = models.CharField(max_length=20,blank=True,null=True)
    ksg_38 = models.CharField(max_length=20,blank=True,null=True)
    ksg_39 = models.CharField(max_length=20,blank=True,null=True)
    ksg_40 = models.CharField(max_length=20,blank=True,null=True)
    ksg_41 = models.CharField(max_length=20,blank=True,null=True)
    ksg_42 = models.CharField(max_length=20,blank=True,null=True)
    ksg_43 = models.CharField(max_length=20,blank=True,null=True)
    ksg_44 = models.CharField(max_length=20,blank=True,null=True)
    ksg_45 = models.CharField(max_length=20,blank=True,null=True)
    ksg_46 = models.CharField(max_length=20,blank=True,null=True)
    isp_ksg = models.CharField(max_length=20,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class group_kc_nomenclature(models.Model):
    kod = models.CharField(max_length=40,blank=True,null=True)
    name = models.CharField(max_length=500,blank=True,null=True)
    ksg_1 = models.CharField(max_length=20,blank=True,null=True)
    ksg_2 = models.CharField(max_length=20,blank=True,null=True)
    ksg_3 = models.CharField(max_length=20,blank=True,null=True)
    ksg_4 = models.CharField(max_length=20,blank=True,null=True)
    ksg_5 = models.CharField(max_length=20,blank=True,null=True)
    ksg_6 = models.CharField(max_length=20,blank=True,null=True)
    ksg_7 = models.CharField(max_length=20,blank=True,null=True)
    isp_ksg = models.CharField(max_length=20,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class group_kc_slp(models.Model):
    kod = models.CharField(max_length=40,blank=True,null=True)
    mnn = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=500,blank=True,null=True)
    num_day = models.CharField(max_length=20,blank=True,null=True)
    ksg = models.CharField(max_length=40,blank=True,null=True)
    isp_ksg = models.CharField(max_length=20,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)


class group_kc_mnn_lp(models.Model):
    kod = models.CharField(max_length=40,blank=True,null=True)
    mnn_lp = models.CharField(max_length=500,blank=True,null=True)
    ksg_1 = models.CharField(max_length=20,blank=True,null=True)
    ksg_2 = models.CharField(max_length=20,blank=True,null=True)
    ksg_3 = models.CharField(max_length=20,blank=True,null=True)
    ksg_4 = models.CharField(max_length=20,blank=True,null=True)
    ksg_5 = models.CharField(max_length=20,blank=True,null=True)
    isp_ksg = models.CharField(max_length=20,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class group_kc_dkk(models.Model):
    kod = models.CharField(max_length=40,blank=True,null=True)
    name = models.CharField(max_length=500,blank=True,null=True)
    ksg_1 = models.CharField(max_length=20,blank=True,null=True)
    ksg_2 = models.CharField(max_length=20,blank=True,null=True)
    ksg_3 = models.CharField(max_length=20,blank=True,null=True)
    ksg_4 = models.CharField(max_length=20,blank=True,null=True)
    ksg_5 = models.CharField(max_length=20,blank=True,null=True)
    isp_ksg = models.CharField(max_length=20,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class group_kc_group(models.Model):
    n = models.CharField(max_length=40,blank=True,null=True)
    mkb_10 = models.CharField(max_length=40,blank=True,null=True)
    mkb_10_2 = models.CharField(max_length=40,blank=True,null=True)
    mkb_10_3 = models.CharField(max_length=40,blank=True,null=True)
    code_usl = models.CharField(max_length=40,blank=True,null=True)
    age = models.CharField(max_length=40,blank=True,null=True)
    w = models.CharField(max_length=40,blank=True,null=True)
    duration = models.CharField(max_length=40,blank=True,null=True)
    ikk = models.CharField(max_length=40,blank=True,null=True)
    df = models.CharField(max_length=40,blank=True,null=True)
    ksg = models.CharField(max_length=40,blank=True,null=True)
    n_group = models.CharField(max_length=40,blank=True,null=True)
    code_usl_kz = models.CharField(max_length=100, blank=True, null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

class group_kc_group_det(models.Model):
    n = models.CharField(max_length=40,blank=True,null=True)
    mkb_10 = models.CharField(max_length=40,blank=True,null=True)
    mkb_10_name = models.CharField(max_length=500,blank=True,null=True)
    mkb_10_2 = models.CharField(max_length=40,blank=True,null=True)
    dd = models.CharField(max_length=40,blank=True,null=True)
    mkb_10_3 = models.CharField(max_length=40,blank=True,null=True)
    ds_oslo = models.CharField(max_length=500,blank=True,null=True)
    code_usl = models.CharField(max_length=40,blank=True,null=True)
    usl = models.CharField(max_length=500,blank=True,null=True)
    age = models.CharField(max_length=40,blank=True,null=True)
    w = models.CharField(max_length=40,blank=True,null=True)
    duration = models.CharField(max_length=40,blank=True,null=True)
    ikk = models.CharField(max_length=40,blank=True,null=True)
    df = models.CharField(max_length=40,blank=True,null=True)
    ksg = models.CharField(max_length=40,blank=True,null=True)
    ksg_ras = models.CharField(max_length=500,blank=True,null=True)
    n_group = models.CharField(max_length=40,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)


class anesthesia(models.Model):
    kod = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=254,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tar_vt(models.Model):
    kod = models.CharField(max_length=50,blank=True,null=True)
    kod_stat = models.CharField(max_length=50,blank=True,null=True)
    kod_r = models.CharField(max_length=50,blank=True,null=True)
    naim = models.CharField(max_length=1000,blank=True,null=True)
    tarif = models.DecimalField(max_digits=13,decimal_places=2,blank=True,null=True)
    isf = models.CharField(max_length=10,blank=True,null=True)
    v_tp = models.CharField(max_length=10,blank=True,null=True)
    metod = models.CharField(max_length=100,blank=True,null=True)
    mkb = models.CharField(max_length=500,blank=True,null=True)
    kod_dop = models.CharField(max_length=10,blank=True,null=True)
    otm = models.CharField(max_length=10,blank=True,null=True)
    kod_old = models.CharField(max_length=50,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.kod_stat}'

    # Д - Базовая высокотех
    # 5 - Сверх базовая
    # 7 - федеральный бюджет


#Тариф
class Tarif(models.Model):
    YearSp = models.CharField(max_length=254,blank=True,null=True)
    Kvartal = models.CharField(max_length=254, blank=True, null=True)
    Ur = models.CharField(max_length=254, blank=True, null=True)
    KOEF_D = models.CharField(max_length=254, blank=True, null=True)
    KodZz = models.CharField(max_length=254, blank=True, null=True)
    V_tp = models.CharField(max_length=254, blank=True, null=True)
    Usl_Ok = models.CharField(max_length=254, blank=True, null=True)
    N_Ksg = models.CharField(max_length=254, blank=True, null=True)
    Code_usl = models.CharField(max_length=254, blank=True, null=True)
    Caption = models.CharField(max_length=1000, blank=True, null=True)
    KOEF_Z = models.CharField(max_length=254, blank=True, null=True)
    Tarif = models.CharField(max_length=254, blank=True, null=True)
    BZTSZ = models.CharField(max_length=254, blank=True, null=True)
    KOEF_U = models.CharField(max_length=254, blank=True, null=True)
    Koef_Up = models.CharField(max_length=254, blank=True, null=True)
    Ver_Ksg = models.CharField(max_length=254, blank=True, null=True)
    SL_K = models.CharField(max_length=254, blank=True, null=True)
    IT_SL = models.CharField(max_length=254, blank=True, null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.YearSp}-{self.Kvartal}-{self.Ur}-{self.Code_usl}'


class Age_group(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name


class Code_med_dev(models.Model):
    kod_id = models.IntegerField(blank=True,null=True)
    rzn = models.CharField(max_length=20,blank=True,null=True)
    parent = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=1000,blank=True,null=True)
    localization = models.CharField(max_length=1000,blank=True,null=True)
    material = models.CharField(max_length=1000,blank=True,null=True)
    metal = models.CharField(max_length=1000,blank=True,null=True)
    sctid = models.CharField(max_length=1000,blank=True,null=True)
    order = models.CharField(max_length=1000,blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.kod_id}'

class UpdatePers(models.Model):
    file = models.FileField(upload_to='update_pers/%Y/%m/%d',blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'{self.file}'

    # def delete(self,*args,**kwargs):
    #     if os.path.isfile(self.file.path):
    #         os.remove(self.file.path)
    #     super(UpdatePers,self).delete(*args,**kwargs)
    # def delete(self, using=None, keep_parents=False):
    #     self.file.storage.delete(self.file.name)
    #     super().delete()

    # def delete(self, *args, **kwargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
    #     super().delete(*args, **kwargs)

class UpdatePersData(models.Model):
    fname = models.CharField(max_length=22,blank=True,null=True)
    coderem = models.CharField(max_length=3,blank=True,null=True)
    rem = models.CharField(max_length=255,blank=True,null=True)
    id_pac = models.CharField(max_length=36,blank=True,null=True)
    fam_reestr = models.CharField(max_length=24,blank=True,null=True)
    im_reestr = models.CharField(max_length=16,blank=True,null=True)
    ot_reestr = models.CharField(max_length=26,blank=True,null=True)
    dr_reestr = models.DateField(blank=True,null=True)
    w_reestr = models.IntegerField(blank=True,null=True)
    nhistory_r = models.CharField(max_length=50,blank=True,null=True)
    mr_reestr = models.CharField(max_length=150,blank=True,null=True)
    data_usl = models.DateField(blank=True,null=True)
    smo_reestr = models.IntegerField(blank=True,null=True)
    vpolis_ree = models.IntegerField(blank=True,null=True)
    npolis_ree = models.CharField(max_length=18,blank=True,null=True)
    spolis_ree = models.CharField(max_length=18,blank=True,null=True)
    smo_ogrn_r = models.CharField(max_length=15,blank=True,null=True)
    smo_ok_ree = models.CharField(max_length=5,blank=True,null=True)
    doctype_re = models.CharField(max_length=20,blank=True,null=True)
    docser_ree = models.CharField(max_length=19,blank=True,null=True)
    docnum_ree = models.CharField(max_length=20,blank=True,null=True)
    snils_ree = models.CharField(max_length=14,blank=True,null=True)
    fam = models.CharField(max_length=24,blank=True,null=True)
    im = models.CharField(max_length=15,blank=True,null=True)
    ot = models.CharField(max_length=27,blank=True,null=True)
    dr = models.CharField(max_length=10,blank=True,null=True)
    w = models.CharField(max_length=5,blank=True,null=True)
    smo = models.CharField(max_length=7,blank=True,null=True)
    vpolis = models.CharField(max_length=10,blank=True,null=True)
    spolis = models.CharField(max_length=10,blank=True,null=True)
    npolis = models.CharField(max_length=18,blank=True,null=True)
    dbeg = models.CharField(max_length=10,blank=True,null=True)
    dstop = models.DateField(blank=True,null=True)
    extnr = models.CharField(max_length=9,blank=True,null=True)
    smo_ok = models.CharField(max_length=5,blank=True,null=True)
    smo_ogrn = models.CharField(max_length=15,blank=True,null=True)
    dend = models.CharField(max_length=10,blank=True,null=True)
    novor = models.CharField(max_length=9,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

class V036(models.Model):
    s_code = models.CharField(max_length=200,blank=True,null=True)
    parameter = models.IntegerField(blank=True,null=True)
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
