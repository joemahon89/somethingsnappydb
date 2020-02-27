from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('patient',views.patient, name='patient'),
    path('variant',views.variant, name='variant'),
    path('position_variants',views.position_variants, name='position_variants'),
]

