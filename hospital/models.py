from operator import mod
from pickle import TRUE
from pyexpat import model
from re import T
from statistics import mode
from typing import Tuple
from okb2.models import (Ab_Obsh, Aosl, CJ, Ds, F003, F008, F011, Isfin, Met_pb, MyUser, N001, N002, N003,
                         N004, N005, N013, N014, N018, N019, Oksm, PER, PR_OSOB, PR_PER, PY, Pope, Posl, 
                         Prli, Prpg, Rab_Ner, Skom, Statistics_type, T003, T004, T006, Tar_vt, Tip_pb, Trs,
                         Trv, Trvnas, V001, V005, V009, V012, V014, V020, V021, V023, V027, V028, V029, V_LGOTY,
                        Vra, Vrzb, Ws, Xosl, anesthesia, group_kc_dkk, otde,Code_med_dev,group_kc_group)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .validators import validate_file

class Load_1c(models.Model):
    oper = models.FileField(upload_to='documents/hospital/%Y/%m/%d', validators=[validate_file],blank=True,null=True)
    sluch = models.FileField(upload_to='documents/hospital/%Y/%m/%d', validators=[validate_file],blank=True,null=True)
    sluch_10 = models.FileField(upload_to='documents/hospital/%Y/%m/%d', validators=[validate_file],blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    progress = models.CharField(max_length=100, blank=True, null=True, default='0')
    

    def __str__(self):
        return self.oper.name + ' ' + self.sluch.name

# class Load(models.Model):
#     oper = models.FileField(upload_to='documents/hospital/%Y/%m/%d', validators=[validate_file])
#     monitoring_res = models.FileField(upload_to='documents/hospital/%Y/%m/%d', validators=[validate_file])
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_delete, sender=Load_1c)
def submission_delete(sender, instance, **kwargs):
    instance.oper.delete(False)
    instance.sluch.delete(False)

class temp_oper(models.Model):
    kod_op = models.CharField(max_length=30, blank=True, null=True)
    dato = models.CharField(max_length=100, blank=True, null=True)
    goc_o = models.CharField(max_length=100, blank=True, null=True)
    py = models.CharField(max_length=100, blank=True, null=True)
    kodx = models.CharField(max_length=100, blank=True, null=True)
    kodxa = models.CharField(max_length=100, blank=True, null=True)
    kodxa1 = models.CharField(max_length=100, blank=True, null=True)
    obz = models.CharField(max_length=100, blank=True, null=True)
    kodan = models.CharField(max_length=100, blank=True, null=True)
    pr_osob = models.CharField(max_length=100, blank=True, null=True)
    k_mm = models.CharField(max_length=100, blank=True, null=True)
    nib = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

class temp_sluch(models.Model):
    fam = models.CharField(max_length=50, blank=True, null=True)
    im = models.CharField(max_length=50, blank=True, null=True)
    ot = models.CharField(max_length=50, blank=True, null=True)
    pol = models.CharField(max_length=1, blank=True, null=True)
    datr = models.CharField(max_length=100, blank=True, null=True)
    udl = models.CharField(max_length=50, blank=True, null=True)
    s_pasp = models.CharField(max_length=100, blank=True, null=True)
    n_pasp = models.CharField(max_length=6, blank=True, null=True)
    ss = models.CharField(max_length=14, blank=True, null=True)
    c_oksm = models.CharField(max_length=3, blank=True, null=True)
    adr = models.CharField(max_length=200, blank=True, null=True)
    m_roj = models.CharField(max_length=200, blank=True, null=True)
    cod_adr = models.CharField(max_length=50, blank=True, null=True)
    cj = models.CharField(max_length=1, blank=True, null=True)
    v_lgoty = models.CharField(max_length=1, blank=True, null=True)
    in_t = models.CharField(max_length=3, blank=True, null=True)
    rab = models.CharField(max_length=200, blank=True, null=True)
    r_n = models.CharField(max_length=20, blank=True, null=True)
    prof = models.CharField(max_length=150, blank=True, null=True)
    vec = models.CharField(max_length=5, blank=True, null=True)
    nib = models.CharField(max_length=15, blank=True, null=True)
    datp = models.CharField(max_length=100, blank=True, null=True)
    datv = models.CharField(max_length=100, blank=True, null=True)
    goc = models.CharField(max_length=1, blank=True, null=True)
    prpg = models.CharField(max_length=12, blank=True, null=True)
    vrez = models.CharField(max_length=20, blank=True, null=True)
    lpy = models.CharField(max_length=6, blank=True, null=True)
    ws = models.CharField(max_length=5, blank=True, null=True)
    tm_otd = models.CharField(max_length=6, blank=True, null=True)
    otd = models.CharField(max_length=100, blank=True, null=True)
    prof_k = models.CharField(max_length=50, blank=True, null=True)
    icx = models.CharField(max_length=1, blank=True, null=True)
    dsny = models.CharField(max_length=100, blank=True, null=True)
    dsk = models.CharField(max_length=100, blank=True, null=True)
    dskz = models.CharField(max_length=100, blank=True, null=True)
    dsc = models.CharField(max_length=100, blank=True, null=True)
    ds_osl = models.CharField(max_length=100, blank=True, null=True)
    dson = models.CharField(max_length=100, blank=True, null=True)
    ksg_osn = models.CharField(max_length=15, blank=True, null=True)
    ksg_sop = models.CharField(max_length=15, blank=True, null=True)
    vid_hmp = models.CharField(max_length=100, blank=True, null=True)
    metod_hmp = models.CharField(max_length=100, blank=True, null=True)
    trs = models.CharField(max_length=100, blank=True, null=True)
    tm_let = models.CharField(max_length=5, blank=True, null=True)
    pri = models.CharField(max_length=3, blank=True, null=True)
    ds_let = models.CharField(max_length=100, blank=True, null=True)
    wskr = models.CharField(max_length=1, blank=True, null=True)
    dspat = models.CharField(max_length=100, blank=True, null=True)
    rasxp = models.CharField(max_length=100, blank=True, null=True)
    otd_y = models.CharField(max_length=6, blank=True, null=True)
    vds = models.CharField(max_length=100, blank=True, null=True)
    sctp = models.CharField(max_length=16, blank=True, null=True)
    nctp = models.CharField(max_length=16, blank=True, null=True)
    t_pol = models.CharField(max_length=1, blank=True, null=True)
    ctkom = models.CharField(max_length=100, blank=True, null=True)
    ksg_ts = models.CharField(max_length=30, blank=True, null=True)
    t_trv = models.CharField(max_length=2, blank=True, null=True)
    details = models.CharField(max_length=6, blank=True, null=True)
    trav_ns = models.CharField(max_length=2, blank=True, null=True)
    pmg = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)


