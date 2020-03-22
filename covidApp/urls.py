from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersList.as_view(), name='UsersList'),
    path('login', views.login, name='login'),
    path('<int:pk>', views.UserRetrieve.as_view(), name='UserRetrieve'),
    path('register', views.UserCreate.as_view(), name='UserCreate'),

    path('hospital', views.HospitalList.as_view(), name='HospitalList'),
    path('hospital/<int:pk>', views.HospitalRetrieve.as_view(), name='HospitalRetrieve'),
    path('hospital/register', views.HospitalCreate.as_view(), name='HospitalCreate'),

    path('helpline', views.HelplineList.as_view()),
    path('helpline/<int:pk>', views.HelplineRetrieve.as_view()),
    path('helpline/register', views.HelplineCreate.as_view()),

    path('testing-center', views.TestingCenterList.as_view()),
    path('testing-center/<int:pk>', views.TestingCenterRetrieve.as_view()),
    path('testing-center/register', views.TestingCenterCreate.as_view()),

    path('video', views.VideoList.as_view()),
    path('video/<int:pk>', views.VideoRetrieve.as_view()),
    path('video/create', views.VideoCreate.as_view()),

    path('faq', views.FaqList.as_view()),
    path('faq/<int:pk>', views.FaqRetrieve.as_view()),
    path('faq/create', views.FaqCreate.as_view()),

]
