from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    region = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Город'


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    photo = models.ImageField(upload_to='static/photos/', null=True, blank=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
class Car(models.Model):
    mark_car = models.CharField(max_length=100, verbose_name='Марка')
    model_car = models.CharField(max_length=100, verbose_name='Модель')
    generation = models.CharField(max_length=100, verbose_name='Поколение')
    body = models.CharField(max_length=100, verbose_name='Кузов')
    motor = models.CharField(max_length=100, verbose_name='Топливо')
    transmission = models.CharField(max_length=100, null=True, verbose_name='Коробка передач')
    drive = models.CharField(max_length=100, verbose_name='Привод')
    year = models.IntegerField(verbose_name='Год')
    price = models.IntegerField(verbose_name='Цена')
    volume = models.CharField(max_length=30, verbose_name='Объем двигателя')
    photo = models.TextField(verbose_name='Фото')
    vin = models.CharField(max_length=20, null=True, blank=True)
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    color = models.CharField(max_length=20, null=True, blank=True, verbose_name='Цвет')
    condition = models.CharField(max_length=20, null=True, verbose_name='Состояние')
    description = models.TextField(null=True, verbose_name='Описание')
    exchange = models.CharField(max_length=40, null=True, blank=True, verbose_name='Обмен')
    options = models.TextField(null=True, blank=True, verbose_name='Опции')
    city_id = models.ForeignKey(City, default=4, on_delete=models.CASCADE, verbose_name='Город')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Владелец')

    class Meta:
        verbose_name = "Машины"
        verbose_name_plural = "Машины"





