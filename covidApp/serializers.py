from django.contrib.auth import get_user_model
from rest_framework import serializers

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
