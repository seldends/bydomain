from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class SearchForm(FlaskForm):
    request = StringField('Название сайта *2', validators=[DataRequired()], render_kw={"class": "form-control form-control-dark", "placeholder": "Название сайта *1"})
    submit = SubmitField('Найти', render_kw={"class": "btn btn-primary"})