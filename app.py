import os.path
from flask import Flask, render_template, redirect, request, jsonify
# from flask_bootstrap import Bootstrap
import form.logon as log_form


basedir = os.path.abspath(os.path.dirname(__file__)) + '/db'
print(basedir)

app = Flask(__name__)
app.config['SECRET_KEY'] = "PEGASUS_SECRET_KEY_c1j2f3k6n2v4i5r1j2n2r394o1i2f4h6e1c2e9i0k2c8h5eih4iv3jjv1jv2nir1o"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "pegasus.db")


# import db.db_models
import db.db_requests as reqs


@app.route('/')
def includes():
    return render_template('includes.html')


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    reg_form = log_form.RegisterForm()
    if reg_form.is_submitted():
        login = reg_form.login.data
        password = reg_form.password.data
        vk_link = reg_form.vk_link.data
        print(login, password, vk_link)
        return redirect('/')
    return render_template('registration.html', form=reg_form)


@app.route('/', methods=['CALENDAR', 'CREATE_REQ'])
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
