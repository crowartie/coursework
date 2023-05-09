from telebot import types

def generate_buttons_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text="Курсы для обучения", callback_data="courses"),
               types.InlineKeyboardButton(text="Тесты", callback_data="tests"),
               types.InlineKeyboardButton(text="Результаты", callback_data="result_tests")]
    markup.add(buttons[0],buttons[1],buttons[2])
    return markup




