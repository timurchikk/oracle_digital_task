# Generated by Django 3.2.7 on 2021-09-05 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.answersmodel')),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.integrationmodel')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionsmodel')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы пользователей',
            },
        ),
    ]