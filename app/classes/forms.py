# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

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

class SurveyForm(FlaskForm):
    # subject = StringField('Subject', validators=[DataRequired()])
    # content = TextAreaField('Comment', validators=[DataRequired()])
    fluentlang = TextAreaField('Fluent Languages', validators=[DataRequired()])
    homelang = TextAreaField('Home Languages', validators=[DataRequired()])
    classlang = TextAreaField('Class Languages', validators=[DataRequired()])
    parentlang = TextAreaField('Parent Languages', validators=[DataRequired()])
    submitl = SubmitField()
    # Participants will be shown an audio sample:
    # 	50%:
    # 	Two different random languages (x and y) will be selected.
    # 	Participants will then be told the sample is from one language and given the audio sample from the other.
    # 	You will now listen to an audio sample from x:
    # 	[audio sample y]
    
    # 	50%:
    # 	A random language will be selected
    # 	They will be told what language it is and be given the audio sample in that language.
    # Now please listen to an audio sample from the language [language name].
    # [audio sample]
    familiarity = IntegerRangeField('Familiarity', validators=[DataRequired()])
    beauty = IntegerRangeField('Beauty', validators=[DataRequired()])
    melody = IntegerRangeField('Melody', validators=[DataRequired()])
    softness = IntegerRangeField('Softness', validators=[DataRequired()])
    orderliness = IntegerRangeField('Orderliness', validators=[DataRequired()])
    sweetness = IntegerRangeField('Sweetness', validators=[DataRequired()])
    submit = SubmitField()
    age = SelectField('Age', validators=[DataRequired()])
    gender = TextAreaField('Gender', validators=[DataRequired()])
    ethnicity = TextAreaField('Ethnicity', validators=[DataRequired()])
    submitd = SubmitField()