from telebot import types
from bot.database import testsRequest

def generate_buttons_answer_option(question):
    markup = types.InlineKeyboardMarkup()
    for button_answer_option in testsRequest.get_answer_option(question):
        markup.add(types.InlineKeyboardButton(text=f"{button_answer_option['answer_option']}",
                                              callback_data=f"ans&{button_answer_option['answer']}"))
    markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_test"))
    return markup

def button_when_show_true_answer():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Следующий",
                                          callback_data="next_question"))
    return markup

def generate_button_end_test():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Завершить", callback_data="return_to_menu_from_test"))
    return markup

