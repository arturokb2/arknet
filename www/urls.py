"""www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from okb2.schema import schema as okb2_schema
from hospital.schema import schema as hospital_schema

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .views import index,mail,hosp_mess
from www.views import UpdatePersFileHospital

urlpatterns = [
    path('',index,name="index"),
    path('update_pers_file_hospital/',UpdatePersFileHospital),
    path('hospital/',include('hospital.urls')),
    path('admin/', admin.site.urls),
    path("graph_hospital/",csrf_exempt(GraphQLView.as_view(graphiql=True,schema=hospital_schema))),
    path('mail/',mail,name="mail"),
    path('hosp_mess/',hosp_mess,name="hosp_mess"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)