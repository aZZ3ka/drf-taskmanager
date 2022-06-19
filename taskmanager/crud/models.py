from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок задачи')
    description = models.TextField(verbose_name='Описание задачи')
    finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Срок исполнения')
    executed = models.BooleanField(default=False, verbose_name='Выполнено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-pk']
