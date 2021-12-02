from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def indexPageView(request):
    people = models.Statenames.objects.all()
    context = {
        "people": people,
    }
    return render(request, 'drug/index.html', context)

def aboutPageView(request):
    return render(request, 'drug/about.html')

def drugDetailPageView(request):
    return render(request, 'drug/drugDetail.html')

def drugSearchPageView(request):
    return render(request, 'drug/drugSearch.html')

def machineLearningPageView(request):
    return render(request, 'drug/machineLearning.html')

def prescriberDetailPageView(request):
    return render(request, 'drug/prescriberDetail.html')

def prescriberSearchPageView(request):    
    return render(request, 'drug/prescriberSearch.html')

def prescriberSearch(request):
    if request.method == "POST":
        prescriber = models.Prescriber.objects.all() #maybe should be get() id or something
        prescriber.fname= request.POST['fname']
        prescriber.lname= request.POST['lname']
        prescriber.credentials= request.POST['credentials'] 
        prescriber.gender= request.POST['gender'] 
        prescriber.state= request.POST['state'] 
        prescriber.specialty= request.POST['specialty'] 
    
    return()