from django.contrib import admin

from parser_1 import Parser_kufar
from .models import Categories, Images, Products, Todo


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_editable = ["name"]
    actions = ["start_parser"]

    def start_parser(self, request, queryset):
        cars = Parser_kufar(id=queryset[0].id, cat=queryset[0].slug, name=queryset[0].name)
        cars.get_data()


admin.site.register(Images)
admin.site.register(Products)
admin.site.register(Todo)
