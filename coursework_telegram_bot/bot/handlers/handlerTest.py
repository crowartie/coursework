from bot.buttons import buttonsMenu,buttonsTest,buttonsTests
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
        if namePassingTest:
            dataTest = testsRequest.get_data_test(namePassingTest['test'])
            if dataTest['status']==0:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.id,
                                      text="Данный тест отключен для обслуживания, по окончанию работ данные будут сброщены",
                                      reply_markup=buttonsTests.generate_button_cancel_test())
                return
            else:
                userActivityInTest = personalDataOfUsers.get_data_activity_user_for_tests(call.message.chat.id,
                                                                                          namePassingTest['test'])
                if call.data == "1":
                    userActivityInTest['result'] += 1
                question = testsRequest.get_question(userActivityInTest['test_id'], userActivityInTest['num_question'])
                trueAnswer = funcTest.show_true_answer(question)
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.id,
                                      text=trueAnswer['text'],
                                      reply_markup=buttonsTest.button_when_show_true_answer())
                userActivityInTest['num_question'] += 1
                personalDataOfUsers.update_data_activity_user_for_tests(userActivityInTest)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Данный тест перезапущен или удалён, вернитесь к тестам и проверьте",
                                  reply_markup=buttonsTests.generate_button_cancel_test())
            return


    @bot.callback_query_handler(func=lambda call: call.data == "next_question")
    def next(call):
        namePassingTest = testsRequest.get_action_test(call.message.chat.id)
        if namePassingTest:
            dataTest = testsRequest.get_data_test(namePassingTest['test'])
            if dataTest['status'] == 0:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.id,
                                      text="Данный тест отключен для обслуживания, по окончанию работ данные будут сброщены",
                                      reply_markup=buttonsTests.generate_button_cancel_test())
                return
            else:
                userActivityInTest = personalDataOfUsers.get_data_activity_user_for_tests(call.message.chat.id,
                                                                                          namePassingTest['test'])
                question = funcTest.get_question_and_answer_option(userActivityInTest)
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.id,
                                      text=question['text'],
                                      reply_markup=question['buttons'])
        else:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Данный тест перезапущен или удалён, вернитесь к тестам и проверьте",
                                  reply_markup=buttonsTests.generate_button_cancel_test())
            return




