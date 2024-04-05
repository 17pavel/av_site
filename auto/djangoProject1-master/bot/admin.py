from django.contrib import admin
from bot.models import User, Message, Answers, Send_schedule, NewCar


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','User_id', 'name')

admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('Message_text', 'User_id', 'Chat_id', 'Message_date', 'Message_ans_status')
    ordering = ('-Message_date',)
    list_filter = ('Message_ans_status',)

admin.site.register(Message, MessageAdmin)

class AnsewrsAdmin(admin.ModelAdmin):
    list_display = ('Answer_text', 'Message_id', 'Answer_status', 'Answer_date')
    list_filter = ('Answer_status',)

admin.site.register(Answers, AnsewrsAdmin)

class Send_scheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Period', 'Quanty', 'Text', 'All', 'User')

admin.site.register(Send_schedule, Send_scheduleAdmin)

class NewCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'price', 'user')

admin.site.register(NewCar, NewCarAdmin)