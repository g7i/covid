from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import (
    Advisory,
    Awareness,
    CoronaAudio,
    GovtData,
    Precaution,
    Neighbour,
    Requirement,
    DailyBasis,
    Home,
    Bank,
)

from .serializers import (
    AdvisorySerializer,
    AwarenessSerializer,
    GovtDataSerializer,
    PrecautionSerializer,
    CoronaAudioSerializer,
    NeighbourSerializer,
    RequirementSerializer,
    DailyBasisSerializer,
    HomeSerializer,
    BankSerializer,
)


class AdvisoryList(generics.ListAPIView):
    serializer_class = AdvisorySerializer

    def get_queryset(self):
        objs = Advisory.objects.all()
        search = self.request.query_params.get('search', None)
        if search is None:
            return objs
        if search == 'update':
            return objs.filter(is_update__exact=True)
        return objs.filter(is_update__exact=False)


class AdvisoryCreate(generics.CreateAPIView):
    queryset = Advisory.objects.all()
    serializer_class = AdvisorySerializer


class AwarenessList(generics.ListAPIView):
    queryset = Awareness.objects.all()
    serializer_class = AwarenessSerializer


class AwarenessCreate(generics.CreateAPIView):
    queryset = Awareness.objects.all()
    serializer_class = AwarenessSerializer


class GovtDataList(generics.ListAPIView):
    serializer_class = GovtDataSerializer

    def get_queryset(self):
        objs = GovtData.objects.all()
        search = self.request.query_params.get('search', None)
        if search is None:
            return objs
        if search == 'state':
            return objs.filter(is_state__exact=True)
        return objs.filter(is_state__exact=False)


class GovtDataCreate(generics.CreateAPIView):
    queryset = GovtData.objects.all()
    serializer_class = GovtDataSerializer


class PrecautionList(generics.ListAPIView):
    serializer_class = PrecautionSerializer

    def get_queryset(self):
        objs = Precaution.objects.all()
        search = self.request.query_params.get('search', None)
        if search is None:
            return objs
        if search == 'lockdown':
            return objs.filter(is_lockdown__exact=True)
        return objs.filter(is_lockdown__exact=False)


class PrecautionCreate(generics.CreateAPIView):
    queryset = Precaution.objects.all()
    serializer_class = PrecautionSerializer


class CoronaAudioCreate(generics.CreateAPIView):
    queryset = CoronaAudio.objects.all()
    serializer_class = CoronaAudioSerializer


class NeighbourList(generics.ListAPIView):
    queryset = Neighbour.objects.all()
    serializer_class = NeighbourSerializer


class NeighbourCreate(generics.CreateAPIView):
    queryset = Neighbour.objects.all()
    serializer_class = NeighbourSerializer


class RequirementList(generics.ListAPIView):
    serializer_class = RequirementSerializer

    def get_queryset(self):
        objs = Requirement.objects.all()
        state, dist = self.request.query_params.get('state', None), self.request.query_params.get('district', None)
        if state is not None:
            return objs.filter(state__iexact=state)
        if dist is not None:
            return objs.filter(district__iexact=dist)
        return objs


class RequirementCreate(generics.CreateAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class DailyBasisCreate(generics.CreateAPIView):
    queryset = DailyBasis.objects.all()
    serializer_class = DailyBasisSerializer


class DailyBasisList(generics.ListAPIView):
    queryset = DailyBasis.objects.all()
    serializer_class = DailyBasisSerializer
    filter_backends = [SearchFilter]
    search_fields = ['district']


class HomeCreate(generics.CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomeList(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=aadhar']


class BankCreate(generics.CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
