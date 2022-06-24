from django.contrib import admin
from .models import *

class SluchayAdmin(admin.ModelAdmin):
    search_fields = ('id','nib')

admin.site.register(Load_1c)
admin.site.register(temp_oper)
admin.site.register(temp_sluch)
admin.site.register(Sluchay,SluchayAdmin)
admin.site.register(Vb_s)
admin.site.register(Vb_a)
admin.site.register(Vds)
admin.site.register(Le_Vr)
admin.site.register(Le_trv)
admin.site.register(Oper)
admin.site.register(Oslo)
admin.site.register(Manpy)
admin.site.register(Disability)
admin.site.register(Onk_sl)
admin.site.register(Napr)
admin.site.register(Cons)
admin.site.register(B_diag)
admin.site.register(B_prot)
admin.site.register(Onk_usl)
admin.site.register(Ksg_kpg)
admin.site.register(Patient_P)

class PatientAdmin(admin.ModelAdmin):
    search_fields = ('id',)
admin.site.register(Patient,PatientAdmin)



admin.site.register(Onmk_sp)
admin.site.register(Onmk_li)
admin.site.register(Med_dev)
admin.site.register(temp_monitoring_res)
admin.site.register(temp_monitoring_res_10)

admin.site.register(otdl7)
admin.site.register(umer7)
admin.site.register(form7)
