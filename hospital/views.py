from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls.conf import path
from django.views.generic import View
from django.http import JsonResponse
from .models import Load_1c,temp_monitoring_res
from .forms import Load_1c_forms
import datetime
from .tasks import (save_oper_sluch,
                    create_reestr,
                    create_mix_reports,
                    # create_reference_reports,
                    create_annual_reports,
                    save_oper_monitoring_res,
                    Patients,
                    reference_report)

from services.hospital.search_history import Search_history
from services.hospital.history import History
from services.hospital.history_save import Save
from okb2.models import group_kc_group,Tar_vt
import random, hashlib
import os
# Create your views here.
class index(View):
    def get(self, request):
        hash = hashlib.sha256(str(random.random()).encode()).hexdigest()
        return render(request, 'hospital_index.html',{'hash':hash})
    def post(self,request):
        if request.POST.get('type') == 'get_user':
            return JsonResponse({'user': request.user.id})
        elif request.POST.get('type') == 'load_fales':
            Load_1c.objects.filter(user=request.user.id).delete()
            temp_monitoring_res.objects.filter(user=request.user.id).delete()
            form = Load_1c_forms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                save_oper_monitoring_res.delay(request.user.id)
                return JsonResponse({'rez': ''}, status=200)
        # elif request.POST.get('type') == 'load':
        #     Load.objects.filter(user=request.user.id).delete()
        #     form = Load_forms(request.POST, request.FILES)
        #     if form.is_valid():
        #         form.save()
        #         save_oper_monitoring_res.delay(request.user.id)
        #         return JsonResponse({'rez': ''}, status=200)


class Create_reestr(View):
    def post(self,request):
        if request.POST.get('type') == 'create_reestr':
            create_reestr.delay(request.user.id,
                                request.POST.get('date_1'),
                                request.POST.get('date_2'),
                                request.POST.get('type_res'),
                                request.POST.get('filename'))
        return JsonResponse({'rez': ''})

class reports(View):
    def post(self,request):
        if self.request.POST.get('task_type') == 'kcc_cb' and self.request.POST.get('group_p_list') == 'null':
            create_mix_reports.delay(
                request.user.id,
                request.POST
            )
        elif self.request.POST.get('task_type') == 'kcc_cb' and self.request.POST.get('group_p_list') != 'null':
            reference_report.delay(
                request.user.id,
                request.POST
            )

        elif self.request.POST.get('task_type') == 'reports':
            reference_report.delay(
                request.user.id,
                request.POST
            )
        elif self.request.POST.get('task_type') == 'annual':
            create_annual_reports.delay(
                request.user.id,
                request.POST
            )
        return JsonResponse({'rez':True})

class form_7(View):
    def get(self,request):
        hash = hashlib.sha256(str(random.random()).encode()).hexdigest()
        return render(request, 'the_form_7.html',{'hash':hash})
 
class search(View):
    def get(self, request):
        hash = hashlib.sha256(str(random.random()).encode()).hexdigest()
        return render(request, 'search_history.html',{'hash':hash})

    def post(self, request):
        # if request.POST.get('type') == 'search':
        #     history_list = Search_history(request.POST.get('history'), request.user.id)
        #     rez = history_list.get_history()
        #     return JsonResponse({'rez': rez})
        if request.POST.get('type') == 'data_history':
            pk = request.POST.get('id')
            h = History(pk)
            rez = h.get_History_data()
            return JsonResponse({'rez': rez})
        elif request.POST.get('type') == 'save':
            save = Save(request=request)
            save.save()
            return JsonResponse({'rez':''})

