from django.shortcuts import render
from django.http import HttpResponse

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

def prescriberDetailPageView(request):
    return render(request, 'drug/prescriberDetail.html')

def prescriberSearchPageView(request):
    return render(request, 'drug/prescriberSearch.html')