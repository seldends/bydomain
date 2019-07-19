from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "в"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "в"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Имя пользователя"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control", "placeholder": "example@email.com"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Пароль"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control", "placeholder": "Повторите пароль"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    # def validate_username(self, username):
    #     users_count = users.find_one({ "username": username })
    #     if users_count is not None:
    #         raise ValidationError('Пользователь с таким именем уже зарегистрирован')

    # def validate_email(self, email):
    #     users_count = users.find_one({ "email": email })
    #     if users_count is not None:
    #         raise ValidationError('Пользователь с такой почтой уже зарегистрирован')

