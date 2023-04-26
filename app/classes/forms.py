
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import widgets, StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, SelectMultipleField
from wtforms.fields.html5 import IntegerRangeField

langChoices = [('English','English'),('Russian','Russian'),('Spanish','Spanish'),('German','German'),('French','French'),('Japanese','Japanese'),('Turkish','Turkish'),('Portuguese','Portuguese'),('Italian','Italian'),('Persian','Persian'),('Dutch, Flemish','Dutch, Flemish'),('Chinese','Chinese'),('Polish','Polish'),('Vietnamese','Vietnamese'),('Arabic','Arabic'),('Indonesian','Indonesian'),('Korean','Korean'),('Czech','Czech'),('Ukrainian','Ukrainian'),('Greek','Greek'),('Hebrew','Hebrew'),('Swedish','Swedish'),('Thai','Thai'),('Romanian','Romanian'),('Hungarian','Hungarian'),('Danish','Danish'),('Slovak','Slovak'),('Finnish','Finnish'),('Bulgarian','Bulgarian'),('Serbian','Serbian'),('Norwegian (Bokmål)','Norwegian (Bokmål)'),('Croatian','Croatian'),('Lithuanian','Lithuanian'),('Slovenian','Slovenian'),('Catalan','Catalan'),('Norwegian','Norwegian'),('Estonian','Estonian'),('Latvian','Latvian'),('Hindi','Hindi'),('Tamil','Tamil')]

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
    age = IntegerField('Age', validators=[DataRequired()])
    gender = TextAreaField('Gender', validators=[DataRequired()])
    ethnicity = TextAreaField('Ethnicity', validators=[DataRequired()])
    submit = SubmitField()