import os.path
from flask import Flask, render_template, redirect, request, jsonify, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
# from flask_bootstrap import Bootstrap
import form.logon as log_form


basedir = os.path.abspath(os.path.dirname(__file__)) + '/db'
print(basedir)

app = Flask(__name__)
app.config['SECRET_KEY'] = "PEGASUS_SECRET_KEY_c1j2f3k6n2v4i5r1j2n2r394o1i2f4h6e1c2e9i0k2c8h5eih4iv3jjv1jv2nir1o"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "pegasus.db")


import db.db_requests as reqs
from db.db_models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def includes():
    return render_template('includes.html', header_key="includes",
                           username=current_user.user, link_vk=current_user.pers_data)


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect('/')
    reg_form = log_form.RegisterForm()
    if reg_form.validate_on_submit():
        user_login = reg_form.login.data
        password = reg_form.password.data
        vk_link = reg_form.vk_link.data
        result = reqs.user_add(user_login, password, vk_link)
        if result == reqs.MessagesEnum.success:
            return redirect('/login')
        else:
            flash("Пользователь уже существует", "error")
            return render_template('registration.html', header_key="registration", form=reg_form)
    return render_template('registration.html', header_key="registration", form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    login_form = log_form.LoginForm()
    if login_form.validate_on_submit():
        user_login = login_form.login.data
        password = login_form.password.data
        result = reqs.user_get(user_login, password)
        if result:
            login_user(result, remember=login_form.remember.data)
            return redirect('/')
        else:
            flash("Неправильное имя пользователя или пароль", "error")
            return render_template('login.html', header_key="login", form=login_form)
    return render_template('login.html', header_key="login", form=login_form)


@app.route('/', methods=['CALENDAR', 'CREATE_REQ', 'DATE_REQS'])
@login_required
def includes_request():
    print(request.method)
    if request.method == 'DATE_REQS':
        res = reqs.is_exists_request(request.form)
        return jsonify(res)
    if request.method == 'CALENDAR':
        res = reqs.calendar_request_get(request.form)
        return jsonify(res)
    if request.method == 'CREATE_REQ':
        res = reqs.calendar_request_set(request.form)
        print(res)
        return jsonify(res)
    print("Unexpected error")
    return "Unexpected error"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/personal_area')
@login_required
def personal_area():
    return render_template('personal_area.html', header_key="personal_area",
                           form=reqs.user_list_of_request(current_user.user))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
