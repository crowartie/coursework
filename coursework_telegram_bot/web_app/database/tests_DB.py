from web_app.database.MySQLConnect import create_connection


def delete_test(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""DELETE FROM `tests` WHERE id={id}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()


def check_status_test(test_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""SELECT status from tests WHERE id={test_id}"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()


def add_test(name):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""INSERT INTO `tests`( `name`, `callback`, `status`) VALUES ('{name}','',0)"""
        cursor.execute(select)
        lastId = cursor.lastrowid
        select = f"""UPDATE `tests` SET `callback`=concat('test','{str(lastId)}') WHERE id={lastId}"""
        cursor.execute(select)
        select = f"""select * from tests where id={lastId}"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.commit()
        connection.close()


def edit_test(id, name):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE `tests` SET `name`='{name}' WHERE id={id}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()


def get_count_questions(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""SELECT count(*) as count FROM `questions` WHERE test_id={id}"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()


def edit_status_test(id, status):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE `tests` SET `status`={status} WHERE id={id}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()


def reset_data_users_enabling_test(id_test):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE `usersActivityInTests` SET 
                     `num_question`=0,
                     `is_passing`=0,
                     `is_passed`=0,
                     `result`=0,
                     `max_result`=(select COUNT(questions.question) AS countQuestions
                                   FROM questions 
                                   WHERE test_id={id_test})
                     WHERE test_id={id_test}"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.commit()
        connection.close()


def get_tests():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select * from tests"""
        cursor.execute(select)
        result = cursor.fetchall()
        return result
    finally:
        connection.close()
