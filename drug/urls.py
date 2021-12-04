from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import drugDetailPageView
from .views import drugSearchPageView
from .views import machineLearningPageView
from .views import prescriberDetailPageView
from .views import prescriberSearchPageView
from .views import deletePrescriberView
<<<<<<< HEAD
from .views import updatePrescriberView
=======
from .views import drugDeleteView
>>>>>>> fa8c7e59a1bc4bea0dd5dc3f5fd12717a37b7d15

urlpatterns= [ 
    path("prescriberSearch/", prescriberSearchPageView, name="prescriberSearch"),
    path("machineLearning/", machineLearningPageView, name="machineLearning"),
    path("drugSearch/", drugSearchPageView, name="drugSearch"),
    path("drugDetail/<str:drug>/", drugDetailPageView, name="drugDetail"),
    path("drugDelete/<str:drug>/", drugDeleteView, name="drugDelete"),
    path("about/", aboutPageView, name="about"),
    path("", indexPageView, name="index"),
    path("delete/<str:prescriber>", deletePrescriberView, name="delete"),
    path("prescriberDetail/<str:prescriber>", prescriberDetailPageView, name="drDetail"),
    path("updatePrescriber/<str:drugName>/<str:number>/<str:npiT>", updatePrescriberView, name="updatePrescriber")
]