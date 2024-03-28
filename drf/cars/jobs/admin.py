from django.contrib import admin

from runapscheduler import Triger, Data
from .models import Jobs
from scheduled_tasks import schedule_jobs


# from runapscheduler import Command
# Register your models here.
# jobs = Jobs.objects.all()
@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ["triger", "period", "message", "date_on", "date_off", "date_create"]
    actions = [
        "send_one",
        "start_schedule_triger",
        "start_schedule_data",
    ]

    def send_one(self, request, queryset):
        schedule_jobs(queryset)


    def start_schedule_triger(self, request, queryset):
        start = Triger()
        start.handle(queryset)

    def start_schedule_data(self, request, queryset):
        start = Data()
        start.handle(queryset)
