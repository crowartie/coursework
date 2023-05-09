from bot.database import resultRequest,personalDataOfUsers


def create_result_text(user):
    text=""
    for test in resultRequest.get_tests_for_create_results():
        userActivityInTest=personalDataOfUsers.get_data_activity_user_for_create_result(user,test['id'])
        if(userActivityInTest):
            if userActivityInTest['num_question']==userActivityInTest['max_result'] and userActivityInTest['max_result']!=0 and userActivityInTest['num_question']!=0:
                text += f"{test['name']}: {100 / userActivityInTest['max_result'] * userActivityInTest['result']:.1f}%.\n"
            else:

                text += f"{test['name']}: Выполнение теста ещё не закончено\n"
        else:
            text+=f"{test['name']}: Ещё не начиналось выполнение.\n"

    return text

