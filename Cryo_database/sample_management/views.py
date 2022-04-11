from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample, Location

def index(request):
    return HttpResponse("Here is the Cryopreservation page")

def detail(request, hp_accession):
    sample = Sample.objects.get(hp_accession = hp_accession)
    context = {'sample': sample}
    return render(request, 'sample_management/index.html', context)
    #return HttpResponse(f"You're looking for HP {hp_accession}")

# Create your views here.
