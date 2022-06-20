from django.urls import path
from .views import (SearchHistoryListAPIView,
                    History,
                    PatientUpdate,
                    SluchayUpdate,
                    )
urlpatterns = [
    path('search_history/',SearchHistoryListAPIView.as_view()),
    path('history/<int:pk>/',History.as_view()),
    path('patient_update/<int:pk>/',PatientUpdate),
    path('sluchay_update/<int:pk>/',SluchayUpdate),
    # path('form7/',Form7ListAPIView.as_view()),
]