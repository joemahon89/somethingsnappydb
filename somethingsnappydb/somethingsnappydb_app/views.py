from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Patient, Variant
from django_tables2 import SingleTableView

from .tables import PatientTable, VariantTable

# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Something Snappy Database")
    return render (request,'somethingsnappydb_app/home.html')

def patient(request):
    return render (request,'somethingsnappydb_app/patient.html')


def variant(request):
    return render (request,'somethingsnappydb_app/variant.html')

def position_variants(request):
    return render (request,'somethingsnappydb_app/position_variants.html')

#def all_data(request):
#    return render (request, 'somethingsnappydb_app/all_data.html')

class PatientListView(SingleTableView):
    model = Patient
    table_class = PatientTable
    template_name='somethingsnappydb_app/patient.html'

class VariantListView(SingleTableView):
    model = Variant
    table_class = VariantTable
    template_name='somethingsnappydb_app/variant.html'
    