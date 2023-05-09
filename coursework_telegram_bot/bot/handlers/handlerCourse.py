from bot.buttons import buttonsMenu
from bot.database import personalDataOfUsers
from bot.functions import funcCourse

def course(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "next_page_course")
    def next_page_course(call):
        userActivityInCourse = personalDataOfUsers.get_data_activity_user_while_passing_course(call.message.chat.id)
        dataCourseForUser=funcCourse.get_course_text_next_page_for_send_user(userActivityInCourse)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=dataCourseForUser['text'],
                              reply_markup=dataCourseForUser['buttons'])

    @bot.callback_query_handler(func=lambda call: call.data == "previous_page_course")
    def previous_page_course(call):
        userActivityInCourse = personalDataOfUsers.get_data_activity_user_while_passing_course(call.message.chat.id)
        dataCourseForUser = funcCourse.get_course_text_previous_page_for_send_user(userActivityInCourse)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text=dataCourseForUser['text'],
                              reply_markup=dataCourseForUser['buttons'])
    @bot.callback_query_handler(func=lambda call: call.data == "return_to_menu_from_course")
    def return_to_menu_from_courses(call):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="Меню:",
                              reply_markup=buttonsMenu.generate_buttons_menu())