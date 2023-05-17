from bot.database import testsRequest, personalDataOfUsers
from bot.buttons import buttonsTest


def show_true_answer(question):
    text = ""
    for answer_option in testsRequest.get_answer_option(question):
        if answer_option['answer'] == 0:
            text += answer_option['answer_option'] + " ❌\n"
        else:
            text += answer_option['answer_option'] + " ✅\n"
    return {'text': text}


def get_question_and_answer_option(user):
    if user['num_question'] == user['max_result']:
        user['is_passed'] = 1
        user['is_passing'] = 0
        personalDataOfUsers.update_data_activity_user_for_tests(user)
        text = f"Вы успешно прошли тест.\nВаш результат:{100 / user['max_result'] * user['result']:.1f}%"
        buttons = buttonsTest.generate_button_end_test()

        return {'text': text, 'buttons': buttons}
    question = testsRequest.get_question(user['test_id'], user['num_question'])
    buttons = buttonsTest.generate_buttons_answer_option(question)
    return {'text': question, 'buttons': buttons}