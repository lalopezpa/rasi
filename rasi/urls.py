from django.urls import include, path
from . import views

urlpatterns = [
    path('historiaclinica/', include('historiaclinica.urls')),
    path('health/', views.health_check),
    path('patient/medical_history/', include('nombre_de_tu_app.patient.medical_history.urls')),

]


