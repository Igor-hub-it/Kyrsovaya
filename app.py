import os.path
from flask import Flask, render_template, redirect, request, jsonify
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
    return render_template('includes.html')


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    reg_form = log_form.RegisterForm()
    if reg_form.validate_on_submit():
        user_login = reg_form.login.data
        password = reg_form.password.data
        vk_link = reg_form.vk_link.data
        result = reqs.user_add(user_login, password, vk_link)
        if result == reqs.MessagesEnum.success:
            return redirect('/login')
    return render_template('registration.html', form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = log_form.LoginForm()
    if login_form.validate_on_submit():
        user_login = login_form.login.data
        password = login_form.password.data
        result = reqs.user_get(user_login, password)
        if result:
            login_user(result, remember=False)
            return redirect('/')
    return render_template('login.html', form=login_form)


@app.route('/', methods=['CALENDAR', 'CREATE_REQ'])
@login_required
def includes_request():
    print(request.method)
    if request.method == 'CALENDAR':
        res = reqs.calendar_request_get(request.form)
        return jsonify(res)
    if request.method == 'CREATE_REQ':
        res = reqs.calendar_request_set(request.form)
        print(res)
        return jsonify(res)
    print("Unexpected error")
    return "Unexpected error"


if __name__ == "__main__":
    app.run()
