from django.urls import path 
from . import views
from somethingsnappydb_app.views import PatientListView

urlpatterns = [
    path('',views.home, name='home'),
    path('patient',PatientListView.as_view()),
    path('variant',views.variant, name='variant'),
    path('position_variants',views.position_variants, name='position_variants'),
    #path('data', PatientListView.as_view()),

]

