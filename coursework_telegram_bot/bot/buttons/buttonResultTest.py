from telebot import types
from bot.database import testsRequest


def generate_buttons_result_test():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_result_tests"))
    return markup