def check_ksg(request):
    dat = datetime.datetime.now()
    dskz = request.GET['dskz'].strip() if request.GET['dskz'].strip() != '' else None
    dsc = request.GET['dsc'].strip() if request.GET['dsc'].strip()  != '' else None
    ksg_osn = request.GET['ksg_osn'].strip()
    ksg_osn_all = request.GET['ksg_osn_all'].strip() 
    pol = f'{request.GET["pol"].strip()}.0'
    datr = request.GET['datr'].strip() 
    datr = datetime.datetime.strptime(datr,'%d-%m-%Y')

    oper_osn = request.GET['oper_osn'].strip() if request.GET['oper_osn'].strip() != '' else None
    ds_osl = request.GET['ds_osl'].strip() if request.GET['ds_osl'].strip()!= "" else None
    oopkk = request.GET['oopkk'].strip() if  request.GET['oopkk'].strip() != "" else None
    code_usl = request.GET['code_usl'].strip()

    datv = request.GET['datv'].strip() 
    datv = datv.split('-')
    datv[2] = '20'+str(datv[2])
    datv = '-'.join(datv)
    datv = datetime.datetime.strptime(datv,'%d-%m-%Y')

    datp = request.GET['datp'].strip() 
    datp = datp.split('-')
    datp[2] = '20'+str(datp[2])
    datp = '-'.join(datp)
    datp = datetime.datetime.strptime(datp,'%d-%m-%Y')
    # dd = datetime.datetime.fromtimestamp((datv.second - datr.second))
    dd_year = datv.year - datr.year
    dd_day = datv - datr
    dd_day = dd_day.days


    if dd_year > 18:
        ddr = '6'
    elif 364 >= dd_day or 0 < dd_year <= 18:
        ddr = '5'
    elif 364 >= dd_day or 0 < dd_year <= 2:
        ddr = '4'
    elif 91 <= dd_day <= 364:
        ddr = '3'
    elif  29 <= dd_day <= 90:
        ddr = '2'
    elif 0 <= dd_day <= 28:
        ddr = '1'



    # count_day = datetime.datetime.fromtimestamp((datv - datp).seconds).day
    count_day = datv - datp
    count_day = count_day.days
    if count_day <=3:
        count_day = '1'
    elif 4 <= count_day <= 10:
        count_day = '2'
    elif 11 <= count_day <= 20:
        count_day = '3'
    elif 21 <= count_day <= 30:
        count_day = '4'
    

    group = group_kc_group.objects.values('mkb_10','code_usl','w','age','mkb_10_2','mkb_10_3','ikk','ksg','duration').filter(ksg=ksg_osn_all,ksg__istartswith='st',dateend=None)
    group_list = []
    gg = group_kc_group.objects.values_list('mkb_10','mkb_10_2','mkb_10_3','ksg','w','age','duration','code_usl','ikk').filter(ksg=ksg_osn_all,ksg__istartswith='st',dateend=None)
    for g in gg:
        group_list.append(list(g))
    temp = [dskz,dsc,ds_osl,ksg_osn_all,pol,ddr,count_day,oper_osn,oopkk]
    err = []
    err_bool = None
    rez = None
    err_age = None
    # ksg_osn_all

    for gp in group_list:
        t = temp.copy()
        for g in range(len(gp)):
            if gp[g] == None:
                t[g] = None
            if ksg_osn_all == 'st25.004':
                gp[0] = gp[0][0]
                t[0]  = t[0][0]
        # t = tuple(t)
        #
        # print(t)
        if t == gp:
            err_bool = True
            print(gp)
            data = group_kc_group.objects.values('id','dateend').filter(mkb_10=gp[0],mkb_10_2=gp[1],mkb_10_3=gp[2],\
                                                 ksg=ksg_osn_all,w=gp[4],age=gp[5],duration=gp[6],\
                                                 code_usl=gp[7],ikk=gp[8],dateend=None)[:1]
            if len(data) > 0:
                rez = data[0]['id']
            else:
                data = group_kc_group.objects.values('id', 'dateend').filter(mkb_10=gp[0] ,
                                                                             mkb_10_2=gp[1],
                                                                             mkb_10_3=gp[2],
                                                                             ksg=ksg_osn_all,
                                                                             w=gp[4], age=gp[5],
                                                                             duration=gp[6],
                                                                             code_usl=gp[7],
                                                                             ikk=gp[8],
                                                                             dateend=None)[:1]
                # elif len(data) == 0:
                #     data = group_kc_group.objects.values('id', 'dateend').filter(mkb_10=gp[0], mkb_10_2=gp[1],mkb_10_3=gp[2], \
                #                                                                  ksg=ksg_osn_all, w=gp[4], age=gp[5],duration=gp[6], \
                #                                                                  code_usl=gp[7], ikk=gp[8]).exclude(dateend=None)[:1]
                #     if len(data) > 0:
                #         err.append('Старый код КСГ отдайте историю экспертам')
                #         return JsonResponse({'rez': list(set(err)), 'r': rez})

            break
        else:
            err_bool = False


    
    if err_bool == False:
            print('123')
            mkb_10_list = [g['mkb_10'] for g in group]
            mkb_10_2_list = [g['mkb_10_2'] for g in group]
            mkb_10_3_list = [g['mkb_10_3'] for g in group]
            code_usl_list = [g['code_usl'] for g in group]
            duration_list = [g['duration'].split('.')[0] if g['duration'] != None else None  for g in group]
            w_list = [g['w'] for g in group]
            age_list = [g['age'] for g in group]
            ikk_list = [g['ikk'] for g in group]

            if mkb_10_list.count(None) != len(mkb_10_list):
                if (dskz in mkb_10_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия Ds Клин.заключ пациента')
                
            if mkb_10_2_list.count(None) != len(mkb_10_2_list):
                mkb_10_2_len = True
                if (dsc in mkb_10_2_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия Ds сопутствующий пациента')
            
            if mkb_10_3_list.count(None) != len(mkb_10_3_list): 
                if (ds_osl in mkb_10_3_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия Ds осложнения пациента')
                    err_ds_osl = True

            if code_usl_list.count(None) != len(code_usl_list): 
                if (oper_osn in code_usl_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия кода операции пациента')
                    err_oper_osn = True   
            if w_list.count(None) != len(w_list): 
                if (pol in w_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия пола пациента')
                    err_pol = True 
            
            if age_list.count(None) != len(age_list): 
                for age in age_list:
                    if age == '1' and 0 <= dd_day <= 28:
                        err_age = True
                        break

                    if age == '2' and 29 <= dd_day <= 90:
                        err_age = True
                        break
                    
                    if age == '3' and 91 <= dd_day <= 364:
                        err_age = True
                        break
                    
                    if age == '4' and (364 >= dd_day  or  0< dd_year <= 2):
                        err_age = True
                        break
                    
                    if age == '5' and (364 >= dd_day  or  0< dd_year <= 18):
                        err_age = True
                        break
                    
                    if age == '6' and  dd_year > 18:
                        err_age = True
                        break

                if err_age == False:
                    err.append('Ошибка КСГ: Нет соответствия возраста пациента')

            if duration_list.count(None) != len(duration_list):
                if (count_day in duration_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия койко дней')
                    

            if ikk_list.count(None) != len(ikk_list):
                if (oopkk in ikk_list) == False:
                    err.append('Ошибка КСГ: Нет соответствия классификатор критерии пациента')
                    err_oopkk = True  

    # print('id',rez)
    return JsonResponse({'rez':list(set(err)),'r':rez})
def check_ksg_sop(request):
    dsc = request.GET['dsc'].strip() if request.GET['dsc'].strip()  != '' else None
    ksg_sop = request.GET['ksg_sop'].strip()
    rez = group_kc_group.objects.values('id').filter(code_usl_kz=ksg_sop,mkb_10=dsc,dateend=None)
    r = None
    if rez.count() > 0:
        r = rez[0]['id']
    return JsonResponse({'rez':r})

def check_vt(request):

    dskz = request.GET['dskz'].strip()
    # dskz = str(dskz).split('.')[0]
    metod_hmp = request.GET['metod_hmp'].strip()
    vid_hmp = request.GET['vid_hmp'].strip()
    code_usl_vt = request.GET['code_usl_vt'].strip()
    vt = Tar_vt.objects.values('id').filter(kod_stat=metod_hmp, metod__icontains=vid_hmp,mkb__icontains=dskz,dateend=None)
    err = []
    if len(vt) == 0:
        dskz = str(dskz).split('.')[0]
        vt = Tar_vt.objects.values('id').filter(kod_stat=metod_hmp, metod__icontains=vid_hmp, mkb__icontains=dskz,dateend=None)
        if len(vt) == 0:
            err.append('Ошибка вида,метода,диагноза')
    return  JsonResponse({'rez':err})
def download(request):
    file = request.GET['file']
    if os.path.exists(file):
        with open(file,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(fh.name)}"'
            # response['Content-Disposition'] = 'inline;filename='+os.path.basename(fh.name)
            # response['Content-Disposition'] = 'inline;filename='+file

    return response

def testPatients(request):
    Patients.delay()
    return JsonResponse({'qwe':'qwe'})