from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def indexPageView(request):
    return render(request, 'drug/index.html')

def aboutPageView(request):
    return render(request, 'drug/about.html')

def drugDetailPageView(request):
    return render(request, 'drug/drugDetail.html')

def drugSearchPageView(request):
    return render(request, 'drug/drugSearch.html')

def machineLearningPageView(request):
    return render(request, 'drug/machineLearning.html')

def prescriberDetailPageView(request, prescriber):
    dr = models.Prescriber.objects.get(npi=prescriber)

    context = {
        'dr': dr,
    }

    return render(request, 'drug/prescriberDetail.html', context)

def prescriberSearchPageView(request):    
    prescribers = models.Prescriber.objects.all()
    states = models.Statedata.objects.all()
    context = {
        "prescriber": prescribers,
        "states": states
    }

    return render(request, 'drug/prescriberSearch.html', context)

def deletePrescriberView(request, prescriber):
    dr = models.Prescriber.objects.get(npi=prescriber)
    dr.delete()
    prescribers = models.Prescriber.objects.all()
    states = models.Statedata.objects.all()
    context = {
        "prescriber": prescribers,
        "states": states
    }
    return render(request, 'drug/prescriberSearch.html', context)