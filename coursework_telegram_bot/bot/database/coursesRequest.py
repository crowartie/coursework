from bot.database.MySQLConnect import create_connection


def get_courses():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = """select name, callback from courses where status=1"""
        cursor.execute(select)
        return cursor.fetchall()
    finally:
        connection.close()


def get_file_course(callback):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select file_path from courses where callback='{callback}'"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()


def get_file_course_by_id_course(course_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select file_path from courses where id='{course_id}'"""
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()

