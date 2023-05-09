from telebot import types


def generate_buttons_course(user):
    markup = types.InlineKeyboardMarkup()
    if user['max_size_course'] <= 1000:
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup
    elif user['send_symbols'] <= 1000:
        markup.add(types.InlineKeyboardButton(text="следующая", callback_data="next_page_course"))
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup
    elif user['send_symbols'] >= user['max_size_course']:
        markup.add(types.InlineKeyboardButton(text="предыдущая", callback_data="previous_page_course"))
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup
    else:
        buttons = [types.InlineKeyboardButton(text="следующая", callback_data="next_page_course"),
                   types.InlineKeyboardButton(text="Предыдущая", callback_data="previous_page_course")]
        markup.add(buttons[1], buttons[0])
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup


def generate_buttons_course_by_next_page(user):
    markup = types.InlineKeyboardMarkup()
    if user['send_symbols'] + 1000 >= user['max_size_course']:
        markup.add(types.InlineKeyboardButton(text="предыдущая", callback_data="previous_page_course"))
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup
    else:
        buttons = [types.InlineKeyboardButton(text="следующая", callback_data="next_page_course"),
                   types.InlineKeyboardButton(text="Предыдущая", callback_data="previous_page_course")]
        markup.add(buttons[1], buttons[0])
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup


def generate_buttons_course_by_previous_page(user):
    markup = types.InlineKeyboardMarkup()
    if user['send_symbols'] - 1000 <= 0:
        markup.add(types.InlineKeyboardButton(text="следующая", callback_data="next_page_course"))
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup
    else:
        buttons = [types.InlineKeyboardButton(text="следующая", callback_data="next_page_course"),
                   types.InlineKeyboardButton(text="Предыдущая", callback_data="previous_page_course")]
        markup.add(buttons[1], buttons[0])
        markup.add(types.InlineKeyboardButton(text="Меню", callback_data="return_to_menu_from_course"))
        return markup
