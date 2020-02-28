from django.urls import path, include
from . import views
from somethingsnappydb_app.views import PatientListView,VariantListView

urlpatterns = [
    path('',views.home, name='home'),
    path('patient',PatientListView.as_view()),
    path('variant',VariantListView.as_view()),
    path('results/',views.search, name='search'),
   path('position_variants/<str:chromosome>/<str:position1>-<str:position2>/',
			    	views.position_variants_multiple, 
			    	name='position_variants_multiple'),

    path('position_variants/<str:chromosome>/<str:position>/',
			    	views.position_variants, 
			    	name='position_variants'),
    path('accounts/', include('django.contrib.auth.urls')),

]



