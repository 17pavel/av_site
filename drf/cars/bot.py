import telebot
import json
from telebot import types, callback_data
from environs import Env
from django.core.paginator import Paginator

from items.models import Categories, Products
from items.urls import CategorySerializer, ItemsSerializer
from users.models import Profile, Message


bot = telebot.TeleBot("6935890707:AAFV1soCQucuipNHfnTuAiDTNTRvmAACsio")


def get_data():
    category = Categories.objects.all()
    category_serializer = CategorySerializer(category, many=True)

    return category_serializer.data


def get_items(category_id, page_number=1):
    items_query = Products.objects.filter(category_id=category_id)
    paginator = Paginator(items_query, 20)
    items_query_page = paginator.get_page(page_number).object_list
    items_serializer = ItemsSerializer(items_query_page, many=True)
    items_data = items_serializer.data

    return items_data


# Создаем объект CallbackData
pagination_callback = callback_data.CallbackData(["page"], "pagination")

@bot.callback_query_handler(func=lambda call: call.data.startswith('item_'))
def item_button(call):
    item_id = call.data.split('_')[1]
    # Добавьте здесь логику обработки callback для выбранного товара
    bot.send_message(call.message.chat.id, f"Вы выбрали товар с ID {item_id}")

@bot.callback_query_handler(func=lambda call: pagination_callback.filter(page=...))
def pagination_button(call):
    page_number = int(pagination_callback.get(call.data)["page"])
    items_data = get_items(page_number)
    
    keyboard = types.InlineKeyboardMarkup()
    for item in items_data:
        keyboard.add(types.InlineKeyboardButton(item["name"], callback_data=f'item_{item["id"]}'))
    
    # Добавляем кнопки "Назад" и "Вперед" для пагинации
    if page_number > 1:
        keyboard.row(types.InlineKeyboardButton('<< Назад', callback_data=pagination_callback.new(page=page_number - 1)))
    if len(items_data) == ITEMS_PER_PAGE:
        keyboard.row(types.InlineKeyboardButton('Вперед >>', callback_data=pagination_callback.new(page=page_number + 1)))
    
    bot.send_message(
        call.message.chat.id,
        f"Страница {page_number}. Выберите товар или задайте вопрос",
        reply_markup=keyboard,
    )

# Добавьте здесь функции get_data(), get_items(category_id) и get_items_for_page(page_number)

@bot.message_handler(commands=["menu"])
def send_menu(message):
    category_data = get_data()
    keyboard = types.InlineKeyboardMarkup()
    for category in category_data:
        keyboard.add(types.InlineKeyboardButton(category["name"], callback_data=category["id"]))
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.username}\nДобро пожаловать в наш автомагазин!",
        reply_markup=keyboard,
    )
