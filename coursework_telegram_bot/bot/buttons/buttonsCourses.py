from telebot import types
from bot.database import coursesRequest


def generate_buttons_courses():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for button in coursesRequest.get_courses():
        markup.add(types.InlineKeyboardButton(text=f"{button['name']}", callback_data=f"{button['callback']}"))
    markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_courses"))
    return markup



