from django.urls import path,include
from .views import (index,search,reports,Create_reestr,check_ksg,
                    download,check_vt,check_ksg_sop,testPatients,
                    form_7)

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema as hospital_schema

urlpatterns = [
    path('',index.as_view(),name='index_hospital'),
    path('create_reestr/',Create_reestr.as_view(),name='create_reestr_hospital'),
    path('reports/',reports.as_view(),name='reports_hospital'),
    path('search/',search.as_view(),name='search_hospital'),
    path("search/graph_hospital/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=hospital_schema)),name='graph_hospital'),
    path("graph_hospital/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=hospital_schema)),name='graph_hospital'),
    path("api/",include('hospital.api.urls')),
    path("search/check_ksg/",check_ksg),
    path("download/",download),
    path("search/check_vt/",check_vt),
    path("search/check_ksg_sop/",check_ksg_sop),
    path("testPatients/",testPatients),
    path('formm_7/',form_7.as_view(),name='form_7_hospital'),
]
