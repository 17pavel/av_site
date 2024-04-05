import datetime
import schedule
import time
import telebot
from environs import Env
import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto.settings')
django.setup()

from bot.models import Answers, Message, Send_schedule, User
from av_by.models import Car
env = Env()
env.read_env()

bot = telebot.TeleBot(env.str('Token_bot'))

def AnswerBot():
    ans = Answers.objects.all()
    for an in ans:
        if not an.Answer_status:
            bot.send_message(an.Message_id.Chat_id, f'Вы справшивали <i>{an.Message_id.Message_text}</i>\n Ответ - <b>{an.Answer_text}</b>', parse_mode='html')
            an.Answer_status = True
            mes = Message.objects.all()
            m = mes.get(id= an.Message_id.id)
            m.Message_ans_status = True
            m.save()
            an.save()
            print('Ответ направлен')

def Send(id):
    user = User.objects.all()

    sends = Send_schedule.objects.get(id=id)
    if sends.All:
        for us in user:
            bot.send_message(us.User_id, sends.Text)
    else:
        bot.send_message(sends.User.User_id, sends.Text)

def FIlter(date_from, date_to):
    mess = Message.objects.all()
    mes_id = list()
    for mes in mess:
        try:
            if (datetime.date.today() - mes.Message_date.date()).days <= date_from and (datetime.date.today() - mes.Message_date.date()).days >= date_to:
                mes_id.append(mes.id)
        except TypeError:
            print('Ошибка формата')
    return mes_id

def First(day_from, day_to, month_from, month_to, year_from, year_to=2024):
    mess = Message.objects.all()
    first = {}
    last = {}
    for mes in mess:
        b=first.get(mes.User_id.id)
        if b:
            pass
        else: first[mes.User_id.id]=mes.Message_date.date()
        last[mes.User_id.id] = mes.Message_date.date()

    for key, val in last.items():
        if val.year>=year_from and val.year<=year_to and val.month>=month_from and val.month<=month_to and val.day>=day_from and val.day<=day_to:
            user = User.objects.get(id=key)
            print(user.name)

    print(f'Дата первого сообщения {first}')
    print(f'Дата последнего сообщения {last}')
def newcar():
    car = Car.objects.all()
    users = User.objects.all()
    for i in car:
        if i.data_create.date() == datetime.datetime.now().date():
            if i.data_create.time().hour==datetime.datetime.now().time().hour and i.data_create.time().minute >= datetime.datetime.now().time().minute -1:

                for user in users:
                    bot.send_message(user.User_id, f''' Добавлена новая машина!
                    {i.mark_car} {i.model_car}
                    {i.year} года
                    Цена {i.price}р
                    Продавец {i.user.name}
                    Телефон +375{i.user.phone}''')
def schedule_jobs():
    sends = Send_schedule.objects.all()
    schedule.every(3).seconds.do(AnswerBot)
    schedule.every(1).minute.do(newcar)
    for send in sends:
        if send.Period == 'sec':
            schedule.every(send.Quanty).seconds.do(Send, id=send.id)
        elif send.Period == 'min':
            schedule.every(send.Quanty).minutes.do(Send, id=send.id)
        elif send.Period == 'hour':
            schedule.every(send.Quanty).hours.do(Send, id=send.id)
        elif send.Period == 'day':
            if len(str(send.Quanty))==1:
                Quanty = '0' + str(send.Quanty)
            else: Quanty = str(send.Quanty)
            schedule.every().day.at(f'{Quanty}:00', 'Europe/Moscow').do(Send, id=send.id)


schedule_jobs()

newcar()
First(1, 5, 3, 3, 2024)

while True:
    schedule.run_pending()
    time.sleep(5)

