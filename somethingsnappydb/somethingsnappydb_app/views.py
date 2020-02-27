from django.shortcuts import render
from django.http import HttpResponse

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
    