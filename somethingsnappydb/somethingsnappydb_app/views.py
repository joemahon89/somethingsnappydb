from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import PatientTable, VariantTable

from .models import (Patient,
                    SampleType,
                    SomaticInformation,
                    Sample,
                    Sequencer,
                    Analysis,
                    Variant,
                    RefGenome,
                    AnalysisVariant,
                    Interpretation,
                    Criteria,
                    InterpretationCriteria,)


# Create your views here.

# Search related Views
def search(request):
    query = request.GET['query']
    if "-" in query:
        chromosome = int(query.split("-")[0])
        position = query.split("-", 1)[1]
        # Two positions provided
        if "-" in position:
            print("YES")
            position1 = int(position.split("-")[0])
            position2 = int(position.split("-")[1])
            return redirect('position_variants_multiple', 
                        chromosome=chromosome,
                        position1=position1,
                        position2=position2,
                        )

        else:
            position = int(position)
            return redirect('position_variants', 
                        chromosome=chromosome,
                        position=position)
    else:
        return redirect('home')


def home(request):
    #return HttpResponse("Welcome to the Something Snappy Database")
    patients = Patient.objects.count()
    patientsAF = Patient.objects.filter(affected_relatives=0).count()
    variants = Variant.objects.count()
    pathogenic_variants4 = Interpretation.objects.filter(pathogenicity=5).count()
    pathogenic_variants5 = Interpretation.objects.filter(pathogenicity=4).count()
    pathogenic_variants = pathogenic_variants4 + pathogenic_variants5

    context = {"patients":patients,"variants":variants,"pathogenic_variants":pathogenic_variants,"patientsAF":patientsAF}

    return render (request,'somethingsnappydb_app/home.html',context)

def patient(request):
    return render (request,'somethingsnappydb_app/patient.html')


def variant(request):
    return render (request,'somethingsnappydb_app/variant.html')


# Position Variants Related Views


def position_variants(request, chromosome, position):
    """View that gets variants at a position"""
    variants = query_variants_at_pos(chromosome, position)
    context = {"variants" : variants,
                "position": position,
                "chromosome": chromosome,
                }
    return render(request,
                'somethingsnappydb_app/position_variants.html',
                context)

def query_variants_at_pos(chromosome, position):
    """Performs the django query to look for variants at a position.
    Includes the interpretations and genome build information"""
    variants_at_pos = AnalysisVariant.objects.select_related(
                                    'genome_id').all().select_related(
                                    'variant_id').all().filter(
                         variant_id__pos=position,
                         variant_id__chrom=chromosome)
    variants_at_pos = variants_at_pos.prefetch_related("interpretation_set").all()
    return variants_at_pos


# Between positions
def position_variants_multiple(request, chromosome, position1, position2):
    """View that gets variants at a position"""
    variants = query_variants_between_pos(chromosome, position1, position2)
    context = {"variants" : variants,
                "position1": position1,
                "position2": position2,
                "chromosome": chromosome,
                }
    return render(request,
                'somethingsnappydb_app/position_variants_multiple.html',
                context)

def query_variants_between_pos(chromosome, position1, position2):
    """Performs the django query to look for variants between two positions.
    Includes the interpretations and genome build information"""
    variants_at_pos = AnalysisVariant.objects.select_related(
                                    'genome_id').all().select_related(
                                    'variant_id').all().filter(
                                     variant_id__pos__gte=position1,
                                     variant_id__pos__lte=position2,
                                     variant_id__chrom=chromosome)
    variants_at_pos = variants_at_pos.prefetch_related("interpretation_set").all()
    return variants_at_pos

class PatientListView(SingleTableView):
    model = Patient
    table_class = PatientTable
    template_name='somethingsnappydb_app/patient.html'


class VariantListView(SingleTableView):
    model = Variant
    table_class = VariantTable
    template_name='somethingsnappydb_app/variant.html'
    

