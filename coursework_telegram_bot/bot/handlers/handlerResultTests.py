from bot.functions import funcResult
from bot.buttons import buttonResultTest,buttonsMenu

def resultTest(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "result_tests")
    def result_tests(call):
        text=funcResult.create_result_text(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=text,reply_markup=buttonResultTest.generate_buttons_result_test())

    @bot.callback_query_handler(func=lambda call: call.data == "return_to_menu_from_result_tests")
    def return_to_menu_from_test(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="Меню:",
                              reply_markup=buttonsMenu.generate_buttons_menu())

