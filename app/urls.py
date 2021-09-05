from django.urls import path
from .views import *

urlpatterns = [
    path('create_integration/', CreateIntegrationView.as_view()),
    path('update_integration/<int:pk>/', UpdateIntegrationView.as_view()),
    path('delete_integration/<int:pk>/', DeleteIntegrationView.as_view()),
    path('create_answer/', CreateAnswersView.as_view()),
    path('update_answer/<int:pk>/', UpdateAnswersView.as_view()),
    path('delete_answer/<int:pk>/', DeleteAnswerView.as_view()), 
    path('create_question/', CreateQuestionView.as_view()),
    path('update_question/<int:pk>/', UpdateQuestionView.as_view()),
    path('delete_question/<int:pk>/', DeleteQuestionView.as_view()),
    path('list_create_user_questions/', ListCreateUserQuestionsView.as_view()),
]