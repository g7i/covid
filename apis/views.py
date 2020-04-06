from django.shortcuts import render
from rest_framework import generics

from .models import (
    Advisory,
    Awareness,
    CoronaAudio,
    GovtData,
    Precaution,
    Neighbour,
    Requirement
)

from .serializers import (
    AdvisorySerializer,
    AwarenessSerializer,
    GovtDataSerializer,
    PrecautionSerializer,
    CoronaAudioSerializer,
    NeighbourSerializer,
    RequirementSerializer
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
    queryset = Precaution.objects.all()
    serializer_class = PrecautionSerializer


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
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementCreate(generics.CreateAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
