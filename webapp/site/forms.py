from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class SearchForm(FlaskForm):
    request = StringField('host:by', validators=[DataRequired()], render_kw={"class": "form-control form-control-dark", "placeholder": "host:by"})
    submit = SubmitField('Найти', render_kw={"class": "btn btn-primary"})
