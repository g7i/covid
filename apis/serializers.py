from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import (
    Advisory,
    Awareness,
    GovtData,
    Precaution,
    CoronaAudio,
)

User = get_user_model()


class AdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisory
        fields = '__all__'


class AwarenessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awareness
        fields = '__all__'


class GovtDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovtData
        fields = '__all__'


class PrecautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precaution
        fields = '__all__'


class CoronaAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaAudio
        fields = '__all__'
