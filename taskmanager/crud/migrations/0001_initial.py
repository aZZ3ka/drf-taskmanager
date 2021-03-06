# Generated by Django 4.0.5 on 2022-06-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('finish_date', models.DateTimeField(blank=True, null=True, verbose_name='Срок исполнения')),
                ('executed', models.BooleanField(default=False, verbose_name='Выполнено')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['-pk'],
            },
        ),
    ]
