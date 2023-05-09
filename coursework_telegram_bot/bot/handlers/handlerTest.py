from bot.buttons import buttonsMenu,buttonsTest
from bot.database import personalDataOfUsers,testsRequest
from bot.functions import funcTest

def test(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "return_to_menu_from_test")
    def return_to_menu_from_test(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="Меню:",
                              reply_markup=buttonsMenu.generate_buttons_menu())

    @bot.callback_query_handler(func=lambda call: call.data.startswith("ans&"))
    def selected_answer_option(call):
        call.data = call.data[4:]
        namePassingTest = testsRequest.get_action_test(call.message.chat.id)
        userActivityInTest = personalDataOfUsers.get_data_activity_user_for_tests(call.message.chat.id, namePassingTest['test'])
        if call.data == "1":
            userActivityInTest['result'] += 1
        question = testsRequest.get_question(userActivityInTest['test_id'], userActivityInTest['num_question'])
        trueAnswer=funcTest.show_true_answer(question)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=trueAnswer['text'],
                              reply_markup=buttonsTest.button_when_show_true_answer())
        userActivityInTest['num_question'] += 1
        personalDataOfUsers.update_data_activity_user_for_tests(userActivityInTest)

    @bot.callback_query_handler(func=lambda call: call.data == "next_question")
    def next(call):
        namePassingTest = testsRequest.get_action_test(call.message.chat.id)
        if namePassingTest:
            pass
        userActivityInTest = personalDataOfUsers.get_data_activity_user_for_tests(call.message.chat.id, namePassingTest['test'])
        question = funcTest.get_question_and_answer_option(userActivityInTest)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=question['text'],
                              reply_markup=question['buttons'])



