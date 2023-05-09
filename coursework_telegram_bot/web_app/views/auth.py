from flask import redirect, url_for, request, render_template
from flask_login import login_required, logout_user, login_user
from web_app import app, User


@app.route('/logout')
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))


@app.route('/login', methods=['get', 'post'])
def login_page():
    if request.method == 'POST' and 'login_user' in request.form and 'password_user' in request.form:
        login = request.form.get('login_user')
        password = request.form.get('password_user')
        if login and password:
            user = User.query.filter_by(login=login, password=password).first()
            print(user)
            if user:

                login_user(user)
                next_page = request.args.get('next')
                if next_page is None:
                    return redirect('tests')

                return redirect(next_page)
            else:
                return render_template("auth.html")
    return render_template("auth.html")


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response

