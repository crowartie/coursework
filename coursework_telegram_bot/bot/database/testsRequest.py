from bot.database.MySQLConnect import create_connection


def get_tests():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = """select name, callback from tests where status=1"""
        cursor.execute(select)
        return cursor.fetchall()
    finally:
        connection.close()

def get_question(test_id,num_question):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""SELECT question FROM questions where test_id={test_id}"""
        cursor.execute(select)
        question = cursor.fetchall()
        return question[num_question]['question']
    finally:
        connection.close()


def get_answer_option(question):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""
             SELECT answers.answer_option AS answer_option, answers.answer AS answer
             FROM answers
             JOIN questions ON answers.question_id=questions.id
             WHERE questions.question='{question}'
            """
        cursor.execute(select)
        return cursor.fetchall()
    finally:
        connection.close()

def get_action_test(user):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""SELECT tests.callback AS test
                     FROM usersActivityInTests 
                     JOIN users ON usersActivityInTests.user_id=users.id 
                     JOIN tests ON usersActivityInTests.test_id=tests.id 
                     WHERE users.user='{user}' AND usersActivityInTests.is_passing=1"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()

def get_test():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""SELECT tests.callback AS test
                         FROM usersActivityInTests 
                         JOIN users ON usersActivityInTests.user_id=users.id 
                         JOIN tests ON usersActivityInTests.test_id=tests.id 
                         WHERE users.user='{user}' AND usersActivityInTests.is_passing=1"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()


