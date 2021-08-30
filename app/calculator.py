from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class Calculator(FlaskForm):
	number = IntegerField("Input number", validators=[DataRequired()])
	submit = SubmitField("Calculate!")