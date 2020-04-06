from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
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
    filter_backends = [SearchFilter]
    search_fields = ['=cat']


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
    fuser = {
        "aadhar": user.username,
        "id": user.id
    }
    return Response(fuser,
                    status=HTTP_200_OK)


@api_view(('GET',))
def aggregates(request):
    try:
        search = request.GET.get('search', '')

        users = User.objects.all()
        members = Member.objects.all()

        if search:
            users = users.filter(state=search)
            members = members.filter(state=search)


        registered = len(users)

        infected, symptoms, recovered = set(), set(), set()
        for user in users.filter(is_infected=True):
            try:
                infected.add(int(user.username))
            except:
                pass
        for member in members.filter(is_infected=True):
            infected.add(member.aadhar)
        infected = len(list(infected))

        for user in users.filter(symptoms=True):
            try:
                symptoms.add(int(user.username))
            except:
                pass
        for member in members.filter(symptoms=True):
            symptoms.add(member.aadhar)
        symptoms = len(list(symptoms))

        for user in users.filter(cured=True):
            try:
                recovered.add(int(user.username))
            except:
                pass
        for member in members.filter(cured=True):
            recovered.add(member.aadhar)
        recovered = len(list(recovered))

        data = {
            "registered": registered,
            "infected": infected,
            "symptoms": symptoms,
            "recovered": recovered
        }

        return Response(data, status=HTTP_200_OK)
    except:
        return Response({'error': "An Error Occured"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
