from www.celery import app
# from services.hospital.save_oper_sluch import Load_md
from services.hospital.import_1с import Load_md
from services.hospital.create_reestr import Create
from services.hospital.patient_lists_reports import Create as Create_lists_reports
from services.hospital.reference_reports import ReferenceReport

# from services.hospital.reference_reports import Create as Create_reference_reports
from services.hospital.annual_reports import Create as Create_annual_reports
from services.hospital.patient import PatientsData
from services.hospital.reports import *
from services.hospital.annual_reports import AnnualReport

import json

@app.task
def save_oper_sluch(user):
    load_md = Load_md(user)
    #Убрать на боеваом сервере
    #load_md.clear_md()
    ###
    # load_md.load_data(user)
    # return load_md.insert_temp.rez
    return 'Load_md'

@app.task
def save_oper_monitoring_res(user):
    load_md = Load_md(user)
    return 'save_oper_monitoring_res'

@app.task
def create_reestr(user, date_1, date_2,type_reestr,his):
    create = Create(user,date_1,date_2,type_reestr,his)
    create.create()
    return 'Create Reestr OK !!!! '

@app.task
def create_mix_reports(user,request):
    if (request.get('list_data',None) != None):
        reports = Create_lists_reports(user,request)
        reports.create(request)
        return 'Create mix reports'
    else:
        return 'Not mix create reports'

# @app.task
# def create_reference_reports(user,request):
#     reports = Create_reference_reports(user,request)
#     reports.create()
#     return 'Create reference reports'

@app.task
def reference_report(user,request):
    ReferenceReport(user,request)
    return 'reference_report'

@app.task
def create_annual_reports(user,request):
    # reports = Create_annual_reports(user,request)
    # reports.create()
    AnnualReport(user,request)
    return 'Create annual reports'

@app.task
def create_list_of_patients(user,request):
    pass

@app.task
def Patients():
    # patients = PatientsData()
    # patients.sluchays()
    # bf = BetterFilter()
    #
    # # Применияем когда фильтруем данные и получаем объекст который соответсвует нужым фильтрам
    # # sp = OtdSpecification('НЕЙРОХИРУРГИЯ') & ProfkSpecification()
    #
    #
    # # Применияем когда нужно получить определенные поля из объектов
    # sp = OtdSpecification() ^ ProfkSpecification() ^ CountSluchaySpecification() ^ ProfKNSpecification() ^ \
    #      GocEkSpecification() ^ RezUmerSpecification() ^ RezUmerGocEkSpecification() ^ RezUmerGocEkSrSpecification()
    # for patient in patients.patients:
    #     for p in bf.filter(patient,sp):
    #         pass
    #         #Применияем когда нужно получить определенные поля из объектов
    #         # print(bf.format_list(p))
    #
    #         #Применияем когда фильтруем данные и получаем объекст который соответсвует нужым фильтрам
    #         # if p == True:
    #         #     print(patient.sluchay.otd)
    return ''