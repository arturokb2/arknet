from django.urls import re_path,path
from .import consumers
websocket_urlpatterns = [
    path('hospital/ws/reports/<int:user_id>/',consumers.ReportsConsumer.as_asgi()),
    path('hospital/ws/reports_mix/<int:user_id>/',consumers.ReportsMixConsumer.as_asgi()),
    path('hospital/ws/annual_reports/<int:user_id>/',consumers.AnnualReportsConsumer.as_asgi()),
    path('hospital/ws/reference/<int:user_id>/',consumers.ReferenceConsumer.as_asgi()),
    path('hospital/ws/exportfrom1c/<int:user_id>/',consumers.ExportFrom1cConsumer.as_asgi()),
    path('hospital/ws/create_reestr/<int:user_id>/',consumers.CreateReestr.as_asgi()),
    path('hospital/ws/hospital/',consumers.Hospital.as_asgi()),
]