class temp_monitoring_res(models.Model):
    block_cd = models.CharField(max_length=1,blank=True,null=True)
    code_mo = models.CharField(max_length=6,blank=True,null=True)
    fam = models.CharField(max_length=100,blank=True,null=True)
    im = models.CharField(max_length=100,blank=True,null=True)
    ot = models.CharField(max_length=100,blank=True,null=True)
    w = models.IntegerField(blank=True,null=True)
    dr = models.DateField(blank=True,null=True)
    dost = models.CharField(max_length=48,blank=True,null=True)
    tel = models.CharField(max_length=10,blank=True,null=True)
    id_pac = models.CharField(max_length=100,blank=True,null=True)
    vpolis = models.IntegerField(blank=True,null=True)
    spolis = models.CharField(max_length=10,blank=True,null=True)
    npolis = models.CharField(max_length=20,blank=True,null=True)
    st_okato = models.CharField(max_length=5,blank=True,null=True)
    smo = models.CharField(max_length=5,blank=True,null=True)
    smo_ogrn = models.CharField(max_length=15,blank=True,null=True)
    smo_ok = models.CharField(max_length=5,blank=True,null=True)
    smo_nam = models.CharField(max_length=100,blank=True,null=True)
    inv = models.IntegerField(blank=True,null=True)
    novor = models.CharField(max_length=9,blank=True,null=True)
    vnov_d = models.IntegerField(blank=True,null=True)
    idcase = models.IntegerField(blank=True,null=True)
    usl_ok = models.IntegerField(blank=True,null=True)
    vidpom = models.IntegerField(blank=True,null=True)
    for_pom = models.IntegerField(blank=True,null=True)
    vid_hmp = models.CharField(max_length=20,blank=True,null=True)
    metod_hmp = models.CharField(max_length=20,blank=True,null=True)
    npr_mo = models.CharField(max_length=6,blank=True,null=True)
    lpu = models.CharField(max_length=6,blank=True,null=True)
    lpu_1 = models.CharField(max_length=8,blank=True,null=True)
    podr = models.CharField(max_length=12,blank=True,null=True)
    profil = models.IntegerField(blank=True,null=True)
    det = models.IntegerField(blank=True,null=True)
    tal_d = models.DateField(blank=True,null=True)
    tal_p = models.DateField(blank=True,null=True)
    tal_num = models.CharField(max_length=20,blank=True,null=True)
    nhistory = models.CharField(max_length=50,blank=True,null=True)
    p_per = models.IntegerField(blank=True,null=True)
    date_1 = models.DateField(blank=True,null=True)
    date_2 = models.DateField(blank=True,null=True)
    kd = models.IntegerField(blank=True,null=True)
    kp = models.IntegerField(blank=True,null=True)
    kd_z = models.IntegerField(blank=True,null=True)
    ds0 = models.CharField(max_length=10,blank=True,null=True)
    ds1 = models.CharField(max_length=10,blank=True,null=True)
    ds1_pr = models.IntegerField(blank=True,null=True)
    ds2 = models.CharField(max_length=100,blank=True,null=True)
    ds2_n = models.CharField(max_length=100, blank=True, null=True)
    ds3 = models.CharField(max_length=10,blank=True,null=True)
    vnov_m = models.CharField(max_length=32,blank=True,null=True)
    code_mes1 = models.CharField(max_length=20,blank=True,null=True)
    code_mes2 = models.CharField(max_length=20, blank=True, null=True)
    rslt = models.IntegerField(blank=True,null=True)
    rslt_d = models.IntegerField(blank=True,null=True)
    ishod = models.IntegerField(blank=True,null=True)
    prvs = models.IntegerField(blank=True,null=True)
    iddokt = models.CharField(max_length=25, blank=True, null=True)
    code_md = models.CharField(max_length=25, blank=True, null=True)
    os_sluch = models.CharField(max_length=20, blank=True, null=True)
    os_t002 = models.CharField(max_length=20, blank=True, null=True)
    idsp = models.IntegerField(blank=True,null=True)
    ed_col = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    kol_usl = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    tarif = models.DecimalField(max_digits=17,decimal_places=2,blank=True,null=True)
    sumv = models.DecimalField(max_digits=17,decimal_places=2,blank=True,null=True)
    sum_m = models.DecimalField(max_digits=17,decimal_places=2,blank=True,null=True)
    vid_vme = models.CharField(max_length=15, blank=True, null=True)
    code_usl = models.CharField(max_length=20, blank=True, null=True)
    fam_p = models.CharField(max_length=100, blank=True, null=True)
    im_p = models.CharField(max_length=100, blank=True, null=True)
    ot_p = models.CharField(max_length=100, blank=True, null=True)
    w_p = models.IntegerField(blank=True,null=True)
    dr_p = models.DateField(blank=True,null=True)
    dost_p = models.CharField(max_length=48, blank=True, null=True)
    mr = models.CharField(max_length=100, blank=True, null=True)
    doctype = models.CharField(max_length=2, blank=True, null=True)
    docser = models.CharField(max_length=10, blank=True, null=True)
    docnum = models.CharField(max_length=20, blank=True, null=True)
    docdate = models.DateField(blank=True,null=True)
    docorg = models.CharField(max_length=254, blank=True, null=True)
    snils = models.CharField(max_length=14, blank=True, null=True)
    okatog = models.CharField(max_length=11, blank=True, null=True)
    okatop = models.CharField(max_length=11, blank=True, null=True)
    year = models.IntegerField(blank=True,null=True)
    month = models.IntegerField(blank=True,null=True)
    nschet = models.CharField(max_length=17, blank=True, null=True)
    dschet = models.DateField(blank=True,null=True)
    plat = models.CharField(max_length=5, blank=True, null=True)
    v_tp = models.IntegerField(blank=True,null=True)
    disp = models.CharField(max_length=3, blank=True, null=True)
    pr_nov = models.IntegerField(blank=True,null=True)
    rep_u = models.IntegerField(blank=True,null=True)
    n_prot = models.CharField(max_length=15, blank=True, null=True)
    d_prot = models.DateField(blank=True,null=True)
    vbr = models.IntegerField(blank=True,null=True)
    p_otk = models.IntegerField(blank=True,null=True)
    naz_r = models.IntegerField(blank=True,null=True)
    naz_sp = models.IntegerField(blank=True,null=True)
    naz_v = models.IntegerField(blank=True,null=True)
    naz_pmp = models.IntegerField(blank=True,null=True)
    naz_pk = models.IntegerField(blank=True,null=True)
    napr_usl = models.CharField(max_length=15, blank=True, null=True)
    napr_date = models.DateField(blank=True,null=True)
    napr_mo = models.CharField(max_length=6, blank=True, null=True)
    napr_v = models.IntegerField(blank=True,null=True)
    pr_d_n = models.IntegerField(blank=True,null=True)
    npl = models.IntegerField(blank=True,null=True)
    npl_cf = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    sl_id = models.CharField(max_length=36, blank=True, null=True)
    idserv = models.CharField(max_length=36, blank=True, null=True)
    mse = models.IntegerField(blank=True,null=True)
    npr_date = models.DateField(blank=True,null=True)
    p_disp2 = models.IntegerField(blank=True,null=True)
    profil_k = models.IntegerField(blank=True,null=True)
    p_cel = models.CharField(max_length=3, blank=True, null=True)
    dn = models.IntegerField(blank=True,null=True)
    reab = models.IntegerField(blank=True,null=True)
    vb_p = models.IntegerField(blank=True,null=True)
    n_ksg = models.CharField(max_length=20, blank=True, null=True)
    ver_ksg = models.IntegerField(blank=True,null=True)
    ksg_pg = models.IntegerField(blank=True,null=True)
    koef_z = models.DecimalField(max_digits=12,decimal_places=5,blank=True,null=True)
    koef_up = models.DecimalField(max_digits=12,decimal_places=5,blank=True,null=True)
    bztsz = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    koef_d = models.DecimalField(max_digits=12,decimal_places=5,blank=True,null=True)
    koef_u = models.DecimalField(max_digits=12,decimal_places=5,blank=True,null=True)
    crit = models.CharField(max_length=254, blank=True, null=True)
    sl_k = models.IntegerField(blank=True,null=True)
    c_zab = models.IntegerField(blank=True,null=True)
    ds_onk = models.IntegerField(blank=True,null=True)
    onk_sl = models.IntegerField(blank=True,null=True)
    ds1_t = models.IntegerField(blank=True,null=True)
    stad = models.IntegerField(blank=True,null=True)
    onk_t = models.IntegerField(blank=True,null=True)
    onk_n = models.IntegerField(blank=True,null=True)
    onk_m = models.IntegerField(blank=True,null=True)
    mtstz = models.IntegerField(blank=True,null=True)
    sod = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    k_fr = models.IntegerField(blank=True,null=True)
    wei = models.DecimalField(max_digits=6,decimal_places=1,blank=True,null=True)
    hei = models.IntegerField(blank=True,null=True)
    bsa = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    b_diag = models.CharField(max_length=254, blank=True, null=True)
    b_prot = models.CharField(max_length=254, blank=True, null=True)
    cons = models.CharField(max_length=254, blank=True, null=True)
    onkusl_id = models.IntegerField(blank=True,null=True)
    usl_tip = models.IntegerField(blank=True,null=True)
    hir_tip = models.IntegerField(blank=True,null=True)
    lek_tip_l = models.IntegerField(blank=True,null=True)
    lek_tip_v = models.IntegerField(blank=True,null=True)
    luch_tip = models.IntegerField(blank=True,null=True)
    pptr = models.IntegerField(blank=True,null=True)
    date_inj = models.CharField(max_length=254,blank=True,null=True)
    regnum = models.CharField(max_length=6, blank=True, null=True)
    code_sh = models.CharField(max_length=10, blank=True, null=True)
    data_inj = models.DateField(blank=True, null=True)
    cod_mark = models.CharField(max_length=100, blank=True, null=True)
    ed_izm = models.CharField(max_length=3, blank=True, null=True)
    dose_inj = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    method_inj = models.CharField(max_length=3, blank=True, null=True)
    col_inj = models.IntegerField(blank=True, null=True)
    date_med = models.DateField(blank=True, null=True)
    codemeddev = models.IntegerField(blank=True, null=True)
    number_ser = models.CharField(max_length=100, blank=True, null=True)
    data_in = models.DateField(blank=True,null=True)
    date_out = models.DateField(blank=True,null=True)
    prscsdtbeg = models.DateField(blank=True,null=True)
    adres = models.CharField(max_length=254, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)






    date_in = models.DateField(blank=True,null=True)


    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

