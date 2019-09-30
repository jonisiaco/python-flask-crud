from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Send')

class Edit(FlaskForm):
	id = HiddenField('id', validators=[DataRequired()])
	title = StringField('Title', validators=[DataRequired()])
	content = StringField('Content', widget=TextArea())
	submit = SubmitField('Update')