from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import TestingCenter, Helpline, Hospital

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'password',
            'father_name',
            'state',
            'district',
            'village',
            'latitude',
            'longitude',
            'is_infected',
            'travelled',
            'travel_country',
            'from_date',
            'to_date',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class TestingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingCenter
        fields = '__all__'


class HelplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helpline
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
