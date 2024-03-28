import json

import telebot
from telebot import types
from environs import Env
from django.core.paginator import Paginator

from items.models import Categories, Products
from items.serializers import CategorySerializer, ItemsSerializer
from users.models import Profile, Message

env = Env()
env.read_env()
bot = telebot.TeleBot(env("BOT"))
ITEMS_PAGE = 20


def get_data():
    category = Categories.objects.all()
    category_serializer = CategorySerializer(category, many=True)

    return category_serializer.data


def get_items(filter, page_number=1):
    if isinstance(filter, int):
        items_query = (
            Products.objects.filter(category_id=filter)
            .order_by("price")
            .exclude(price=0)
        )
    if isinstance(filter, str):
        items_query = (
            Products.objects.filter(name__icontains=filter)
            .order_by("price")
            .exclude(price=0)
        )
    paginator = Paginator(items_query, ITEMS_PAGE)
    items_query_page = paginator.get_page(page_number).object_list
    items_serializer = ItemsSerializer(items_query_page, many=True)
    items_data = items_serializer.data

    return items_data


@bot.message_handler(commands=["menu", "start"])
def send_menu(message: types.Message):
    category_data = get_data()
    keyboard = types.InlineKeyboardMarkup()

    for category in category_data:
        keyboard.add(
            types.InlineKeyboardButton(
                category["name"], callback_data=f"page_1_{category['id']}"
            )
        )

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.username}\nДобро пожаловать в наш автомагазин!",
        reply_markup=keyboard,
    )


# пагинация
@bot.callback_query_handler(func=lambda call: call.data.startswith("page_"))
def pagination(call):
    page_number = int(call.data.split("_")[1])
    filter = call.data.split("_")[-1]
    if filter.isdigit():
        filter = int(filter)
    items_data = get_items(filter, page_number)

    keyboard = types.InlineKeyboardMarkup()
    for item in items_data:
        keyboard.add(
            types.InlineKeyboardButton(
                f'{item["name"]} | {item["price"]}$',
                callback_data=f'item_{item["id"]}_{filter}',
            )
        )

    # кнопки "Назад" и "Вперед" для пагинации,
    if page_number > 1:
        keyboard.row(
            types.InlineKeyboardButton(
                "<< Назад", callback_data=f"page_{page_number - 1}_{filter}"
            )
        )
    if len(items_data) == ITEMS_PAGE:
        keyboard.row(
            types.InlineKeyboardButton(
                "Вперед >>", callback_data=f"page_{page_number + 1}_{filter}"
            )
        )

    bot.send_message(
        call.message.chat.id,
        f"Страница {page_number}. Выберите товар, задайте вопрос или воспользуйтесь поиском(search_mazda)",
        reply_markup=keyboard,
    )


# поиск
@bot.message_handler(func=lambda message: message.text.startswith("search_"))
def search(message: types.Message):
    page_number = 1
    filter = message.text.split("_")[1]
    items_data = get_items(filter, page_number)

    keyboard = types.InlineKeyboardMarkup()

    for item in items_data:
        keyboard.add(
            types.InlineKeyboardButton(
                f'{item["name"]} | {item["price"]}$',
                callback_data=f'page_1_{item["id"]}_{filter}',
            )
        )

    if page_number > 1:
        keyboard.row(
            types.InlineKeyboardButton(
                "<< Назад", callback_data=f"page_{page_number - 1}_{filter}"
            )
        )
    if len(items_data) == ITEMS_PAGE:
        keyboard.row(
            types.InlineKeyboardButton(
                "Вперед >>", callback_data=f"page_{page_number + 1}_{filter}"
            )
        )

    bot.send_message(
        message.chat.id,
        f"Страница {page_number}. Выберите товар или задайте вопрос",
        reply_markup=keyboard,
    )


# продукт
@bot.callback_query_handler(func=lambda call: call.data.startswith("item_"))
def item(call: types.CallbackQuery):
    items_id = call.data.split("_")[1]
    items_query = Products.objects.filter(id=items_id)
    items_serializer = ItemsSerializer(items_query, many=True)
    items_data = items_serializer.data
    items_data = json.dumps(items_data, ensure_ascii=False, indent=4)

    bot.send_message(call.message.chat.id, items_data)


# 2. Сохранять обращения пользователей в БД
@bot.message_handler()
def echo_all(message: types.Message):
    bot.reply_to(message, "Ваш вопрос стоит в очереди на ответ")
    profile, _ = Profile.objects.get_or_create(
        external_id=message.from_user.id,
        name=message.from_user.first_name,
        username=message.from_user.username,
    )
    message = Message(
        external_id=message.from_user.id, profile=profile, text=message.text
    )
    message.save()


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
