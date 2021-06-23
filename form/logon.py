from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    login = StringField('username', validators=[InputRequired(), Length(min=4, max=16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    login = StringField('Логин:', validators=[InputRequired(), Length(min=4, max=16)])
    password = PasswordField('Пароль:', validators=[InputRequired(), Length(min=8, max=80)])
    vk_link = StringField('Ссылка на профиль Вконтакте:', validators=[InputRequired(), Length(min=7, max=31)])
