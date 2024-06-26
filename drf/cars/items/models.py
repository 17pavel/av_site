from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)

    #set to current time
    created = models.DateTimeField(auto_now_add=True) 
    completed = models.BooleanField(default=False)

    #user who posted this
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='slug')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    url = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание')
    parameter = models.JSONField()
    price = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="product",verbose_name='Категория')


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    

    def display_id(self):
        return f"{self.id}"


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price
        
class Images(models.Model):

    image = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="images", verbose_name='Продукт')

    class Meta:
        db_table="images"
        verbose_name = "Изображение"
        verbose_name_plural = "Изоброжения"


    def __str__(self):
        return self.image
