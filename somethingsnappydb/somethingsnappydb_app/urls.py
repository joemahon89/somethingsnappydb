from django.urls import path 
from . import views
from somethingsnappydb_app.views import PatientListView,VariantListView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('',views.home, name='home'),
    path('patient',login_required(PatientListView.as_view())),
    path('variant',login_required(VariantListView.as_view())),
    path('results/',views.search, name='search'),
    path('position_variants/<str:chromosome>/<str:position1>-<str:position2>/',
                views.position_variants_multiple, 
                name='position_variants_multiple'),
    path('position_variants/<str:chromosome>/<str:position>/',
			    	views.position_variants, 
			    	name='position_variants'),

                    
]



