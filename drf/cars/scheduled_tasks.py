import telebot
from environs import Env

# from datetime import datetime

from users.models import Profile, Message

# from jobs.models import Jobs
# from django.utils import timezone

env = Env()
env.read_env()
bot = telebot.TeleBot(env("BOT"))


# 1. Проверка, есть ли в базе / Проверка блокировки/разблокировки
def send_all(to_sent):
    users = Profile.objects.filter(block="no")
    for user in users:
        print(f"{user.external_id}: {to_sent}")
        bot.send_message(user.external_id, to_sent)


# 3. Отправить пользователю ответ полученный из Джанго Админки
def sent_answer(message):
    # for message in messages:
        if message.answer:
            bot.send_message(message.external_id, message.answer)


# 4. Отправить всем пользователям ответ сообщение из рассылки


def send_all_answer(messages, answer):
    profiles = Profile.objects.filter(block="no")
    for profile in profiles:
        flag = False
        for message in Message.objects.filter(profile=profile):
            if message in messages:
                flag = True
        if flag:
            bot.send_message(profile.external_id, answer)


def schedule_jobs(jobs):
    profiles = Profile.objects.filter(block="no")
    for job in jobs:
        for profile in profiles:
            messages = Message.objects.filter(profile=profile)
            flag = False
            for message in messages:
                if job.date_off >= message.time >= job.date_on:
                    flag = True
            if flag:
                bot.send_message(profile.external_id, job.message)


def schedule_jobs_date(jobs):
    profiles = Profile.objects.filter(block="no")
    for job in jobs:
        for profile in profiles:
            bot.send_message(profile.external_id, job.message)


def schedule_jobs_last_message(jobs):
    profiles = Profile.objects.filter(block="no")
    for job in jobs:
        for profile in profiles:
            message = Message.objects.filter(profile=profile).last()
            if job.date_off >= message.time >= job.date_on:
                bot.send_message(profile.external_id, job.message)


def schedule_jobs_first_message(jobs):
    profiles = Profile.objects.filter(block="no")
    for job in jobs:
        for profile in profiles:
            message = Message.objects.filter(profile=profile).first()
            if job.date_off >= message.time >= job.date_on:
                bot.send_message(profile.external_id, job.message)
