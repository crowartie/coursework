from bot.database.MySQLConnect import create_connection
from bot.functions import funcCourse
def find_a_user_in_the_bot_database(user):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select * from users where user='{user}'"""
        cursor.execute(select)
        return cursor.fetchall()
    finally:
        connection.close()

def add_a_user_in_the_bot_database(user):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""insert into users (user) values('{user}')"""
        cursor.execute(select)
        return cursor.fetchall()
    finally:
        connection.commit()
        connection.close()

def get_data_activity_user_for_courses(user,course):
    connection=create_connection()
    try:
        print(user,course)

        cursor = connection.cursor()
        select = f"""UPDATE usersActivityInCourses SET  is_passing = 1                                         
                                     WHERE usersActivityInCourses.user_id=(select id from users where user='{user}')
                                        AND usersActivityInCourses.course_id=(select id from courses where callback='{course}')
        """
        cursor.execute(select)
        select = f"""select 	user_id,	course_id,	is_passing,	send_symbols,	max_size_course
                     from usersActivityInCourses where user_id=(select id from users where user='{user}') and 
                     course_id=(select id from courses where callback='{course}')"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.commit()
        connection.close()

def add_data_activity_user_for_courses(user,course):
    connection=create_connection()
    try:
        cursor = connection.cursor()
        select = f"""insert into usersActivityInCourses (user_id,	course_id,	is_passing,	send_symbols,	max_size_course) 
                     values ((select id from users where user='{user}'), 
                            (select id from courses where callback='{course}'),
                            1,0,{funcCourse.get_max_num_of_char_in_a_file(course)})"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()

def update_data_activity_user_for_courses(user_id,send_symbols):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE `usersActivityInCourses` 
                     SET `send_symbols`='{send_symbols}' 
                     WHERE is_passing=1 and user_id = '{user_id}'"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()

def get_data_activity_user_while_passing_course(user):
    connection=create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select user_id, course_id,	is_passing,	send_symbols, max_size_course
                     from usersActivityInCourses where user_id=(select id from users where user='{user}') and 
                     is_passing=1"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()

def get_data_activity_user_for_tests(user,test):
    connection=create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE usersActivityInTests SET  is_passing = 1                                         
                     WHERE user_id=(select id from users where user='{user}')
                     AND test_id=(select id from tests where callback='{test}')"""
        cursor.execute(select)
        select = f"""select user_id, test_id, num_question, is_passing, is_passed,result, max_result
                     from usersActivityInTests where user_id=(select id from users where user='{user}') and 
                     test_id=(select id from tests where callback='{test}')"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.commit()
        connection.close()

def add_data_activity_user_for_tests(user,test):
    connection=create_connection()
    try:
        cursor = connection.cursor()
        select = f"""insert into usersActivityInTests (user_id, test_id, num_question, is_passing, 
                                                       is_passed,result, max_result) 
                     values ((SELECT id from users where user='{user}'), 
                             (SELECT id FROM tests WHERE callback='{test}'), 
                             0, 1, 0, 0,
                             (select COUNT(questions.question) AS countQuestions
                              FROM questions 
                              WHERE test_id=(SELECT id FROM tests WHERE callback='{test}')))"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()

def update_data_activity_user_for_tests(user):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE usersActivityInTests SET num_question = {user['num_question']}, is_passing = {user['is_passing']}, 
                                                is_passed = {user['is_passed']}, result = {user['result']}
                         WHERE user_id={user['user_id']} and test_id={user['test_id']}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()

def get_data_activity_user_for_create_result(user,test_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select user_id, test_id, num_question, is_passing, is_passed,result, max_result
                         from usersActivityInTests where user_id=(select id from users where user='{user}') and 
                         test_id={test_id}"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()
