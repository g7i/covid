from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersList.as_view(), name='UsersList'),
    path('login', views.login, name='login'),
    path('<int:pk>/', views.UserRetrieve.as_view(), name='UserRetrieve'),
    path('register', views.UserCreate.as_view(), name='UserCreate'),
]
