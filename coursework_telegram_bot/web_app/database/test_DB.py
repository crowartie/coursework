from dotenv import load_dotenv, find_dotenv
from web_app.database.MySQLConnect import create_connection

load_dotenv(find_dotenv())


def create_new_answer_in_new_question(answer):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""INSERT INTO `answers`(`question_id`, `answer_option`,`answer`) VALUES ({answer['id_question']},'{answer['answerOption']}',{answer['answer']})"""
        cursor.execute(select)
        return 0
    finally:
        connection.commit()
        connection.close()


def create_new_question(idTest, question):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""INSERT INTO `questions`(`test_id`, `question`) VALUES ({idTest},'{question}')"""
        cursor.execute(select)
        lastId = cursor.lastrowid
        return {"id_question": lastId}
    finally:
        connection.commit()
        connection.close()


def get_questions(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select questions.id, tests.name, question FROM questions JOIN tests on questions.test_id=tests.id WHERE tests.id={id};"""
        cursor.execute(select)
        result = cursor.fetchall()
        return result
    finally:
        connection.close()


def get_test(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select name from tests where id={id}"""
        cursor.execute(select)
        result = cursor.fetchone()
        return result['name']
    finally:
        connection.close()


def get_answer_option(question_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"""select * from answers where question_id={question_id}"""
        cursor.execute(select)
        result = cursor.fetchall()
        return result
    finally:
        connection.close()


def update_answer_options_in_exist_question(answer_options, question_id):
    connection = create_connection()
    try:
        reset_true_answer(question_id)
        answers_id = []
        for answer_option in answer_options:
            if (
            search_answer_option_in_exist_question(answer_option['question_id'], answer_option['answer_option_id'])):
                print("432222222")
                update_answer_option(answer_option['question_id'], answer_option['answer_option_id'],
                                     answer_option['answer_name'], answer_option['answer'])
                answers_id.append(answer_option['answer_option_id'])
            else:
                print("1232435543")

                answers_id.append(create_answer_option(answer_option['question_id'], answer_option['answer_name'],
                                                       answer_option['answer']))
        delete_answers(answers_id, question_id)
        return "0"
    finally:
        connection.commit()
        connection.close()


def search_answer_option_in_exist_question(question_id, answer_option_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"select * from answers where id={answer_option_id} and question_id={question_id}"
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()


def update_answer_option(question_id, answer_option_id, answer_option, answer):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"update answers set answer_option='{answer_option}', answer={answer} where question_id={question_id} and id={answer_option_id}"
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()


def create_answer_option(question_id, answer_option, answer):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"INSERT INTO `answers`(`question_id`, `answer_option`, `answer`) VALUES ({question_id},'{answer_option}',{answer})"
        cursor.execute(select)
        lastId = cursor.lastrowid
        return lastId
    finally:
        connection.commit()
        connection.close()


def reset_true_answer(question_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"update answers set answer=0 where question_id='{question_id}'"
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()


def delete_answers(answers_id, question_id):
    connection = create_connection()
    try:
        text = ""
        for answer_id in answers_id:
            if answers_id.index(answer_id) + 1 != len(answers_id):
                text += f"{answer_id},"
            else:
                text += f"{answer_id}"
        cursor = connection.cursor()
        select = f"delete from answers where id not in ({text}) and question_id={question_id}"
        cursor.execute(select)
    finally:
        connection.commit()
        connection.close()


def delete_question(question_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"delete from questions where id={question_id}"
        cursor.execute(select)
        return "0"
    finally:
        connection.commit()
        connection.close()


def edit_question(question_id, question_name):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"update questions set question='{question_name}' where id={question_id}"
        cursor.execute(select)
        return "0"
    finally:
        connection.commit()
        connection.close()

def check_status_test(id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        select = f"select status from tests where id={id}"
        cursor.execute(select)
        return cursor.fetchone()
    finally:
        connection.close()
