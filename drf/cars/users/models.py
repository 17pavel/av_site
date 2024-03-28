from django.db import models


# Create your models here.
class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID telegram',
        unique=True,
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
    )
    username = models.TextField(
        verbose_name='username',
    )
    block = models.TextField(
        verbose_name='Блокировка',
        default="no"
    )

    def __str__(self):

        return f'#{self.external_id}|{self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID telegram',
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Профиль',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    answer = models.TextField(
        verbose_name='Ответ',
        blank=True,
    )
    
    time = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'#{self.pk}|{self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Filter(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

    def __str__(self):
        return f'#{self.from_date}'

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'