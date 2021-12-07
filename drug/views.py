from typing import ContextManager
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import re 
from django.db import connection
import requests
import json
import numpy as np

import drug

# Create your views here.

def indexPageView(request):
    return render(request, 'drug/index.html')

def aboutPageView(request):
    return render(request, 'drug/about.html')

def drugDetailPageView(request, drug):
    dru = models.Drug.objects.get(drugname=drug)
    drug = re.sub(r'[^a-zA-Z]','', drug)
    drug=drug.lower()
    drugKey = "-" + drug
    list= models.Prescriber.objects.order_by(drugKey)[0:10]
    countList = []
    
    for dr in list:
        attributes = vars(dr)
        countList.append(attributes[drug])



    context = {
        'dru': dru,
        "list": list,
        "counts": countList
        
    }
    return render(request, 'drug/drugDetail.html', context)

def drugSearchPageView(request):
    druginfo = models.Drug.objects.all()
    
    context = {
        "drug": druginfo,
       
    }

    return render(request, 'drug/drugSearch.html', context)

def drugDeleteView(request, drug):
    tempDrug = models.Drug.objects.get(drugname=drug)
    tempDrug.delete()
    druginfo = models.Drug.objects.all()
    
    context = {
        "drug": druginfo,
       
    }

    return render(request, 'drug/drugSearch.html', context)

def machineLearningPageView(request):
    states = models.Statedata.objects.all()
    context = {
        "states": states
    }
    return render(request, 'drug/machineLearning.html', context)

def prescriberDetailPageView(request, prescriber):
    #get prescriber requested
    dr = models.Prescriber.objects.get(npi=prescriber)

    #creates a dictionary of all of the attributes of the dr object
    attributes = vars(dr)
    tupList = []

    states = models.Statedata.objects.all()

    #loops through each dr attribute that is a drug. 
    for att in attributes:
        if ((type(attributes[att]) == int) and (att != 'totalperscriptions') and (attributes[att] != 0) and (att != 'npi')):
            avg = int(averagePrec(att))
            name = att
            amount = attributes[att]
            tempTup = (name, amount, avg)
            tupList.append(tempTup)

    #totalPrescriptions, credentials, specialty, gender, state, isopiodprescriber

    recDrugs = callRecommender(dr.totalperscriptions, "", dr.specialty, dr.gender, dr.state, dr.isopiodprescriber)

    context = {
        'dr': dr,
        'drugList': tupList,
        'states': states,
        'recDrugs': recDrugs
    }

    return render(request, 'drug/prescriberDetail.html', context)

def prescriberSearchPageView(request):    
    prescribers = models.Prescriber.objects.all()
    states = models.Statedata.objects.all()

    tuples = []
    for dr in prescribers:
        npi = "npi"
        value = dr.npi
        creds = models.Credential.objects.filter(**{npi: value})
        temptup = (dr, creds)
        tuples.append(temptup)


    context = {
        "prescriber": tuples,
        "states": states
    }

    return render(request, 'drug/prescriberSearch.html', context)

def deletePrescriberView(request, prescriber):
    dr = models.Prescriber.objects.get(npi=prescriber)
    dr.delete()
    prescribers = models.Prescriber.objects.all()
    states = models.Statedata.objects.all()
    tuples = []
    for dr in prescribers:
        creds = models.Credential.objects.filter(npi=dr.npi)
        temptup = (dr, creds)
        tuples.append(temptup)
    context = {
        "prescriber": tuples,
        "states": states
    }
    return render(request, 'drug/prescriberSearch.html', context)

def averagePrec(att):
    filterKey = att + '__gt'
    prescribers = models.Prescriber.objects.filter(**{filterKey: 0})
    total = 0
    count = 0
    for dr in prescribers:
        attributes = vars(dr)
        total += attributes[att]
        if attributes[att] > 0:
            count += 1
    
    return round((total / count), 0)



