# Generated by Django 3.2.7 on 2021-09-05 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('started_date', models.DateTimeField()),
                ('ended_date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='QuestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.integrationmodel')),
            ],
            options={
                'verbose_name': 'Вариант',
                'verbose_name_plural': 'Варианты',
            },
        ),
        migrations.CreateModel(
            name='AnswersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.integrationmodel')),
                ('true_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionsmodel')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
