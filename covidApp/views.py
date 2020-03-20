from tokenize import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from .serializers import UserSerializer, User, HelplineSerializer, HospitalSerializer, TestingCenterSerializer
from .models import Helpline, Hospital, TestingCenter


class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieve(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HelplineList(ListAPIView):
    queryset = Helpline.objects.all()
    serializer_class = HelplineSerializer


class HelplineCreate(CreateAPIView):
    queryset = Helpline.objects.all()
    serializer_class = HelplineSerializer


class HelplineRetrieve(RetrieveAPIView):
    queryset = Helpline.objects.all()
    serializer_class = HelplineSerializer


class HospitalList(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalCreate(CreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalRetrieve(RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class TestingCenterList(ListAPIView):
    queryset = TestingCenter.objects.all()
    serializer_class = TestingCenterSerializer


class TestingCenterCreate(CreateAPIView):
    queryset = TestingCenter.objects.all()
    serializer_class = TestingCenterSerializer


class TestingCenterRetrieve(RetrieveAPIView):
    queryset = TestingCenter.objects.all()
    serializer_class = TestingCenterSerializer


@csrf_exempt
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
