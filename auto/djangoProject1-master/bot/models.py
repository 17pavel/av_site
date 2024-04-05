
from django.db import models



class User(models.Model):
    User_id = models.BigIntegerField(verbose_name='Идетификатор пользователя')
    name = models.CharField(max_length=300, verbose_name='Имя пользователя')

    def __str__ (self):
        return f'{self.name}'
    class Meta():
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

class Message(models.Model):
    Message_id = models.IntegerField(verbose_name='Идентификатор сообщения')
    Message_text = models.TextField(verbose_name='Текст сообщения')
    Chat_id = models.BigIntegerField(verbose_name='Идентификатор чата')
    Message_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Идетификатор пользователя')
    Message_ans_status = models.BooleanField(default=False, verbose_name='Статус ответа')

    def __str__ (self):
        return f'{self.Message_text, self.User_id}'



    class Meta():
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'

class Answers(models.Model):
    Answer_text = models.TextField(verbose_name='Текст ответа')
    Message_id = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Идентификатор сообщения')
    Answer_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True)
    Answer_status = models.BooleanField(default=False, verbose_name='Статус ответа')
    class Meta():
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'


period_schedule = {'sec':'seconds', 'min':'minutes', 'hour':'hour', 'day':'day'}
class Send_schedule(models.Model):
    Period = models.CharField(choices=period_schedule, verbose_name='Период рассылки')
    Quanty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    Text = models.TextField(verbose_name='Текст')
    All = models.BooleanField(verbose_name='Всем пользователям')
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)

    class Meta():
        verbose_name = 'Рассылки'
        verbose_name_plural = 'Рассылки'


class NewCar(models.Model):
    mark = models.CharField(max_length=30, verbose_name='Модель машины', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta():
        verbose_name = 'Новые машины'
        verbose_name_plural = 'Новые машины'