from django.urls import path
from . import views

urlpatterns = [

    path('advisory', views.AdvisoryList.as_view()),
    path('advisory/create', views.AdvisoryCreate.as_view()),

    path('awareness', views.AwarenessList.as_view()),
    path('awareness/create', views.AwarenessCreate.as_view()),

    path('govt', views.GovtDataList.as_view()),
    path('govt/create', views.GovtDataCreate.as_view()),

    path('precaution', views.PrecautionList.as_view()),
    path('precaution/create', views.PrecautionCreate.as_view()),

    path('audio/create', views.CoronaAudioCreate.as_view()),

    path('neighbours', views.NeighbourList.as_view()),
    path('neighbours/create', views.NeighbourCreate.as_view()),

    path('requirements', views.RequirementList.as_view()),
    path('requirements/create', views.RequirementCreate.as_view()),

    path('daily-basis', views.DailyBasisList.as_view()),
    path('daily-basis/create', views.DailyBasisCreate.as_view()),

    path('home', views.HomeList.as_view()),
    path('home/create', views.HomeCreate.as_view()),

    path('bank', views.BankList.as_view()),
    path('bank/create', views.BankCreate.as_view()),

]
