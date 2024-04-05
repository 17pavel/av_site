from django.contrib import admin

from av_by.models import Car, User, City


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id','mark_car', 'model_car', 'generation', 'volume','body', 'price', 'data_create', 'year', 'city_id', 'user',)
    ordering = ('data_create',)

admin.site.register(Car, CarAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'id')



admin.site.register(User, UserAdmin)

class CityAdmin(admin.ModelAdmin):

    list_display = ('region', 'name')
    list_filter = ('region',)
    City.region.short_description = 'Область'
    City.name.short_description = 'Город'

    def __str__(self):
        return f'{self.name}'

admin.site.register(City, CityAdmin)

