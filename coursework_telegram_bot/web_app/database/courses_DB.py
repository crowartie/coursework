from web_app.database.MySQLConnect import create_connection
from bot.functions import funcCousesForWebApp


def get_courses():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select * from courses"""
        cursor.execute(select)
        return cursor.fetchall()

    finally:
        connection.close()

def get_path_exist_course(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select file_path from courses where id={id}"""
        cursor.execute(select)
        return cursor.fetchone()

    finally:
        connection.close()

def get_text_exist_course(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select file_path from courses where id={id}"""
        cursor.execute(select)
        return cursor.fetchone()

    finally:
        connection.close()

def edit_status(id,status):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""update courses set status={status} where id={id}"""
        cursor.execute(select)
        return cursor.fetchone()

    finally:
        connection.commit()
        connection.close()

def reset_data_users_in_courses(count_symbols,course_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""UPDATE `usersActivityInCourses` 
                     SET `is_passing`=0,`send_symbols`=0,`max_size_course`='{count_symbols}' 
                     WHERE course_id={course_id}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()

def create_course(course_name):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""INSERT INTO `courses`(`name`, `callback`, `file_path`, `status`) VALUES ('{course_name}','','',0)"""
        cursor.execute(select)
        lastId = cursor.lastrowid
        select = f"""update `courses` SET `callback`='course{lastId}', `file_path`='courses/course{lastId}.txt' where id={lastId}"""
        cursor.execute(select)
        select=f"""select id,file_path from courses where id={lastId}"""
        cursor.execute(select)
        return cursor.fetchone()

    finally:
        connection.commit()
        connection.close()

def edit_course(id,course_name):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""update `courses` SET `name`='{course_name}' where id={id}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()

def delete_course(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select=f"""select file_path from courses where id={id}"""
        cursor.execute(select)
        file=cursor.fetchone()
        funcCousesForWebApp.delete_file(file['file_path'])
        select=f"""delete from courses where id={id}"""
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()