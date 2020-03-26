from django.shortcuts import render
from rest_framework import generics

from .models import (
    Advisory,
    Awareness,
    CoronaAudio,
    GovtData,
    Precaution
)

from .serializers import (
    AdvisorySerializer,
    AwarenessSerializer,
    GovtDataSerializer,
    PrecautionSerializer,
    CoronaAudioSerializer
)


class AdvisoryList(generics.ListAPIView):
    queryset = Advisory.objects.all()
    serializer_class = AdvisorySerializer


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
    queryset = GovtData.objects.all()
    serializer_class = GovtDataSerializer


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