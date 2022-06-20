from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
#
# from okb2.models import *
# Register your models here.
from .models import (Statistics_type, F008, V006, V008, V014, F003, V009, V012, V010, V002, V020, V025, V021,
    V023, V026, V024, V001, Ab_Obsh, T003, T004, T005, Vra, T006, V027, V028, V029, N019, N018, N002, N003, N005, N007,
    N008, N010, N011, N001, N013, N014, N015, N016, N017, N020, dtrule, V016, V005, V017, N004, F011, otde, Ds, Rab_Ner,
    Oksm, Kladr, Kladr_T, Street, Street_T, Vrzb, CJ, V_LGOTY, Skom, Prpg, Ws, PR_PER, Trv, Trvnas, PY, PR_OSOB, Xosl,
    Posl, Aosl, Trs, Pope, Prli, Isfin, Tip_pb, Met_pb, PER, anesthesia,Age_group,group_kc_group,group_kc_group_det,group_kc_dkk,
    Code_med_dev,UpdatePers,UpdatePersData,Tar_vt)

from .models import MyUser
from django.urls import path
from django.shortcuts import render
import openpyxl
import os
import pandas as pd
import xlrd
from  django.conf import settings
import datetime
from django.contrib import messages

admin.site.register(MyUser)

class MyUser(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'Код подразделения'



class UserAdmin(UserAdmin):
    inlines = (MyUser,)

#T005
class T005Form(forms.Form):
    t005 = forms.FileField()
class T005Admin(admin.ModelAdmin):
    list_display = ('id_dokt','fam','im','ot','dr','code_dokt','code_vc','datebeg','dateend')
    list_filter = ('code_dokt',)
    search_fields = ('code_dokt','fam')
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_admin/',self.upload),]
        return new_urls + urls

    def upload(self,request):
        if request.method == "POST":
            temp_dir = 'temp/okb2'
            dir = '/'.join([settings.MEDIA_ROOT,temp_dir,''])
            dir += 't005.xls'
            t005_file = request.FILES["t005"]
            with open(dir, 'wb+') as f:
                for t005 in t005_file.chunks():
                    f.write(t005)
            rb = xlrd.open_workbook(dir,formatting_info=True)
            sheet = rb.sheet_by_index(0)
            error_list = []
            tmf = ['OKATO', 'CODE_MO', 'ID_DOKT', 'Fam', 'Im', 'Ot', 'DR', 'SNILS', 'OGRN', 'CODE_DOKT', 'CODE_VC', 'Name_1', 'DOKT_SP', 'Name_2', 'DATEBEG', 'DATEEND', 'Comment', '']
            for rownum in range(sheet.nrows):
                row = sheet.row_values(rownum)
                if rownum > 0:
                    if int(row[1]) == 720002:
                        try:
                            t = T005.objects.get(id_dokt=row[2],code_vc = int(row[10]))
                        except T005.DoesNotExist:
                            t = T005()
                        except:
                            #Туть нужно писать записи в файл если они ошибочно заполнены из файла.И отправить пользаку протокол 
                            error_list.append(row)
                            continue
                        try:
                            t.okato = int(row[0]) if row[0] != '' else None
                        except:
                            t.okato = None
                        try:
                            t.code_mo = int(row[1]) if row[1] != '' else None
                        except:
                            t.code_mo = None
                        t.id_dokt = row[2] if row[2] != '' else None
                        t.fam = row[3] if row[3] != '' else None
                        t.im = row[4] if row[4] != '' else None
                        t.ot = row[5] if row[5] != '' else None
                        try:
                            dr = datetime.datetime.strptime(row[6],'%d.%m.%Y')
                        except:
                            dr = None
                        t.dr = dr
                        t.snils = row[7] if row[7] != '' else None
                        try:
                            t.ogrn = int(row[8]) if row[8] != '' else None
                        except:
                            t.ogrn = None
                        t.code_dokt = row[9] if row[9] != '' else None
                        try:
                            t.code_vc = int(row[10]) if row[10] != '' else None
                        except:
                            t.code_vc = None
                        t.name_1 = row[11] if row[11] != '' else None
                        try:
                            t.dokt_sp = int(row[12]) if row[12] != '' else None
                        except:
                            t.dokt_sp = None
                        t.name_2 = row[13] if row[13] != '' else None
                        try:
                            datebeg = datetime.datetime.strptime(row[14],'%d.%m.%Y')
                        except:
                            datebeg = None
                        t.datebeg = datebeg
                        try:
                            dateend = datetime.datetime.strptime(row[15],'%d.%m.%Y')
                        except:
                            dateend = None
                        t.dateend = dateend
                        t.comment = row[16] if row[16] != '' else None
                        t.save()
                else:
                    if tmf != row:
                        messages.add_message(request,messages.ERROR,'Файл не соответствует структуре шаблону')
                        break
            else:
                messages.add_message(request,messages.INFO,'Файл обновлен')
        form = T005Form()
        data = {"form":form}
        return render(request,"admin/upload_admin.html",data)

#Vra
class VraForm(forms.Form):
    vra = forms.FileField()
class VraAdmin(admin.ModelAdmin):
    list_display = ('kod','naim','kod_spec','datebeg','dateend')
    list_filter = ('kod',)
    search_fields = ('kod','naim')
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_admin/',self.upload),]
        return new_urls + urls
    def upload(self,request):
        if request.method == "POST":
            temp_dir = 'temp/okb2'
            dir = '/'.join([settings.MEDIA_ROOT,temp_dir,''])
            dir += 'vra.xls'
            vra_file = request.FILES["vra"]
            with open(dir, 'wb+') as f:
                for vra in vra_file.chunks():
                    f.write(vra)
            rb = xlrd.open_workbook(dir,formatting_info=True)
            sheet = rb.sheet_by_index(0)
            tmf = ['KOD,C,5', 'NAIM,C,15', 'INI,C,2', 'KOD_OT,C,2', 'T005,C,8', 'KODVR,C,4', 'KOD_SPEC,C,3', 'V004,C,10', 'V002,C,3', 'V015,C,10', 'V021,C,10', 'N_SPEC,C,50', 'KOD_LPU,C,1', 'XAR_S,C,1', 'NPB,N,3,0', 'NORMA,N,4,0', 'ZAW,C,1', 'KOD_U,C,3', 'KOD_PRO,C,3', 'NAIM_T,C,15']
            update_date = datetime.datetime.now()
            Vra.objects.filter(datebeg=None,dateend=None).update(datebeg=update_date,
                                                                 dateend=update_date)
            #Vra.objects.all().delete()
            for rownum in range(sheet.nrows):
                row = sheet.row_values(rownum)
                if rownum > 0:
                    v = Vra()
                    v.kod = str(row[0]).strip()
                    v.naim = row[1]
                    v.ini = row[2]
                    v.kod_ot = row[3]
                    v.t005 = row[4]
                    v.kodvr = row[5]
                    v.kod_spec = row[6]
                    v.v004 = row[7]
                    v.v002 = row[8]
                    v.v015 = row[9]
                    v.v021 = row[10]
                    v.n_spec = row[11]
                    v.kod_lpy = row[12]
                    v.xar_s = row[13]
                    v.npb = row[14]
                    v.norma = row[15]
                    v.zaw = row[16]
                    v.kod_u = row[17]
                    v.kod_pro = row[18]
                    v.naim_t = row[19]
                    v.save()
                else:
                    if tmf != row:
                        messages.add_message(request,messages.ERROR,'Файл не соответствует структуре шаблону')
                        break
            else:
                messages.add_message(request,messages.INFO,'Файл обновлен')
        form = VraForm()
        data = {"form":form}
        return render(request,"admin/upload_admin.html",data)


class OtdeAdmin(admin.ModelAdmin):
    list_display = ('id','naim','datebeg','dateend')
    list_filter = ('tipe',)
    search_fields = ('naim','t013')

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Statistics_type)

