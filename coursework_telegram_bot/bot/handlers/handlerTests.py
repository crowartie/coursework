from bot.buttons import buttonsCourses, buttonsMenu, buttonsTests
from bot.database import personalDataOfUsers
from bot.functions import funcTest


def tests(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "tests")
    def send_tests(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="тесты:",
                              reply_markup=buttonsTests.generate_buttons_tests())

    @bot.callback_query_handler(func=lambda call: call.data == "return_to_menu_from_tests")
    def return_to_menu_from_courses(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="Меню:",
                              reply_markup=buttonsMenu.generate_buttons_menu())

    @bot.callback_query_handler(func=lambda call: call.data.startswith("test"))
    def test(call):
        userActivityInTest = personalDataOfUsers.get_data_activity_user_for_tests(call.message.chat.id, call.data)
        if userActivityInTest:
            pass
        else:
            personalDataOfUsers.add_data_activity_user_for_tests(call.message.chat.id, call.data)
        userActivityInTest = personalDataOfUsers.get_data_activity_user_for_tests(call.message.chat.id, call.data)
        question = funcTest.get_question_and_answer_option(userActivityInTest)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=question['text'],
                              reply_markup=question['buttons'])


