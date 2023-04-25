
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import widgets, StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField
from wtforms.fields.html5 import IntegerRangeField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class SurveyForm1(FlaskForm):
    fluentlang = TextAreaField('Fluent Languages', validators=[DataRequired()])
    homelang = TextAreaField('Home Languages', validators=[DataRequired()])
    classlang = TextAreaField('Class Languages', validators=[DataRequired()])
    parentlang = TextAreaField('Parent Languages', validators=[DataRequired()])
    submit = SubmitField()

class SurveyForm2(FlaskForm):
    familiarity = IntegerRangeField('Familiarity', validators=[DataRequired()])
    beauty = IntegerRangeField('Beauty', validators=[DataRequired()])
    melody = IntegerRangeField('Melody', validators=[DataRequired()])
    softness = IntegerRangeField('Softness', validators=[DataRequired()])
    orderliness = IntegerRangeField('Orderliness', validators=[DataRequired()])
    sweetness = IntegerRangeField('Sweetness', validators=[DataRequired()])
    submit = SubmitField()

class SurveyForm3(FlaskForm):
    age = SelectField('Age', validators=[DataRequired()])
    gender = TextAreaField('Gender', validators=[DataRequired()])
    ethnicity = TextAreaField('Ethnicity', validators=[DataRequired()])
    submit = SubmitField()