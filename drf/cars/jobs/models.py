from django.db import models


# Create your models here.
class Jobs(models.Model):
    date_create = models.DateTimeField(
        verbose_name='Дата',
    )
    triger = models.TextField(
        verbose_name='тригер',
        blank=True
    )
    period = models.IntegerField(
        verbose_name='Периодичность',
    )
    message = models.TextField(
        verbose_name='Сообщение',
        
    )
    date_on = models.DateTimeField(
        verbose_name='Дата вкл',
    )
    date_off = models.DateTimeField(
        verbose_name='Дата выкл',
    )

    def __str__(self):
        return f'#{self.triger}|{self.period}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
