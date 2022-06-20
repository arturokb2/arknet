import graphene

from .models import *
from .type import *

class Query(graphene.ObjectType):
    F008 = graphene.List(F008Type)
    V006 = graphene.List(V006Type)
    V008 = graphene.List(V008Type)
    V014 = graphene.List(V014Type)
    F003 = graphene.List(F003Type)
    V009 = graphene.List(V009Type)

    V005 = graphene.List(V005Type)

    def resolve_F008(root,info):
        return F008.objects.filter(dateend=None).all()

    def resolve_V006(root,info):
        return V006.objects.filter(dateend=None).all()
    
    def resolve_V008(root,info):
        return V008.objects.filter(dateend=None).all()
    
    def resolve_V014(root,info):
        return V014.objects.filter(dateend=None).all()
    
    def resolve_F003(root,info):
        return F003.objects.filter(dateend=None).all()
    
    def resolve_V009(root,info):
        return V009.objects.filter(dateend=None).all()

    def resolve_V005(root,info):
        return V005.objects.filter(polname='Мужской').all()

schema = graphene.Schema(query=Query)
