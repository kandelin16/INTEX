from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import drugDetailPageView
from .views import drugSearchPageView
from .views import machineLearningPageView
from .views import prescriberDetailPageView
from .views import prescriberSearchPageView
from .views import deletePrescriberView
from .views import updatePrescriberView
from .views import addPrescriberView
from .views import updatePrescriberDetailsView

urlpatterns= [ 
    path("prescriberSearch/", prescriberSearchPageView, name="prescriberSearch"),
    path("machineLearning/", machineLearningPageView, name="machineLearning"),
    path("drugSearch/", drugSearchPageView, name="drugSearch"),
    path("drugDetail/<str:drug>/", drugDetailPageView, name="drugDetail"),
    path("about/", aboutPageView, name="about"),
    path("", indexPageView, name="index"),
    path("delete/<str:prescriber>", deletePrescriberView, name="delete"),
    path("prescriberDetail/<str:prescriber>", prescriberDetailPageView, name="drDetail"),
    path("updatePrescriptionCount/", updatePrescriberView, name="updatePrescriber"),
    path("addPrescriber/", addPrescriberView, name="AddPrescriber"),
    path("updatePrescriber/", updatePrescriberDetailsView, name="updatePrescriber")
]