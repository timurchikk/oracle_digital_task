from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import check_rel_lookup_compatibility


#Класс вопросов
class AnswersModel(models.Model):
    integration = models.ForeignKey('IntegrationModel', on_delete=models.CASCADE)
    # title = models.CharField(max_length=50)
    answer_text = models.CharField(max_length=100)
    true_question = models.ForeignKey('QuestionsModel', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__ (self):
        return self.answer_text

#То что будет выводиться пользователю        
class UserQuestionsModel(models.Model):
    integration = models.ForeignKey('IntegrationModel', on_delete=models.CASCADE)
    answer = models.ForeignKey('AnswersModel', on_delete=models.CASCADE)
    question = models.ForeignKey('QuestionsModel', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы пользователей'

    def __str__ (self):
        return f'Ответ{self.id}'

#Варианы ответов в отдельном классе
class QuestionsModel(models.Model):
    question = models.CharField(max_length=50)
    integration = models.ForeignKey('IntegrationModel', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__ (self):
        return self.question

#Опросы в отдельном классе
class IntegrationModel(models.Model):
    title = models.CharField(max_length=50)
    started_date = models.DateTimeField()
    ended_date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__ (self):
        return self.title
