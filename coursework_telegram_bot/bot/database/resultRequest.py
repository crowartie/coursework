from bot.database.MySQLConnect import create_connection


def get_tests_for_create_results():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = """select id,name from tests where status=1"""
        cursor.execute(select)
        return cursor.fetchall()
    finally:
        connection.close()



