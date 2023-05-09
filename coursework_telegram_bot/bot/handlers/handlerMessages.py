def messages(bot):
    @bot.message_handler(content_types=['text'])
    def chatting(message):
        bot.delete_message(message.chat.id, message.message_id)