def updatePrescriberView(request):
    npi = request.POST.get("npi", "")
    dr = models.Prescriber.objects.get(npi = npi)
    attributes = vars(dr)


    drugName = request.POST.get("drugName", "")
    number = request.POST.get("number", "")
    models.Prescriber.objects.filter(npi=npi).update(**{drugName: number})

    diff = int(number) - int(attributes[drugName])
    newAmount = int(attributes["totalperscriptions"]) + diff
    key = "totalperscriptions"
    models.Prescriber.objects.filter(npi=npi).update(**{key: newAmount})

    data = {
        "newAmount": newAmount
    }
    return JsonResponse(data)

def addPrescriberView(request):
    fname = request.POST.get("fname", "")
    lname = request.POST.get("lname", "")
    gender = request.POST.get("gender", "")
    state = request.POST.get("state", "")
    specialty = request.POST.get("specialty", "")
    isopioid = request.POST.get("opioid", "")

    newDoc = models.Prescriber(fname=fname, lname=lname, gender=gender, state=state, specialty=specialty, isopiodprescriber = isopioid, totalperscriptions = 0)
    newDoc.save()

    prescribers = models.Prescriber.objects.all()
    states = models.Statedata.objects.all()

    tuples = []
    for dr in prescribers:
        npi = "npi"
        value = dr.npi
        creds = models.Credential.objects.filter(**{npi: value})
        temptup = (dr, creds)
        tuples.append(temptup)


    context = {
        "prescriber": tuples,
        "states": states
    }

    return render(request, 'drug/prescriberSearch.html', context)

def updatePrescriberDetailsView(request):
    npi = request.POST.get("npi", "")
    dr = models.Prescriber.objects.get(npi=npi)

    fname = request.POST.get("fname", "")
    if (fname != dr.fname):
        sqlUpdate(npi, "fname", fname)

    lname = request.POST.get("lname", "")
    if (lname != dr.lname):
        sqlUpdate(npi, "lname", lname)

    specialty = request.POST.get("specialty", "")
    if (specialty != dr.specialty):
        sqlUpdate(npi, "specialty", specialty)

    gender = request.POST.get("gender", "")
    if (gender != dr.gender):
        sqlUpdate(npi, "gender", gender)

    state = request.POST.get("state", "")
    if (state != dr.state):
        sqlUpdate(npi, "state", state)

    isopiodprescriber = request.POST.get("opioid", "")
    if (isopiodprescriber != dr.isopiodprescriber):
        sqlUpdate(npi, "isopiodprescriber", isopiodprescriber)

    dr = models.Prescriber.objects.get(npi=npi)
    attributes = vars(dr)

    tupList = []
    states = models.Statedata.objects.all()
    #loops through each dr attribute that is a drug. 
    for att in attributes:
        if ((type(attributes[att]) == int) and (att != 'totalperscriptions') and (attributes[att] != 0) and (att != 'npi')):
            avg = int(averagePrec(att))
            name = att
            amount = attributes[att]
            tempTup = (name, amount, avg)
            tupList.append(tempTup)
            
    recDrugs = callRecommender(dr.totalperscriptions, "", dr.specialty, dr.gender, dr.state, dr.isopiodprescriber)


    context = {
        "dr": dr,
        'drugList': tupList,
        'states': states,
        'recDrugs': recDrugs
    }
    return render(request, 'drug/prescriberDetail.html', context)

def sqlUpdate(npi, attribute, newValue):
    with connection.cursor() as cursor:
        if attribute == "fname":
            cursor.execute("UPDATE prescriber SET fname = %s WHERE npi = %s", [newValue, npi])
        if attribute == "lname":
            cursor.execute("UPDATE prescriber SET lname = %s WHERE npi = %s", [newValue, npi])
        if attribute == "specialty":
            cursor.execute("UPDATE prescriber SET specialty = %s WHERE npi = %s", [newValue, npi])
        if attribute == "gender":
            cursor.execute("UPDATE prescriber SET gender = %s WHERE npi = %s", [newValue, npi])
        if attribute == "state":
            cursor.execute("UPDATE prescriber SET state = %s WHERE npi = %s", [newValue, npi])
        if attribute == "isopiodprescriber":
            cursor.execute("UPDATE prescriber SET isopiodprescriber = %s WHERE npi = %s", [newValue, npi])


