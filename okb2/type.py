from django.db.models.base import Model
from graphene_django import DjangoObjectType, fields
from .models import *


class F008Type(DjangoObjectType):
    class Meta:
        model = F008
        fields = ('tip_name',)
    
class V006Type(DjangoObjectType):
    class Meta:
        model = V006
        fields = ('tip_name',)

class V008Type(DjangoObjectType):
    class Meta:
        model = V008
        fields = ('tip_name',)

class V014Type(DjangoObjectType):
    class Meta:
        model = V014
        fields = ('tip_name',)

class F003Type(DjangoObjectType):
    class Meta:
        model = F003

class V009Type(DjangoObjectType):
    class Meta:
        model = V009
        fields = ('tip_name',)



class V005Type(DjangoObjectType):
    class Meta:
        model = V005
        fields = ('polname',)

class Age_groupType(DjangoObjectType):
    class Meta:
        model = Age_group
        fields = ('name',)