from bot.buttons import buttonsCourses,buttonsMenu
from bot.database import personalDataOfUsers
from bot.functions import funcCourse


def courses(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "courses")
    def send_courses(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="Курсы:",
                              reply_markup=buttonsCourses.generate_buttons_courses())

    @bot.callback_query_handler(func=lambda call: call.data == "return_to_menu_from_courses")
    def return_to_menu_from_courses(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="Меню:",
                              reply_markup=buttonsMenu.generate_buttons_menu())
    @bot.callback_query_handler(func=lambda call: call.data.startswith("course"))
    def course(call):
        userActivityInCourse=personalDataOfUsers.get_data_activity_user_for_courses(call.message.chat.id,call.data)
        if userActivityInCourse:
            pass

        else:
            personalDataOfUsers.add_data_activity_user_for_courses(call.message.chat.id,call.data)
            userActivityInCourse = personalDataOfUsers.get_data_activity_user_for_courses(call.message.chat.id, call.data)
        dataCourseForUser=funcCourse.get_course_text_for_send_user(userActivityInCourse,call.data)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=dataCourseForUser['text'],
                              reply_markup=dataCourseForUser['buttons'])
