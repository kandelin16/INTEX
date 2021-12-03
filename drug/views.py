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
    #get prescriber requested
    dr = models.Prescriber.objects.get(npi=prescriber)

    #creates a dictionary of all of the attributes of the dr object
    attributes = vars(dr)
    tupList = []

    #loops through each dr attribute that is a drug. 
    for att in attributes:
        if ((type(attributes[att]) == int) and (att != 'totalperscriptions') and (attributes[att] != 0) and (att != 'npi')):

            avg = int(averagePrec(att))

            name = att
            amount = attributes[att]
            tempTup = (name, amount, avg)
            tupList.append(tempTup)


    context = {
        'dr': dr,
        'drugList': tupList
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

def averagePrec(att):
    prescribers = models.Prescriber.objects.all()

    total = 0
    count = 0
    for dr in prescribers:
        attributes = vars(dr)
        total += attributes[att]
        if attributes[att] > 0:
            count += 1
    
    return round((total / count), 0)
