from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


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


class ChangePasswordForm(FlaskForm):
    password_old = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Пароль"})
    password_new1 = PasswordField('Новый пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Новый пароль"})
    password_new2 = PasswordField('Повторите пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Повторите пароль"})
    submit = SubmitField('Обновить', render_kw={"class": "btn btn-primary"})