def RecommenderView(request):
    totalPrescriptions = request.POST.get("totalPrescriptions", "")
    credentials = request.POST.get("credentials", "")
    specialty = request.POST.get("specialty", "")
    gender = request.POST.get("gender", "")
    state = request.POST.get("state", "")
    isopiodprescriber = request.POST.get("opioid", "")

    drugList = callRecommender(totalPrescriptions, credentials, specialty, gender, state, isopiodprescriber)
    states = models.Statedata.objects.all()
    
    
    context = {
        "states": states,
        "drugList": drugList,
        "recommender": "True"
    }
    
    return render(request, 'drug/machineLearning.html', context)

def PredictorView(request):
    states = models.Statedata.objects.all()

    totalPrescriptions = request.POST.get("totalPrescriptions", "")
    credentials = request.POST.get("credentials", "")
    specialty = request.POST.get("specialty", "")
    gender = request.POST.get("gender", "")
    state = request.POST.get("state", "")
    isopiodprescriber = request.POST.get("opioid", "")

    predTotal = callPredictor(totalPrescriptions, gender, specialty, credentials, isopiodprescriber, state)

    context = {
        "states": states,
        "predictor": "True",
        "predTotal": predTotal
    }

    return render(request, 'drug/machineLearning.html', context) 

def callRecommender(totalPrescriptions, credentials, specialty, gender, state, isopiodprescriber):
    url = "http://680c85ca-cf52-4116-9171-cef2d9e9d1e6.eastus2.azurecontainer.io/score"
    payload = json.dumps({
    "Inputs": {
        "WebServiceInput3": [
        {
            "npi": 1992883235,
            "drugname": "LANTUS.SOLOSTAR",
            "qty": 49
        }
        ],
        "WebServiceInput1": [
        {
            "npi": 0,
            "gender": gender,
            "state": state,
            "specialty": specialty,
            "isopiodprescriber": isopiodprescriber,
            "totalperscriptions": totalPrescriptions,
            "credentials": credentials
        }
        ],
        "WebServiceInput2": [
        {
            "drugname": "ABILIFY",
            "isopiod": "FALSE"
        }
        ]
    },
    "GlobalParameters": {}
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer uIHNxgJeKTlQGcvZbzxFxXUMQeqbXdP0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()["Results"]["WebServiceOutput0"][0]
    drugList = []
    drugList.append(response["Recommended Item 1"])
    drugList.append(response["Recommended Item 2"])
    drugList.append(response["Recommended Item 3"])
    drugList.append(response["Recommended Item 4"])
    drugList.append(response["Recommended Item 5"])

    return drugList

def callPredictor(totalprec,gender, specialty, creds, isopioid, state):

    
    #totalPrec = np.log1p(int(totalPrec))
    url = "http://3cc325ee-4037-41e0-8f31-ba3ea5b8213d.eastus2.azurecontainer.io/score"

    payload = json.dumps({
    "Inputs": {
        "WebServiceInput0": [
        {
            "LnPlus1(totalperscriptions)": 0,
            "gender": gender,
            "specialty": specialty,
            "credentials": creds,
            "fname": "",
            "isopiodprescriber": isopioid,
            "state": state,
            "lname": "",
            "npi": 0
        }
        ],
        "WebServiceInput1": [
        {
            "id": 1,
            "npi": 1003008475,
            "credentials": "NP"
        },
        {
            "id": 2,
            "npi": 1003009630,
            "credentials": "MD"
        },
        {
            "id": 3,
            "npi": 1003016270,
            "credentials": "M.D."
        },
        {
            "id": 4,
            "npi": 1003042805,
            "credentials": "MD"
        },
        {
            "id": 5,
            "npi": 1003043324,
            "credentials": "M.D."
        }
        ]
    },
    "GlobalParameters": {}
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer p2VaNopYq3kyTeT1RvMDEWEHBlAbkZof'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    theGoods = str(round(float(response.json()["Results"]["WebServiceOutput0"][0]["ExpMinus1(Scored Labels)"]),3))
    print(theGoods)
    return theGoods