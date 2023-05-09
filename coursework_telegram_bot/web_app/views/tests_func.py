from web_app import app
from flask import request
from web_app.database import tests_DB


@app.route('/_check_status_test',methods=['POST'])
def check_status_test():
    if request.method=='POST':
        data=request.json
        return tests_DB.check_status_test(int(data['id']))


@app.route('/_del_test',methods=['POST'])
def del_test():
    if request.method=='POST':
        data=request.json
        tests_DB.delete_test(int(data['id']))
        return ({'result':'success'})


@app.route('/_edit_test',methods=['POST'])
def edit_test():
    if request.method=='POST':
        data=request.json
        tests_DB.edit_test(int(data['id']),data['name'])
        return "success"


@app.route('/_add_test',methods=['POST'])
def add_test():
    if request.method=='POST':
        data=request.json
        return tests_DB.add_test(data['name'])


@app.route('/_check_identical_in_tests',methods=['POST'])
def check_identical_in_tests():
    if request.method=='POST':
        data=request.json
        return tests_DB.check_identical_in_tests(data['id'],data['name'])


@app.route('/_check_identical_in_new_tests',methods=['POST'])
def check_identical_in_new_tests():
    if request.method=='POST':
        data=request.json
        return tests_DB.check_identical_in_new_tests(data['name'])


@app.route('/_reset_data_users_enabling_test',methods=['POST'])
def reset_data_users_enabling_test():
    if request.method=='POST':
        data=request.json
        tests_DB.reset_data_users_enabling_test(data['id'])
        return "success"


@app.route('/_get_count_questions',methods=['POST'])
def get_count_questions():
    if request.method=='POST':
        data=request.json
        return tests_DB.get_count_questions(data['id'])


@app.route('/_edit_status_test',methods=['POST'])
def edit_status_test():
    if request.method=='POST':
        data=request.json
        tests_DB.edit_status_test(data['id'],data['status'])
        return "0"

