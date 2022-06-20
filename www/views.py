from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages

from .forms import Form_auth



from django.core.mail import EmailMessage
from  django.http import  HttpResponse
from okb2.models import UpdatePers
from django.http import JsonResponse
from .tasks import update_pers
from django.contrib.auth.models import User

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def index(request):
# Функция index получает запрос от пользователя и выводит форму авторизации.
# Если пользователь существует и у него есть права доступа к ресурсу он на него перейдет.
    x = 1
    y = 2
    
    if request.POST:
        form = Form_auth(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            programm = request.POST.get('programms')

            user = authenticate(username = username.strip(),
                                password = password.strip()) 
                                
            if user == None:
                messages.success(request,'Пользователь не существует или пароль введен не правильно!')
                form = Form_auth()
                return render(request,'index.html',{'form':form}) 
            else:
                login(request,user)
                return redirect(programm)
    else:
        form = Form_auth()
        return render(request,'index.html',{'form':form})

def mail(request):
    email = EmailMessage("Hello",'message_arknet',' arknet@okb2-tmn.ru',['tyktybaev_ad@okb2-tmn.ru'])
    email.send()
    return HttpResponse('Почта отпавлена')

def UpdatePersFileHospital(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        UpdatePers.objects.filter(user=request.user.id).all().delete()
        for f in files:
            UpdatePers.objects.create(file=f,user=request.user)
        update_pers.delay(request.user.id)

    return JsonResponse({'rez':'updatefile'})

def hosp_mess(request):
    mes = request.GET['mes']
    async_to_sync(get_channel_layer().group_send)('hospital_user_all',
                                                  {'type': 'message', 'text': mes})
    return JsonResponse({'mes':mes})
