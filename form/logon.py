from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[InputRequired(), Length(min=4, max=16, message="От 4 до 16 символов")])
    password = PasswordField('Пароль', validators=[InputRequired(),
                                                   Length(min=8, max=80, message="От 8 до 80 символов")])
    remember = BooleanField('Запомнить меня')


class RegisterForm(FlaskForm):
    login = StringField('Логин:', validators=[InputRequired(), Length(min=4, max=16, message="От 4 до 16 символов")])
    password = PasswordField('Пароль:', validators=[InputRequired(),
                                                    Length(min=8, max=80, message="От 8 до 80 символов")])
    vk_link = StringField('Ссылка на профиль Вконтакте:',
                          validators=[InputRequired(), Length(min=7, max=31, message="От 7 до 31 символов")])
