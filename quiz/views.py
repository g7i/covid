from django.shortcuts import render
from rest_framework import generics

from .models import Quiz, Attempted

from .serializers import QuizSerializer, AttemptedSerializer


class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizCreate(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class AttemptedList(generics.ListAPIView):
    queryset = Attempted.objects.all()
    serializer_class = AttemptedSerializer


class AttemptedCreate(generics.CreateAPIView):
    queryset = Attempted.objects.all()
    serializer_class = AttemptedSerializer
