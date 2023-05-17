from telebot import types
from bot.database import testsRequest


def generate_buttons_tests():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for button in testsRequest.get_tests():
        markup.add(types.InlineKeyboardButton(text=f"{button['name']}", callback_data=f"{button['callback']}"))
    markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_tests"))
    return markup


def generate_button_cancel_test():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="Вернуться к тестам",
                                          callback_data="tests"))
    return markup