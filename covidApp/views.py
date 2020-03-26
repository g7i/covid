from tokenize import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from .serializers import UserSerializer, User, HelplineSerializer, HospitalSerializer, TestingCenterSerializer, \
    VideoSerializer, FaqSerializer, MemberSerializer
from .models import Helpline, Hospital, TestingCenter, Video, Faq, Member


class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieve(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MemberList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=user_id']
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberCreate(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberRetrieve(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberUpdate(UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class HelplineList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['lang']
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


class VideoList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['lang']
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoCreate(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetrieve(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class FaqList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['lang']
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqCreate(CreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqRetrieve(RetrieveAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


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
