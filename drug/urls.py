from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import drugDetailPageView
from .views import drugSearchPageView
from .views import machineLearningPageView
from .views import prescriberDetailPageView
from .views import prescriberSearchPageView
from .views import deletePrescriberView

urlpatterns= [ 
    path("prescriberSearch/", prescriberSearchPageView, name="prescriberSearch"),
    path("machineLearning/", machineLearningPageView, name="machineLearning"),
    path("drugSearch/", drugSearchPageView, name="drugSearch"),
    path("drugDetail/", drugDetailPageView, name="drugDetail"),
    path("about/", aboutPageView, name="about"),
    path("", indexPageView, name="index"),
    path("delete/<str:prescriber>", deletePrescriberView, name="delete"),
    path("prescriberDetail/<str:prescriber>", prescriberDetailPageView, name="drDetail"),
]