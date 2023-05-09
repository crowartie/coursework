from flask import render_template
from flask_login import login_required
from web_app import app
from web_app.database import tests_DB, test_DB,courses_DB


@app.route("/tests/<id>")
@login_required
def test(id):
        status=test_DB.check_status_test(id)
        if(status['status']==0):
            return render_template("test.html", idTest=id, questions=test_DB.get_questions(id), nameTest=test_DB.get_test(id))
        else:
            return render_template("tests.html", tests=tests_DB.get_tests())


@app.route('/', methods=['get', 'post'])
@app.route('/tests', methods=['get', 'post'])
@login_required
def tests():
    return render_template("tests.html", tests=tests_DB.get_tests())

@app.route("/courses")
@login_required
def courses():
    return render_template("courses.html",courses=courses_DB.get_courses())

@app.route("/base")
@login_required
def base():
    return render_template("base.html")