admin.site.register(F008)
admin.site.register(V006)
admin.site.register(V008)
admin.site.register(V014)
admin.site.register(F003)
admin.site.register(V009)
admin.site.register(V012)
admin.site.register(V010)
admin.site.register(V002)
# admin.site.register(V018_bpoms)
# admin.site.register(V018_sboms)
# admin.site.register(V019_bpoms)
# admin.site.register(V019_sboms)
class V020Admin(admin.ModelAdmin):
    search_fields = ('idk_pr','k_prname')
    list_display = ('id','k_prname')
admin.site.register(V020,V020Admin)

admin.site.register(V025)
admin.site.register(V021)
admin.site.register(V023)
admin.site.register(V026)
admin.site.register(V024)
admin.site.register(V001)
admin.site.register(Ab_Obsh)
admin.site.register(T003)
admin.site.register(T004)
admin.site.register(T005,T005Admin)
admin.site.register(Vra,VraAdmin)
admin.site.register(T006)
admin.site.register(V027)
admin.site.register(V028)
admin.site.register(V029)
admin.site.register(N019)
admin.site.register(N018)
admin.site.register(N002)
admin.site.register(N003)
admin.site.register(N005)
admin.site.register(N007)
admin.site.register(N008)
admin.site.register(N010)
admin.site.register(N011)
admin.site.register(N001)
admin.site.register(N013)
admin.site.register(N014)
admin.site.register(N015)
admin.site.register(N016)
admin.site.register(N017)
admin.site.register(N020)
admin.site.register(dtrule)
admin.site.register(V016)
admin.site.register(V005)
admin.site.register(V017)
admin.site.register(N004)
admin.site.register(F011)
admin.site.register(otde,OtdeAdmin)
admin.site.register(Ds)
admin.site.register(Rab_Ner)
admin.site.register(Oksm)
admin.site.register(Kladr)
admin.site.register(Kladr_T)
admin.site.register(Street)
admin.site.register(Street_T)
admin.site.register(Vrzb)
admin.site.register(CJ)
admin.site.register(V_LGOTY)

class SkomAdmin(admin.ModelAdmin):
    search_fields = ('id','naim')
admin.site.register(Skom,SkomAdmin)

admin.site.register(Prpg)
admin.site.register(Ws)
admin.site.register(PR_PER)
admin.site.register(Trv)
admin.site.register(Trvnas)
admin.site.register(PY)
admin.site.register(PR_OSOB)
admin.site.register(Xosl)
admin.site.register(Posl)
admin.site.register(Aosl)
admin.site.register(Trs)
admin.site.register(Pope)
admin.site.register(Prli)
admin.site.register(Isfin)
admin.site.register(Tip_pb)
admin.site.register(Met_pb)
admin.site.register(PER)
admin.site.register(anesthesia)
admin.site.register(Age_group)
admin.site.register(group_kc_group)
admin.site.register(group_kc_group_det)
admin.site.register(group_kc_dkk)
admin.site.register(Code_med_dev)
admin.site.register(UpdatePers)
admin.site.register(UpdatePersData)

class Tar_vtAdmin(admin.ModelAdmin):
    search_fields = ('kod_stat','id')

admin.site.register(Tar_vt,Tar_vtAdmin)

