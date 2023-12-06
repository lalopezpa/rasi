from django.urls import path
from .views import get_medical_history, update_medical_history

urlpatterns = [
    path('medical_history/<int:id>/', get_medical_history),
    path('medical_history/<int:id>/', update_medical_history),
]
