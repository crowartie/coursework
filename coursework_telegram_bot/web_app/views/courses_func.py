from flask import request
from web_app import app
from web_app.database import courses_DB
from bot.functions import funcCousesForWebApp


@app.route('/_get_path_exist_course', methods=['POST'])
def get_path_exist_course():
    if request.method == 'POST':
        data = request.json
        return courses_DB.get_path_exist_course(data['id'])


@app.route('/_get_text_exist_course', methods=['POST'])
def get_text_exist_course():
    if request.method == 'POST':
        data = request.json
        return funcCousesForWebApp.get_course(data['file'])


@app.route('/_upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        data = request.json
        oldText = data['file'].splitlines()
        text = ""
        for line in oldText:
            line = line.strip()
            if len(line) != 0:
                text += line + "\n"
        return {"text": text}


@app.route('/_save_text_in_course', methods=['POST'])
def save_text_in_course():
    if request.method == 'POST':
        data = request.json
        funcCousesForWebApp.save_text_in_course(data['file'], data['text'])
        return "0"


@app.route('/_edit_status_course', methods=['POST'])
def edit_status():
    if request.method == 'POST':
        data = request.json
        courses_DB.edit_status(data['id'], data['status'])
        return "0"


@app.route('/_get_count_symbols_file_path', methods=['POST'])
def get_count_symbols_file_path():
    if request.method == 'POST':
        data = request.json
        return funcCousesForWebApp.get_count_symbols_file_path(data['file'])


@app.route('/_reset_data_in_exist_course', methods=['POST'])
def reset_data_in_exist_course():
    if request.method == 'POST':
        data = request.json
        courses_DB.reset_data_users_in_courses(data['count_symbols'], data['course_id'])
        return "0"


@app.route('/_create_course', methods=["POST"])
def create_course():
    if request.method == 'POST':
        data = request.json
        return courses_DB.create_course(data['course_name'])


@app.route('/_edit_course', methods=["POST"])
def edit_course():
    if request.method == 'POST':
        data = request.json
        courses_DB.edit_course(data['id'], data['course_name'])
        return "0"


@app.route('/_delete_course', methods=["POST"])
def delete_course():
    if request.method == 'POST':
        data = request.json
        courses_DB.delete_course(data['id'])
        return "0"
