from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('patient',views.patient, name='patient'),
    path('variant',views.variant, name='variant'),
    path('results/',views.search, name='search'),
    path('position_variants/<str:chromosome>/<str:position>/',
			    	views.position_variants, 
			    	name='position_variants'),
]



