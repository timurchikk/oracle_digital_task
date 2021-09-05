from django.shortcuts import render
from .models import *
from .serialisers import *
from rest_framework import generics, serializers


class CreateIntegrationView(generics.CreateAPIView):
    serializer_class = CreateIntegrationSerializer

class UpdateIntegrationView(generics.UpdateAPIView):
    serializer_class = UpdateDeleteIntegrationSerialiser
    queryset = IntegrationModel.objects.all()

class DeleteIntegrationView(generics.DestroyAPIView):
    serializer_class = UpdateDeleteIntegrationSerialiser
    queryset = IntegrationModel.objects.all()

class CreateAnswersView(generics.CreateAPIView):
    serializer_class = AnswersSerializer

class UpdateAnswersView(generics.UpdateAPIView):
    serializer_class = AnswersSerializer
    queryset = AnswersModel.objects.all()

class DeleteAnswerView(generics.DestroyAPIView):
    serializer_class = AnswersSerializer
    queryset = AnswersModel.objects.all()

class CreateQuestionView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer

class UpdateQuestionView(generics.UpdateAPIView):
    serializer_class = QuestionsSerializer
    queryset = QuestionsModel.objects.all()

class DeleteQuestionView(generics.DestroyAPIView):
    serializer_class = QuestionsSerializer
    queryset = QuestionsModel.objects.all()

class ListCreateUserQuestionsView(generics.ListCreateAPIView):
    serializer_class = UserQuestionsSerializer
    queryset = UserQuestionsModel.objects.all()