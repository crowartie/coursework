from flask import request
from web_app import app
from web_app.database import test_DB


@app.route('/_update_answer_options_in_exist_question', methods=['POST'])
def update_answer_options_in_exist_question():
    if request.method == 'POST':
        data = request.json
        return test_DB.update_answer_options_in_exist_question(data['answer_options'], data['question_id'])


@app.route('/_create_new_question', methods=['POST'])
def create_new_question():
    if request.method == 'POST':
        data = request.json
        return test_DB.create_new_question(data['id_test'], data['question'])


@app.route('/_create_new_answer_in_new_question', methods=['POST'])
def create_new_answer_in_new_question():
    if request.method == 'POST':
        data = request.json
        for answer in data:
            test_DB.create_new_answer_in_new_question(answer)
        return 'success'


@app.route('/_get_answer_option', methods=['POST'])
def get_answer_option():
    if request.method == 'POST':
        data = request.json
        return test_DB.get_answer_option(data['question_id'])


@app.route('/_delete_question', methods=['POST'])
def delete_question():
    if request.method == 'POST':
        data = request.json
        return test_DB.delete_question(data['question_id'])


@app.route('/_edit_question', methods=['POST'])
def edit_question():
    if request.method == 'POST':
        data = request.json
        return test_DB.edit_question(data['question_id'], data['question_name'])
