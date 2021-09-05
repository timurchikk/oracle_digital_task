from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import *

class UpdateDeleteIntegrationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = IntegrationModel
        fields = ('title', 'ended_date', 'description')

class CreateIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationModel
        fields = '__all__'
        
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsModel
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswersModel
        fields = '__all__'

class UserQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestionsModel
        fields = '__all__'

