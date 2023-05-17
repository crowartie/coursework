from bot.database import coursesRequest, personalDataOfUsers
from bot.buttons import buttonsCourse


def get_max_num_of_char_in_a_file(course):
    with open(f"bot/{coursesRequest.get_file_course(course)['file_path']}", "r", encoding='utf-8') as f:
        return len(f.read())


def get_course_text_for_send_user(user, course):
    with open(f"bot/{coursesRequest.get_file_course(course)['file_path']}", "r", encoding='utf-8') as f:
        text = f.read()
        if user['max_size_course'] <= 1000:
            personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['max_size_course'])
            buttons = buttonsCourse.generate_buttons_course(user)
            return {'buttons': buttons, 'text': text[0:user['max_size_course']]}
        if user['send_symbols'] >= user['max_size_course']:
            user['send_symbols'] = 1000
            buttons = buttonsCourse.generate_buttons_course(user)
            personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['send_symbols'])
            return {'buttons': buttons, 'text': text[0:user['send_symbols']]}
        elif user['send_symbols'] == 0:
            buttons = buttonsCourse.generate_buttons_course(user)
            personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['send_symbols'] + 1000)
            return {'buttons': buttons, 'text': text[0:user['send_symbols']+1000]}
        else:
            buttons = buttonsCourse.generate_buttons_course(user)
            return {'buttons': buttons, 'text': text[user['send_symbols'] - 1000:user['send_symbols']]}


def get_course_text_next_page_for_send_user(user):
    with open(f"bot/{coursesRequest.get_file_course_by_id_course(user['course_id'])['file_path']}", "r",
              encoding='utf-8') as f:
        text = f.read()
        if user['send_symbols'] + 1000 >= user['max_size_course']:
            buttons = buttonsCourse.generate_buttons_course_by_next_page(user)
            personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['max_size_course'])
            return {'buttons': buttons, 'text': text[user['send_symbols']:user['max_size_course']]}
        else:
            buttons = buttonsCourse.generate_buttons_course_by_next_page(user)
            personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['send_symbols'] + 1000)
            return {'buttons': buttons, 'text': text[user['send_symbols']:user['send_symbols'] + 1000]}


def get_course_text_previous_page_for_send_user(user):
    with open(f"bot/{coursesRequest.get_file_course_by_id_course(user['course_id'])['file_path']}", "r",
              encoding='utf-8') as f:
        text = f.read()
        if user['send_symbols'] == user['max_size_course']:
            user['send_symbols'] = user['send_symbols'] - (user['send_symbols'] % 1000)
            buttons = buttonsCourse.generate_buttons_course_by_previous_page(user)
            personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['send_symbols'])
            return {'buttons': buttons, 'text': text[user['send_symbols'] - 1000:user['send_symbols']]}
        else:
            user['send_symbols'] = user['send_symbols'] - 1000
            if user['send_symbols'] - 1000 <= 0:
                buttons = buttonsCourse.generate_buttons_course_by_previous_page(user)
                personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['send_symbols'])
                return {'buttons': buttons, 'text': text[0:user['send_symbols']]}
            else:
                buttons = buttonsCourse.generate_buttons_course_by_previous_page(user)
                personalDataOfUsers.update_data_activity_user_for_courses(user['user_id'], user['send_symbols'])
                return {'buttons': buttons, 'text': text[user['send_symbols'] - 1000:user['send_symbols']]}
