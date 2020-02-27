from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        position = int(query.split("-")[1])
        return redirect('position_variants', 
                        chromosome=chromosome,
                        position=position)
    else:
        pass


def home(request):
    #return HttpResponse("Welcome to the Something Snappy Database")
    return render (request,'somethingsnappydb_app/home.html')

def patient(request):
    return render (request,'somethingsnappydb_app/patient.html')


def variant(request):
    return render (request,'somethingsnappydb_app/variant.html')


# Position Variants Related Views


def position_variants(request, chromosome, position):
    variants_at_pos = AnalysisVariant.objects.select_related(
                                    'genome_id').all().select_related(
                                    'variant_id').all().filter(
                         variant_id__pos=position,
                         variant_id__chrom=chromosome)
    variants_at_pos = variants_at_pos.prefetch_related("interpretation_set").all()
    #for i in variants_at_pos:
        #print(i.variant_id.raw_g)
        #print(vars(i))
        #print(i.genome_id.name)
        #print(i.interpretation_set)
        #print("#####")
        #print(vars(i.interpretation_set.all()[0].pathogenicity))
        #print(i.interpretation_set.all()[0].pathogenicity)
    context = {"variants" : variants_at_pos,
                "position": position,
                "chromosome": chromosome,
                }
    return render(request,
                'somethingsnappydb_app/position_variants.html',
                context)

