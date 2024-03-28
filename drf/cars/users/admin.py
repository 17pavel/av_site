from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect

from scheduled_tasks import send_all_answer
from .models import Profile, Message
from jobs.models import Jobs
from .filters import MessageFilter
from .forms import MessageForm
from bot_runner import main



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "external_id", "profile", "text", "answer", "time"]
    list_editable = ["answer"]
    list_filter = ["time", "profile"]
    search_fields = ["time"]
    ordering = ["profile"]
    filter_class = MessageFilter
    actions = ["send_answer"]

    def send_message(self, request, queryset):
        self.send_form(request, queryset)
        return request, queryset

    def send_answer(self, request, queryset):
        if request.method == "POST":
            answer = Jobs.objects.all()[0].message
            send_all_answer(queryset, answer)

    def send_form(self, request, queryset):
        form = MessageForm()
        return render(
            request,
            "admin/send_message.html",
            context={"messages": queryset, "form": form},
        )

    send_answer.short_description = "Рассылка"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["external_id", "name", "block"]
    list_editable = ["name", "block"]
    actions = ["start_bot"]

    def start_bot(self, request, queryset):
        main()