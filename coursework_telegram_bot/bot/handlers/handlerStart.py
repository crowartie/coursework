from bot.database import personalDataOfUsers
from bot.buttons import buttonsMenu
def start(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        if personalDataOfUsers.find_a_user_in_the_bot_database(message.chat.id):
            try:
                bot.delete_message(message.chat.id, message.message_id-1)
                bot.delete_message(message.chat.id, message.message_id)
            except:
                print("Ошибка при удалении")
            finally:
                bot.send_message(message.chat.id,
                                 text="С возвращением, мы рады снова вас видеть!!!",
                                 reply_markup=buttonsMenu.generate_buttons_menu())
        else:
            bot.send_message(message.chat.id,
                             text="Добро пожаловать на наш канал, я бот, обучающий математике.",
                             reply_markup=buttonsMenu.generate_buttons_menu())
            personalDataOfUsers.add_a_user_in_the_bot_database(message.chat.id)
