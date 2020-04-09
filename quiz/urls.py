from django.urls import path
from . import views

urlpatterns = [

    path('quiz', views.QuizList.as_view()),
    path('quiz/create', views.QuizCreate.as_view()),

    path('attempt', views.AttemptedList.as_view()),
    path('attempt/create', views.AttemptedCreate.as_view()),

]
