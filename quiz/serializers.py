from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Quiz, Question, Attempted


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AttemptedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempted
        fields = '__all__'