class temp_monitoring_res_10(temp_monitoring_res):
    pass

class Vb_s(models.Model):
    # Сведения о переводах
    id = models.BigAutoField(primary_key=True)
    kod_y = models.ForeignKey(F003,on_delete=models.SET_NULL, blank=True, null=True)
    pr_per = models.ForeignKey(PR_PER,on_delete=models.SET_NULL, blank=True, null=True)
    # Внутренний перевод
    potd = models.ForeignKey(otde,on_delete=models.SET_NULL, blank=True, null=True)
    dat_pe = models.DateField(blank=True, null=True)
    datv = models.DateField(blank=True, null=True)
    is_1c = models.BooleanField(blank=True,null=True,default=None)

class Vb_a(models.Model):
    id = models.BigAutoField(primary_key=True)
    datv = models.DateField(blank=True, null=True)
    srber = models.IntegerField(blank=True, null=True)
    pra = models.BooleanField(blank=True, null=True)
    pria = models.ForeignKey(Tip_pb, on_delete=models.SET_NULL, blank=True, null=True)
    m_prer = models.ForeignKey(Met_pb, on_delete=models.SET_NULL, blank=True, null=True)
    n_ber = models.IntegerField(blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Vds(models.Model):
    # сведения об оплате оказанной мед.помощи
    id = models.BigAutoField(primary_key=True)
    vds = models.ForeignKey(Isfin, on_delete=models.SET_NULL, blank=True, null=True)
    sctp = models.CharField(max_length=30, blank=True, null=True)
    nctp = models.CharField(max_length=30, blank=True, null=True)
    t_pol = models.ForeignKey(F008, on_delete=models.SET_NULL, blank=True, null=True)
    ctkom = models.ForeignKey(Skom, on_delete=models.SET_NULL, blank=True, null=True)
    ksg_ts = models.ForeignKey(T003, on_delete=models.SET_NULL, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Le_Vr(models.Model):
    # Сведения о койко-днях
    AroLet_CHOICES = [
        ('1', '1 - в течение 1 часа'),
        ('2', '2 - в течение 1 суток'),
        ('3', '3 - более чем через 1 сутки')
    ]
    id = models.BigAutoField(primary_key=True)
    kd = models.IntegerField(blank=True, null=True)
    aro = models.CharField(max_length=100, blank=True, null=True)
    # otd = models.ForeignKey(otde,on_delete=models.SET_NULL,blank=T003,null=True)
    otd = models.IntegerField(blank=True, null=True)
    kod = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True)
    spec = models.ForeignKey(V021, on_delete=models.SET_NULL, blank=True, null=True)
    prof_k = models.ForeignKey(V020, on_delete=models.SET_NULL, blank=True, null=True)
    pea = models.IntegerField(blank=True, null=True)
    kat1 = models.IntegerField(blank=True, null=True)
    kat2 = models.IntegerField(blank=True, null=True)
    kat3 = models.IntegerField(blank=True, null=True)
    datv = models.DateField(blank=True, null=True)
    prk = models.CharField(max_length=100, blank=True, null=True)
    #нахождения пациента в отд-ях анестез.и реанимации
    aro_n = models.IntegerField(blank=True,null=True)
    aro_let = models.CharField(max_length=1,choices=AroLet_CHOICES,blank=True,null=True)
    aro_sofa = models.BooleanField(blank=True,null=True)
    aro_ivl = models.BooleanField(blank=True,null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    kd_z = models.IntegerField(blank=True, null=True)

    def aro_let_display(self):
        return self.get_aro_let_display()



class Le_trv(models.Model):
    # Заполняется при определенных диагнозах и 1с
    id = models.BigAutoField(primary_key=True)
    t_trv = models.ForeignKey(Trv, on_delete=models.SET_NULL, blank=True, null=True, related_name='Trv')
    details = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='details')
    trav_ns = models.BooleanField(blank=True,null=True)
    # trav_ns = models.ForeignKey(Trvnas, on_delete=models.SET_NULL, blank=True, null=True)
    # trv_3 = models.BooleanField(default=None,blank=True,null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Oslo(models.Model):
    id = models.BigAutoField(primary_key=True)
    inf_oper = models.ForeignKey(V001, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='inf_oper')
    osl = models.ForeignKey(Pope, on_delete=models.SET_NULL, blank=True, null=True)
    xosl = models.ForeignKey(Xosl, on_delete=models.SET_NULL, blank=True, null=True)
    posl = models.ForeignKey(Posl, on_delete=models.SET_NULL, blank=True, null=True)
    aosl = models.ForeignKey(Aosl, on_delete=models.SET_NULL, blank=True, null=True)
    datp = models.DateField(blank=True, null=True)
    dato = models.DateField(blank=True, null=True)
    kopr = models.CharField(max_length=5, blank=True, null=True)
    datv = models.DateField(blank=True, null=True)
    tnvr = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Oper(models.Model):
    # Операции
    id = models.BigAutoField(primary_key=True)
    kodo = models.CharField(max_length=100, blank=True, null=True)
    kodx = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True, related_name='kodx')
    obz = models.ForeignKey(anesthesia, on_delete=models.SET_NULL,blank=True, null=True, related_name='obz', verbose_name='obz')
    obz_2 = models.ForeignKey(anesthesia, on_delete=models.SET_NULL,blank=True, null=True, related_name='obz_2', verbose_name='obz_2')
    koda = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True, related_name='koda')
    kods = models.IntegerField(blank=True, null=True)
    kodxa = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True, related_name='kodxa')
    kodxa1 = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True, related_name='kodxa1')
    kodan = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True, related_name='kodan')
    kopr = models.CharField(max_length=5, blank=True, null=True)
    datv = models.DateField(blank=True, null=True)
    goc = models.ForeignKey(V014, on_delete=models.SET_NULL,blank=True, null=True, related_name='goc_o')
    pop = models.BooleanField(default=False, blank=True, null=True)
    py = models.ForeignKey(PY, on_delete=models.SET_NULL,blank=True, null=True)
    kod_op = models.ForeignKey(V001, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='kod_op')
    pr_osob = models.ManyToManyField(PR_OSOB, blank=True)
    k_mm = models.CharField(max_length=100, blank=True, null=True)
    metobz = models.CharField(max_length=5, blank=True, null=True)
    dato = models.DateField(blank=True, null=True)
    tm_o = models.CharField(max_length=100, blank=True, null=True)
    oslo = models.ManyToManyField(Oslo, blank=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Manpy(models.Model):
    # Сведения о манипуляциях
    PL_CHOICES = [
        ('0', 'Неизвестно'),
        ('1', 'Да'),
        ('2', 'Нет')
    ]
    id = models.BigAutoField(primary_key=True)
    tnvr = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True)
    kodmn = models.ForeignKey(Ab_Obsh, on_delete=models.SET_NULL, blank=True, null=True)
    kopr = models.CharField(max_length=15, blank=True, null=True)
    datm = models.DateField(blank=True, null=True)
    datv = models.DateField(blank=True, null=True)
    kol = models.IntegerField(blank=True, null=True)
    py = models.ForeignKey(PY, on_delete=models.SET_NULL,blank=True, null=True)
    pl = models.CharField(max_length=15, choices=PL_CHOICES, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    def pl_display(self):
        return self.get_pl_display()

class Disability(models.Model):
    # Сведения о листе нетрудоспособности
    id = models.BigAutoField(primary_key=True)
    dat_l1 = models.DateField(blank=True, null=True)
    dat_l2 = models.DateField(blank=True, null=True)
    ot_ln = models.BooleanField(blank=True, null=True)
    vs_bol = models.IntegerField(blank=True, null=True)
    sex_bol = models.ForeignKey(V005, on_delete=models.SET_NULL, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Napr(models.Model):
    id = models.BigAutoField(primary_key=True)
    naprdate = models.DateField(blank=True, null=True)
    napr_mo = models.ForeignKey(F003, on_delete=models.SET_NULL, blank=True, null=True)
    napr_v = models.ForeignKey(V028, on_delete=models.SET_NULL, blank=True, null=True)
    napr_issl = models.ForeignKey(V029, on_delete=models.SET_NULL, blank=True, null=True)
    napr_usl = models.ForeignKey(V001, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='napr_usl')
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Cons(models.Model):
    id = models.BigAutoField(primary_key=True)
    pr_cons = models.ForeignKey(N019, on_delete=models.SET_NULL, blank=True, null=True)
    dt_cons = models.DateField(blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Onk_sl(models.Model):
    MTSTZ_CHOICES = [
        ('1','впервые'),
        ('2','ранее')
    ]
    id = models.BigAutoField(primary_key=True)
    ds1_t = models.ForeignKey(N018, on_delete=models.SET_NULL, blank=True, null=True)
    stad = models.ForeignKey(N002, on_delete=models.SET_NULL, blank=True, null=True)
    onk_t = models.ForeignKey(N003, on_delete=models.SET_NULL, blank=True, null=True)
    onk_n = models.ForeignKey(N004, on_delete=models.SET_NULL, blank=True, null=True)
    onk_m = models.ForeignKey(N005, on_delete=models.SET_NULL, blank=True, null=True)
    mtstz = models.CharField(max_length=1,choices=MTSTZ_CHOICES,blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    def mtstz_display(self):
        return  self.get_mtstz_display()

class B_diag(models.Model):
    DIAG_TIP_CHOICES = [
        ('1', 'Гистологический признак'),
        ('2', 'Маркёр (ИГХ)')
    ]
    id = models.BigAutoField(primary_key=True)
    diag_date = models.DateField(blank=True, null=True)
    diag_tip = models.CharField(max_length=1, choices=DIAG_TIP_CHOICES, blank=True, null=True)
    diag_code = models.CharField(max_length=255, blank=True, null=True)
    diag_rslt = models.CharField(max_length=255, blank=True, null=True)
    rec_rslt = models.IntegerField(blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    def diag_tip_display(self):
        return self.get_diag_tip_display()

class B_prot(models.Model):
    id = models.BigAutoField(primary_key=True)
    prot = models.ForeignKey(N001, on_delete=models.SET_NULL, blank=True, null=True)
    d_prot = models.DateField(blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
class Onk_usl(models.Model):
    id = models.BigAutoField(primary_key=True)
    usl_tip = models.ForeignKey(N013, on_delete=models.SET_NULL, blank=True, null=True)
    hir_tip = models.ForeignKey(N014, on_delete=models.SET_NULL, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

class Ksg_kpg(models.Model):
    id = models.BigAutoField(primary_key=True)
    ksg_in = models.ForeignKey(V023, on_delete=models.SET_NULL, blank=True, null=True)
    ksg_ins = models.CharField(max_length=8, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
class Onmk_sp(models.Model):
    P001_CHOICES = [
        ('1', 'г.Тюмень'),
        ('2', 'Тюменский р-н'),
        ('3', 'Ярковский р-н'),
        ('4', 'Нижнетавдинский р-н'),
        ('5', 'Житель других районов ТО'),
        ('6', 'Другие регионы РФ'),
        ('7', 'Житель другого государства'),
    ]
    P002_CHOICES = [
        ('1', 'СМП'),
        ('2', 'Направление территориальной поликлиники'),
        ('3', 'Перевод из другого стационараг. Тюмени'),
        ('4', 'Перевод из ПСО 1.  ГБУЗ ТО "ОБ№3" г. Тобольск'),
        ('5', 'Перевод из ПСО 2. ГБУЗ ТО "ОБ №4" г. Ишим'),
        ('6', 'Перевод из ПСО 3. ГБУЗ ТО "ОБ №23"г. Ялуторовск'),
        ('7', 'Перевод из отделений ОКБ 2'),
        ('8', 'Самообращение')
    ]
    P003_CHOICES = [
        ('1', 'Транзиторная ишемическая атака (ТИА) МКБ10  G45-46'),
        ('2', 'Ишемический инсульт МКБ10  I63'),
        ('3', 'Субарахноидальное кровоизлияние (САК) МКБ10 - I60'),
        ('4', 'Внутримозговое кровоизлияние (ВМК) МКБ10 - I61'),
        ('5', 'Другое внутричерепное кровоизлияние МКБ10 - I62'),
        ('6', 'Сочетание САК и ВМК')
    ]
    P004_CHOICES = [
        ('1', 'Первичный'),
        ('2', 'Повторный (анамнестически)'),
        ('3', 'Повторный (подтвержден документально)')
    ]

    P005_CHOICES = [
        ('1', 'до 3 часов'),
        ('2', 'от 3 до 4,5 часов'),
        ('3', 'от 4,5 до 6 часов'),
        ('4', 'от 6 до 9 часов'),
        ('5', 'от 9 до 12 часов'),
        ('6', 'от 12 до 24 часов'),
    ]

    P005_2_CHOICES = [
        ('0', 'Да'),
        ('1', 'Нет'),

    ]

    P006_CHOICES = [
        ('1', 'ТЛТ проводилась'),
        ('2', 'ТЛТ не проводилась (зафиксированы противопоказания)'),
        ('3', 'ТЛТ не проводилась (другие причины)')
    ]

    P007_CHOICES = [
        ('1', 'В первые 40 минут от момента поступления'),
        ('2', 'После 40 минут')
    ]

    P008_CHOICES = [
        ('1', 'Да'),
        ('2', 'Нет')
    ]

    P009_CHOICES = [
        ('1', 'В первые 3 часа с момента поступления в отделение'),
        ('2', 'От 3 часов до 24 часов с момента поступления в отделение'),
        ('3', 'После 24 часов с момента поступления в отделение')
    ]

    P010_CHOICES = [
        ('1', 'Каротидный бассейн'),
        ('2', 'Вертебробазилярный бассейн (ВББ)')
    ]

    P011_CHOICES = [
        ('1', 'Атеротромботический (тромбоэмболический)'),
        ('2', 'Кардиоэмболический'),
        ('3', 'Лакунарный'),
        ('4', 'Другой уточненный'),
        ('5', 'Неуточненный (криптогенный)')
    ]

    P012_CHOICES = [
        ('1', 'Группа антиагрегантов при некардиоэмболическом варианте инсульта или ТИА'),
        ('2', 'Группа антикоагулянтов при кардиоэмболическом варианте инсульта или ТИА')
    ]

    P013_CHOICES = [
        ('1', '0 баллов'),
        ('2', '1 балл'),
        ('3', '2 балла'),
        ('4', '3 балла'),
        ('5', '4 балла'),
        ('6', '5 балла'),
    ]

    P014_CHOICES = [
        ('1', '0 баллов'),
        ('2', '1 балл'),
        ('3', '2 балла'),
        ('4', '3 балла'),
        ('5', '4 балла'),
        ('6', '5 балла'),
        ('7', '6 балла'),
    ]

    P015_CHOICES = [
        ('1', 'Пневмония'),
        ('2', 'Пролежни'),
        ('3', 'ТЭЛА')
    ]

    P016_CHOICES = [
        ('1', 'Выписан и направлен на хирургическое лечение в отделение сосудистой хирургии'),
        ('2', 'Переведен на 2 этап реабилитации в ЛРЦ'),
        ('3', 'Переведен на 3 этап реабилитации'),
        ('4', 'Выписан на амбулаторный этап реабилитации'),
        ('5', 'Переведен в больницу сестринского ухода'),
        ('6', 'Летальный исход'),
        ('7', 'Летальный исход у больного после проведения ТЛТ')
    ]

    id = models.BigAutoField(primary_key=True)
    datv = models.DateField(blank=True, null=True)
    dats = models.DateField(blank=True, null=True)
    datz = models.DateField(blank=True, null=True)
    kop_s = models.CharField(max_length=5, blank=True, null=True)
    ball_n = models.CharField(max_length=1, blank=True, null=True)
    p001 = models.CharField(max_length=1, choices=P001_CHOICES, blank=True, null=True)
    p002 = models.CharField(max_length=1, choices=P002_CHOICES, blank=True, null=True)
    p003 = models.CharField(max_length=1, choices=P003_CHOICES, blank=True, null=True)
    p004 = models.CharField(max_length=1, choices=P004_CHOICES, blank=True, null=True)
    p005_1 = models.CharField(max_length=1, choices=P005_CHOICES, blank=True, null=True)
    p005_2 = models.CharField(max_length=1, choices=P005_2_CHOICES, blank=True, null=True)
    p006 = models.CharField(max_length=1, choices=P006_CHOICES, blank=True, null=True)
    p007 = models.CharField(max_length=1, choices=P007_CHOICES, blank=True, null=True)
    p008 = models.CharField(max_length=1, choices=P008_CHOICES, blank=True, null=True)
    p009 = models.CharField(max_length=1, choices=P009_CHOICES, blank=True, null=True)
    p010 = models.CharField(max_length=1, choices=P010_CHOICES, blank=True, null=True)
    p011 = models.CharField(max_length=1, choices=P011_CHOICES, blank=True, null=True)
    p012 = models.CharField(max_length=1, choices=P012_CHOICES, blank=True, null=True)
    p013 = models.CharField(max_length=1, choices=P013_CHOICES, blank=True, null=True)
    p014 = models.CharField(max_length=1, choices=P014_CHOICES, blank=True, null=True)
    p015 = models.CharField(max_length=1, choices=P015_CHOICES, blank=True, null=True)
    p016 = models.CharField(max_length=1, choices=P016_CHOICES, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
class Onmk_li(models.Model):
    P001_CHOICES = [
        ('1', 'Ишемический'),
        ('2', 'Геморрагический')
    ]

    P002_CHOICES = [
        ('1', 'Первичный'),
        ('2', 'Повторный (анамнестически)'),
        ('3', 'Повторный (подтвержден документально)')
    ]

    P003_CHOICES = [
        ('1', 'До 20 лет'),
        ('2', '20 - 29 лет'),
        ('3', '30 - 39 лет'),
        ('4', '40 - 49 лет'),
        ('5', '50 - 59 лет'),
        ('6', '60 - 69 лет'),
        ('7', '79 - 79 лет'),
        ('8', '80 и старше')
    ]

    P004_CHOICES = [
        ('1', 'Менее суток'),
        ('2', '>1 <= 3 суток'),
        ('3', '>3 <= 5 суток'),
        ('4', '>5 <= 7 суток'),
        ('5', '>7 <= 10 суток'),
        ('6', '30 и более суток')
    ]

    P005_CHOICES = [
        ('1', 'до 4.5 часов'),
        ('2', 'от 4.5 до 6 часов'),
        ('3', 'от 6 до 12 часов'),
        ('4', 'от 12 до 24 часов'),
        ('5', 'более 24 часов')
    ]

    P006_CHOICES = [
        ('1', '15'),
        ('2', '14 - 13'),
        ('3', '12 - 11'),
        ('4', '10 - 9'),
        ('5', '8 - 3')
    ]

    P007_CHOICES = [
        ('1', 'Каротидный бассейн - территория более 1/3 СМА'),
        ('2', 'ВББ - очаг стволовой локализации или вторичная окклюзионная гидроцефалия')
    ]

    P008_CHOICES = [
        ('1', 'Объем кровоизлияния более 50 мл'),
        ('2', 'Прорыв крови в желудочки мозга'),
        ('3', 'Кровоизлияние в стволовые отделы'),
        ('4', 'Для САК - тяжесть по Н-Н 4 - 5 баллов')
    ]

    P009_CHOICES = [
        ('1', 'Не проводилась'),
        ('2', 'Проводилась (без динамики)'),
        ('3', 'Проводилась (динамика отрицательная)')
    ]

    P010_CHOICES = [
        ('1', 'Да'),
        ('2', 'Нет')
    ]

    P011_CHOICES = [
        ('1', 'В 1 сутки от момента поступления'),
        ('2', 'На 2 - 3 сутки от момента поступления'),
        ('3', 'Более 3-х суток от момента поступления')
    ]

    P012_CHOICES = [
        ('1', 'В первые 3 часа с момента поступления в отделение'),
        ('2', 'После 3 часов до 24 часов с момента поступления в отделение'),
        ('3', 'После 24 часов с момента поступления'),
        ('4', 'ДСЭКА не проводилось')
    ]

    P013_CHOICES = [
        ('1', 'Да'),
        ('2', 'Нет (имелись противопоказания)'),
        ('3', 'Нет (другие причины)')
    ]

    P014_CHOICES = [
        ('1', 'до 1 суток'),
        ('2', 'от 1 до 2 суток'),
        ('3', 'от 3 до 7 суток'),
        ('4', 'более 7 суток')
    ]

    P015_CHOICES = [
        ('1', '1 - 3 сутки'),
        ('2', '4 - 5 суток'),
        ('3', '6 - 7 суток'),
        ('4', '7 - 10 суток'),
        ('5', 'Более 10 суток')
    ]

    P016_CHOICES = [
        ('1', 'Дислокационный синдром (подтверждено клинически +КТ/МРТ)'),
        ('2', 'Геморрагическая трансформация при ишемическом инсульте'),
        ('3', 'Рецидив кровоизлияния при САК или ВМК'),
        ('4', 'Повторный ишемический инсульт (подтверждено клинически + КТ/МРТ)'),
        ('5', 'Менингоэнцефалит'),
        ('6', 'Пневмония'),
        ('7', 'Пролежни'),
        ('8', 'ЖКК'),
        ('9', 'ТГВ'),
        ('10', 'ТЭЛА'),
        ('11', 'Урологическая инфекция'),
        ('12', 'Сепсис'),
        ('13', 'Пневмоторакс'),
        ('14', 'Падение с травмой (перелом шейки бедра, ЧМТ)'),
        ('15', 'Другое (указать)')
    ]

    P017_CHOICES = [
        ('1', 'Отделение анестезиологии и реанимации'),
        ('2', 'Неврологическое отделение')
    ]

    P018_CHOICES = [
        ('1', 'Рабочие дни, основные рабочие часы персонала (пн.-пт., 8-00 - 16-00)'),
        ('2', 'Рабочие дни, дежурные часы (пн.-чт.,16-01 - 7-59)'),
        ('3', 'Выходные и праздничные дни (с 16-01 пт. по 8-00 пн.)')
    ]

    P019_CHOICES = [
        ('1', 'Да (зафиксирован в медицинской карте стационарного больного)'),
        ('2', 'Нет (внезапная смерть)')
    ]

    P020_CHOICES = [
        ('1', 'Своевременно'),
        ('2', 'Не своевременно'),
        ('3', 'Отсутствует')
    ]

    P021_CHOICES = [
        ('1', 'Вскрытие не проводилось по заявлению родственников и в соответствии с ФЗ 323'),
        ('2', 'Вскрытие проводилось (совпадение диагнозов) - указать код МКБ10 из протокола вскрытия ____'),
        ('3', 'Вскрытие проводилось (расхождение диагнозов)- указать код МКБ10 из протокола вскрытия ___')
    ]

    P022_CHOICES = [
        ('1', 'Сахарный диабет'),
        ('2', 'Злокачественные новообразования'),
        ('3', 'ИБС. ПИКС, ХСН'),
        ('4', 'Инфаркт миокарда, ОКС'),
        ('5', 'Цирроз печени'),
        ('6', 'Критическая ишемия конечностей'),
        ('7', 'Нарушение мезентериального кровообращения'),
        ('8', 'Бронхиальная астма')
    ]

    P023_CHOICES = [
        ('1', 'Да, информация предоставлялась'),
        ('2', 'Нет, информация не предоставлялась')
    ]

    p001 = models.CharField(max_length=1, choices=P001_CHOICES, blank=True, null=True)
    p002 = models.CharField(max_length=1, choices=P002_CHOICES, blank=True, null=True)
    p003 = models.CharField(max_length=1, choices=P003_CHOICES, blank=True, null=True)
    p004 = models.CharField(max_length=1, choices=P004_CHOICES, blank=True, null=True)
    p005 = models.CharField(max_length=1, choices=P005_CHOICES, blank=True, null=True)
    p006 = models.CharField(max_length=1, choices=P006_CHOICES, blank=True, null=True)
    p007 = models.CharField(max_length=1, choices=P007_CHOICES, blank=True, null=True)
    p008 = models.CharField(max_length=1, choices=P008_CHOICES, blank=True, null=True)
    p009 = models.CharField(max_length=1, choices=P009_CHOICES, blank=True, null=True)
    p010 = models.CharField(max_length=1, choices=P010_CHOICES, blank=True, null=True)
    p011 = models.CharField(max_length=1, choices=P011_CHOICES, blank=True, null=True)
    p012 = models.CharField(max_length=1, choices=P012_CHOICES, blank=True, null=True)
    p013 = models.CharField(max_length=1, choices=P013_CHOICES, blank=True, null=True)
    p014 = models.CharField(max_length=1, choices=P014_CHOICES, blank=True, null=True)
    p015 = models.CharField(max_length=1, choices=P015_CHOICES, blank=True, null=True)
    p016 = models.CharField(max_length=2, choices=P016_CHOICES, blank=True, null=True)
    p017 = models.CharField(max_length=1, choices=P017_CHOICES, blank=True, null=True)
    p018 = models.CharField(max_length=1, choices=P018_CHOICES, blank=True, null=True)
    p019 = models.CharField(max_length=1, choices=P019_CHOICES, blank=True, null=True)
    p020 = models.CharField(max_length=1, choices=P020_CHOICES, blank=True, null=True)
    p021 = models.CharField(max_length=1, choices=P021_CHOICES, blank=True, null=True)
    p022 = models.CharField(max_length=1, choices=P022_CHOICES, blank=True, null=True)
    p023 = models.CharField(max_length=1, choices=P023_CHOICES, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)

#Имплатны
class Med_dev(models.Model):
    date = models.DateField(blank=True,null=True)
    code = models.ForeignKey(Code_med_dev,on_delete=models.SET_NULL,blank=True,null=True)
    number_ser = models.CharField(max_length=100,blank=True,null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    def __str__(self):
        return f'{self.date} - {self.code} - {self.number_ser}'

class Sluchay(models.Model):
    # Сведения о пребывании в стационаре (случай)
    TIP_WSK_CHOICES = [
        ('1', 'без вскрытия'),
        ('2', 'патологоанатом.'),
        ('3', 'судебное')
    ]
    RASX_CHOICES = [
        ('1', 'Да'),
        ('2', 'Нет')
    ]

    ALG_CHOICES = [
        ('1', 'Нет'),
        ('2', 'Алкогольное'),
        ('3', 'Наркотическое')
    ]

    TipOMC_CHOICES = [
        ('1', 'Базовая'),
        ('2', 'Высок/Св.баз.'),
    ]

    id = models.BigAutoField(primary_key=True)
    nib = models.CharField(max_length=20, blank=True, null=True)
    datp = models.DateField(blank=True, null=True)
    datv = models.DateField(blank=True, null=True)
    goc = models.ForeignKey(V014, on_delete=models.SET_NULL, blank=True, null=True)
    prpg = models.ForeignKey(Prpg, on_delete=models.SET_NULL, blank=True, null=True)
    vrez = models.ForeignKey(Vrzb, on_delete=models.SET_NULL, blank=True, null=True)
    lpy = models.ForeignKey(F003, on_delete=models.SET_NULL,blank=True, null=True, related_name='lpy')
    ws = models.ForeignKey(Ws, on_delete=models.SET_NULL,blank=True, null=True)
    tm_otd = models.CharField(max_length=100, blank=True, null=True)
    tm_otd_1 = models.CharField(max_length=100, blank=True, null=True)
    iddokt = models.ForeignKey(Vra, on_delete=models.SET_NULL, blank=True, null=True, related_name='iddokt')
    otd = models.ForeignKey(otde, on_delete=models.SET_NULL, blank=True, null=True)
    icx = models.ForeignKey(V012, on_delete=models.SET_NULL, blank=True, null=True)
    pmg = models.ForeignKey(F003, on_delete=models.SET_NULL,blank=True, null=True, related_name='pmg')
    dsny = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='dsny')
    dsk = models.ForeignKey(Ds, on_delete=models.SET_NULL,blank=True, null=True, related_name='dsk')
    dskz = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='dskz')
    dskz2 = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='dskz2')
    dsc = models.ForeignKey(Ds, on_delete=models.SET_NULL,blank=True, null=True, related_name='dsc')
    ds_osl = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='ds_osl')
    dson = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='dson')
    ksg_osn = models.ForeignKey(group_kc_group, on_delete=models.SET_NULL, blank=True, null=True, related_name='ksg_osn')
    ksg_sop = models.ForeignKey(group_kc_group, on_delete=models.SET_NULL, blank=True, null=True, related_name='ksg_sop')
    oopkk = models.ForeignKey(group_kc_dkk, on_delete=models.SET_NULL, blank=True, null=True, related_name='oopkk')
    id_vid_hmp = models.CharField(max_length=100, blank=True, null=True)
    vid_hmp = models.CharField(max_length=100, blank=True, null=True)
    id_metod_hmp = models.CharField(max_length=100, blank=True, null=True)
    metod_hmp = models.CharField(max_length=100, blank=True, null=True)
    vb_s = models.ManyToManyField(Vb_s, blank=True)
    dspat = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='dspat')
    pri = models.ForeignKey(Prli, on_delete=models.SET_NULL, blank=True, null=True)
    trav = models.CharField(max_length=2, blank=True, null=True)
    le_vr = models.OneToOneField(Le_Vr, on_delete=models.SET_NULL, blank=True, null=True)
    alg = models.CharField(max_length=1, choices=ALG_CHOICES, blank=True, null=True)
    ps = models.CharField(max_length=1, blank=True, null=True)
    le_trv = models.OneToOneField(Le_trv, on_delete=models.SET_NULL, blank=True, null=True)
    lv = models.IntegerField(blank=True, null=True)
    oper = models.ManyToManyField(Oper, blank=True)
    manpy = models.ManyToManyField(Manpy, blank=True)
    disability = models.OneToOneField(Disability, on_delete=models.SET_NULL, blank=True, null=True)
    vds = models.OneToOneField(Vds, on_delete=models.SET_NULL, blank=True, null=True,related_name='sl')
    trs = models.ForeignKey(Trs, on_delete=models.SET_NULL, blank=True, null=True)
    rasx = models.CharField(max_length=1, choices=RASX_CHOICES, blank=True, null=True)
    tup = models.CharField(max_length=5, blank=True, null=True)
    dspo = models.CharField(max_length=60, blank=True, null=True)
    vr = models.CharField(max_length=5, blank=True, null=True)
    dat_s = models.DateField(blank=True, null=True)
    z_of = models.CharField(max_length=1, blank=True, null=True)
    otd_y = models.ForeignKey(otde, on_delete=models.SET_NULL, blank=True, null=True, related_name='otd_y')
    admt = models.CharField(max_length=2, blank=True, null=True)
    profz = models.CharField(max_length=3, blank=True, null=True)
    kod_otd = models.CharField(max_length=3, blank=True, null=True)
    osibka = models.CharField(max_length=1, blank=True, null=True)
    tipst = models.CharField(max_length=1, blank=True, null=True)
    tm = models.CharField(max_length=5, blank=True, null=True)
    wskr = models.CharField(max_length=1, choices=TIP_WSK_CHOICES, blank=True, null=True)
    wskr_date = models.CharField(max_length=100, blank=True, null=True)
    rasxp = models.CharField(max_length=1, choices=RASX_CHOICES, blank=True, null=True)
    dat_ot = models.DateField(blank=True, null=True)
    tm_let = models.CharField(max_length=100, blank=True, null=True)
    otm_tfoms = models.CharField(max_length=1, blank=True, null=True)
    otm_w = models.CharField(max_length=1, blank=True, null=True)
    dat_otd = models.DateField(blank=True, null=True)
    ds_oms = models.CharField(max_length=7, blank=True, null=True)
    check_tf = models.CharField(max_length=2, blank=True, null=True)
    dsc_r = models.CharField(max_length=7, blank=True, null=True)
    tnvr_r = models.CharField(max_length=5, blank=True, null=True)
    ds_let = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='ds_let')
    min_po = models.IntegerField(blank=True, null=True)
    n_ib = models.CharField(max_length=15, blank=True, null=True)
    npr_num = models.CharField(max_length=20, blank=True, null=True)
    npr_date = models.DateField(blank=True, null=True)
    ds_0 = models.ForeignKey(Ds, on_delete=models.SET_NULL, blank=True, null=True, related_name='ds_0')
    npl = models.CharField(max_length=1, blank=True, null=True)
    k_npl = models.DecimalField(decimal_places=4, max_digits=4, blank=True, null=True)
    nib_1c = models.CharField(max_length=20, blank=True, null=True)
    rslt = models.ForeignKey(V009, on_delete=models.SET_NULL, blank=True, null=True)
    p_per = models.ForeignKey(PER, on_delete=models.SET_NULL, blank=True, null=True)
    ds_onk = models.CharField(max_length=1, blank=True, null=True)
    onk_sl = models.OneToOneField(Onk_sl, on_delete=models.SET_NULL, blank=True, null=True)
    b_diag = models.OneToOneField(B_diag, on_delete=models.SET_NULL, blank=True, null=True)   
    b_prot = models.OneToOneField(B_prot, on_delete=models.SET_NULL, blank=True, null=True)
    cons = models.OneToOneField(Cons, on_delete=models.SET_NULL, blank=True, null=True)
    onk_usl = models.OneToOneField(Onk_usl, on_delete=models.SET_NULL, blank=True, null=True)
    c_zab = models.ForeignKey(V027, on_delete=models.SET_NULL, blank=True, null=True)
    sumv = models.DecimalField(decimal_places=13, max_digits=13, blank=True, null=True)
    onk_1_2 = models.CharField(max_length=1, blank=True, null=True)
    gwf = models.IntegerField(blank=True, null=True)
    u_gwf = models.CharField(max_length=100, blank=True, null=True)
    sofa = models.CharField(max_length=100, blank=True, null=True)
    iwl = models.CharField(max_length=100, blank=True, null=True)
    ksg_kpg = models.ManyToManyField(Ksg_kpg, blank=True)
    code_usl = models.ForeignKey(T003, on_delete=models.SET_NULL, blank=True, null=True, related_name='code_usl')
    code_usl_vt = models.ForeignKey(Tar_vt, on_delete=models.SET_NULL, blank=True, null=True, related_name='code_usl_vt')
    napr = models.OneToOneField(Napr, on_delete=models.SET_NULL, blank=True, null=True)
    adr_fakt = models.CharField(max_length=100, blank=True, null=True)
    vb_a = models.OneToOneField(Vb_a, on_delete=models.SET_NULL, blank=True, null=True)
    onmk_sp = models.OneToOneField(Onmk_sp, on_delete=models.SET_NULL, blank=True, null=True)
    onmk_li = models.OneToOneField(Onmk_li, on_delete=models.SET_NULL, blank=True, null=True)
    add_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='add_user')
    update_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='update_user')
    statistics_type = models.ForeignKey(Statistics_type, on_delete=models.SET_NULL, blank=True, null=True)
    tip_oms = models.CharField(max_length=1,choices=TipOMC_CHOICES,blank=True,null=True)
    med_dev = models.ManyToManyField(Med_dev,blank=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    usl_ok = models.IntegerField(blank=True, null=True, default=None)
    vidpom = models.IntegerField(blank=True, null=True, default=None)
    lpu_1 = models.CharField(max_length=8, blank=True, null=True)
    podr = models.CharField(max_length=12, blank=True, null=True)
    det = models.IntegerField(blank=True, null=True)
    tal_d = models.DateField(blank=True, null=True)
    tal_p = models.DateField(blank=True,null=True)
    tal_num = models.CharField(max_length=20,blank=True,null=True)
    ds2 = models.CharField(max_length=100,blank=True,null=True)
    ds2_n = models.CharField(max_length=100, blank=True, null=True)
    ds3 = models.CharField(max_length=100, blank=True, null=True)
    code_mes1 = models.CharField(max_length=20,blank=True,null=True)
    code_mes2 = models.CharField(max_length=20, blank=True, null=True)
    idsp = models.IntegerField(blank=True, null=True)
    ed_col = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    kol_usl = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    crit = models.CharField(max_length=254,blank=True,null=True)
    n_ksg = models.CharField(max_length=20,blank=True,null=True)
    vb_p = models.IntegerField(blank=True,null=True)
    reab = models.IntegerField(blank=True,null=True)
    dn = models.IntegerField(blank=True,null=True)
    p_cel = models.CharField(max_length=3,blank=True,null=True)
    profil_k = models.IntegerField(blank=True,null=True)
    err = models.BooleanField(default=False)
    err_text = models.TextField(blank=True,null=True)
    oslo = models.ManyToManyField(Oslo,blank=True)

    def alg_display(self):
        return self.get_alg_display()

    def wskr_display(self):
        return self.get_wskr_display()

    def rasxp_display(self):
        return self.get_rasxp_display()

class Patient_P(models.Model):
    # Сведения о представителе пациента
    id = models.BigAutoField(primary_key=True)
    fam_p = models.CharField(max_length=80, blank=True, null=True)
    im_p = models.CharField(max_length=80, blank=True, null=True)
    ot_p = models.CharField(max_length=80, blank=True, null=True)
    pol = models.ForeignKey(V005, on_delete=models.SET_NULL, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    s_pasp = models.CharField(max_length=100, blank=True, null=True)
    n_pasp = models.CharField(max_length=20, blank=True, null=True)
    m_roj = models.CharField(max_length=200, blank=True, null=True)
    udl_p = models.ForeignKey(F011, on_delete=models.SET_NULL, blank=True, null=True)
    sp_pasp = models.CharField(max_length=30, blank=True, null=True)
    np_pasp = models.CharField(max_length=30, blank=True, null=True)
    skom_p = models.ForeignKey(Skom, on_delete=models.SET_NULL, blank=True, null=True)
    stat_p = models.ForeignKey(F008, on_delete=models.SET_NULL, blank=True, null=True)
    s_pol = models.CharField(max_length=25, blank=True, null=True)
    n_pol = models.CharField(max_length=25, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    dr = models.DateField(blank=True, null=True)
    udl = models.CharField(max_length=2, blank=True, null=True)
    okatog = models.CharField(max_length=50, blank=True, null=True)
    okatop = models.CharField(max_length=50, blank=True, null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
class Patient(models.Model):
    # Сведения о пациенте
    RPR_CHOICES = [
        ('1', 'Центральный АО'),
        ('2', 'Ленинский АО'),
        ('3', 'Калининский АО'),
        ('4', 'Восточный АО')
    ]
    id = models.BigAutoField(primary_key=True)
    fam = models.CharField(max_length=80, blank=True, null=True)
    im = models.CharField(max_length=80, blank=True, null=True)
    ot = models.CharField(max_length=80, blank=True, null=True)
    pol = models.ForeignKey(V005, on_delete=models.SET_NULL, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    vs = models.IntegerField(blank=True, null=True)
    nvs = models.CharField(max_length=1, blank=True, null=True)
    udl = models.ForeignKey(F011, on_delete=models.SET_NULL, blank=True, null=True)
    s_pasp = models.CharField(max_length=30, blank=True, null=True)
    n_pasp = models.CharField(max_length=30, blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    docorg = models.CharField(max_length=200, blank=True, null=True)
    ss = models.CharField(max_length=14, blank=True, null=True)
    c_oksm = models.ForeignKey(Oksm, on_delete=models.SET_NULL, blank=True, null=True)
    adr = models.CharField(max_length=200, blank=True, null=True)
    rkod = models.CharField(max_length=1, blank=True, null=True)
    ylc = models.CharField(max_length=25, blank=True, null=True)
    dom = models.CharField(max_length=7, blank=True, null=True)
    kv = models.CharField(max_length=7, blank=True, null=True)
    kp = models.CharField(max_length=100, blank=True, null=True)
    stro = models.CharField(max_length=100, blank=True, null=True)
    m_roj = models.CharField(max_length=200, blank=True, null=True)
    rai = models.CharField(max_length=1, choices=RPR_CHOICES, blank=True, null=True)
    cj = models.ForeignKey(CJ, on_delete=models.SET_NULL,blank=True, null=True)
    v_lgoty = models.ForeignKey(V_LGOTY, on_delete=models.SET_NULL, blank=True, null=True)
    in_t = models.ForeignKey(T004, on_delete=models.SET_NULL, blank=True, null=True)
    rab = models.CharField(max_length=200, blank=True, null=True)
    r_n = models.ForeignKey(Rab_Ner, on_delete=models.SET_NULL, blank=True, null=True)
    prof = models.CharField(max_length=150, blank=True, null=True)
    vec = models.CharField(max_length=100, blank=True, null=True)
    patient_p = models.OneToOneField(Patient_P, on_delete=models.SET_NULL, blank=True, null=True)
    sluchay = models.ManyToManyField(Sluchay, blank=True,related_name='patient')
    r_name = models.CharField(max_length=30, blank=True, null=True)
    np_name = models.CharField(max_length=30, blank=True, null=True)
    gor_name = models.CharField(max_length=30, blank=True, null=True)
    ul_name = models.CharField(max_length=30, blank=True, null=True)
    cod_adr = models.CharField(max_length=30, blank=True, null=True)
    datnp = models.DateField(blank=True, null=True)
    datkp = models.DateField(blank=True, null=True)
    reg_name = models.CharField(max_length=30, blank=True, null=True)
    okatog = models.CharField(max_length=50,blank=True,null=True)
    okatop = models.CharField(max_length=50,blank=True,null=True)
    is_1c = models.BooleanField(blank=True, null=True, default=None)
    tel = models.CharField(max_length=100,blank=True,null=True)
    novor = models.CharField(max_length=9, blank=True, null=True)



    # def __str__(self):
    #     return str(self.sluchay.values('nib')[0]['nib'])

    def rai_display(self):
        return self.get_rai_display()


class qweqwe(models.Model):
    text = models.CharField(max_length=1,blank=True,null=True)


class otdl7(models.Model):
    OTD = models.ForeignKey(otde,on_delete=models.SET_NULL,blank=True,null=True)
    IM1 = models.CharField(max_length=100,blank=True,null=True)
    PR_OTD = models.CharField(max_length=10,blank=True,null=True)
    FK = models.IntegerField(default=0,blank=True)
    KODI = models.CharField(max_length=10,blank=True,null=True)
    FK_MZ = models.IntegerField(default=0,blank=True)
    FK_R = models.IntegerField(default=0,blank=True)
    K_SR = models.IntegerField(default=0,blank=True)
    K_D_R = models.IntegerField(default=0,blank=True)
    N_KD = models.IntegerField(default=0,blank=True)
    tipe = models.IntegerField(default=0,blank=True)

class umer7(models.Model):
    DAT = models.DateField(blank=True,null=True)
    OTD = models.ForeignKey(otdl7,on_delete=models.SET_NULL,blank=True,null=True)
    FAM = models.CharField(max_length=100,blank=True,null=True)
    UMA = models.IntegerField(default=0,blank=True)
    UM1 = models.IntegerField(default=0,blank=True)
    UMS = models.IntegerField(default=0,blank=True)
    UMAR = models.IntegerField(default=0,blank=True)
    UM1G = models.IntegerField(default=0,blank=True)
    PROF = models.ForeignKey(V020,on_delete=models.SET_NULL,blank=True,null=True)

class form7(models.Model):
    DAT = models.DateField(blank=True,null=True)
    OTD = models.ForeignKey(otdl7,on_delete=models.SET_NULL,blank=True,null=True)
    PROF = models.ForeignKey(V020,on_delete=models.SET_NULL,blank=True,null=True)
    PR_OTD = models.CharField(max_length=10,blank=True,null=True)
    TIP = models.IntegerField(default=0,blank=True)
    F_K = models.IntegerField(default=0,blank=True)
    #4
    NALNN = models.IntegerField(default=0,blank=True)
    #4/1
    NALNA = models.IntegerField(default=0,blank=True)
    #4/2
    NALNR = models.IntegerField(default=0,blank=True)
    #5
    POST = models.IntegerField(default=0,blank=True)
    #5/2
    POSTSG = models.IntegerField(default=0,blank=True)
    #5/4
    POST14 = models.IntegerField(default=0,blank=True)
    POST15 = models.IntegerField(default=0,blank=True)
    POST60 = models.IntegerField(default=0,blank=True)
    #5/3
    POST1 = models.IntegerField(default=0,blank=True)
    #6/7
    PERIZ = models.IntegerField(default=0,blank=True)
    #6/1
    PERAN = models.IntegerField(default=0,blank=True)
    PERW = models.IntegerField(default=0,blank=True)
    PERWAN = models.IntegerField(default=0,blank=True)
    WIP = models.IntegerField(default=0,blank=True)
    UM = models.IntegerField(default=0,blank=True)
    #4#5  # 6/1 + 6/4 + 6/7  
    NALNK = models.IntegerField(default=0,blank=True)
    #4/1 (-#6/1)
    NALKA = models.IntegerField(default=0,blank=True)
    

    MUT = models.IntegerField(default=0,blank=True)
    MUT3 = models.IntegerField(default=0,blank=True)

    PERWR = models.IntegerField(default=0,blank=True)
    #6/4
    PERR = models.IntegerField(default=0,blank=True)
    #4/2 #-6/4
    NALKR = models.IntegerField(default=0,blank=True)
    PERWANE = models.IntegerField(default=0,blank=True)
    PERWRE = models.IntegerField(default=0,blank=True)
    UMA = models.IntegerField(default=0,blank=True)
    UMAR = models.IntegerField(default=0,blank=True)
    UMA1 = models.IntegerField(default=0,blank=True)
    UMAR1 = models.IntegerField(default=0,blank=True)
    UMAE = models.IntegerField(default=0,blank=True)
    UMARE = models.IntegerField(default=0,blank=True)
    WIP_SDP = models.IntegerField(default=0,blank=True)
    PERI = models.IntegerField(default=0,blank=True)
    PERWW = models.IntegerField(default=0,blank=True)
    #5/5
    SWK = models.IntegerField(default=0,blank=True)
    S_MEN = models.IntegerField(default=0,blank=True)
    S_MUT = models.IntegerField(default=0,blank=True)
    SMEST = models.IntegerField(default=0,blank=True)
    UMPO = models.IntegerField(default=0,blank=True)
    UM_S = models.IntegerField(default=0,blank=True)
    UM_E = models.IntegerField(default=0,blank=True)
    #5/1
    POSTDS = models.IntegerField(default=0,blank=True)
    WIPDS = models.IntegerField(default=0,blank=True)
    WIPST = models.IntegerField(default=0,blank=True)
    WIPDR = models.IntegerField(default=0,blank=True)
    F_KR = models.IntegerField(default=0,blank=True)
    #6/2
    PERAN_1G = models.IntegerField(default=0,blank=True)
    PERWAN_1G = models.IntegerField(default=0,blank=True)
    UM_1G = models.IntegerField(default=0,blank=True)
    PERWR_1G = models.IntegerField(default=0,blank=True)
    #6/5
    PERR_1G = models.IntegerField(default=0,blank=True)
    UMA_1G = models.IntegerField(default=0,blank=True)
    UMAR_1G = models.IntegerField(default=0,blank=True)
    #6/3
    PERAN_E = models.IntegerField(default=0,blank=True)
    #6/6
    PERR_E = models.IntegerField(default=0,blank=True)