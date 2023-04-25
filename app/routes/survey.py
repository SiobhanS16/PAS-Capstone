# These routes are an example of how to use data, forms and routes to create
# a forum where a blogs and comments on those blogs can be
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask_login.utils import login_required
from flask_login import current_user
from flask import render_template, flash, redirect, url_for
from app.classes.data import Survey
from app.classes.forms import SurveyForm1, SurveyForm2, SurveyForm3
import datetime as dt
import random

sampleList = [
    ["NW050","Hausa"], 
    ["NW049","Tagalog"], 
    ["NW051","Xhosa"], 
    ["NW037","Luganda"],
    ["NW034","Armenian"], 
    ["NW054","Welsh"],
    ["NW009","Dutch"],
    ["NW055","Norwegian"], 
    ["NW047","Greek"],
    ["NW015","Urdu"],
    ["NW064","Farsi"],
    ["NW056","French"],
    ["NW057","Italian"],
    ["NW052","Russian"],
    ["NW029","Serbian"],
    ["NW053","Maidu"],
    ["NW021","Arabic"],
    ["NW039","Akan"],
    ["NW024","Finnish"],
    ["NW035","Estonian"]
]


@app.route('/survey/new', methods=['GET', 'POST'])
@app.route('/survey_form', methods=['GET', 'POST'])
# @login_required
def surveyNew1():
    form = SurveyForm1()

    if form.validate_on_submit():

        newSurvey = Survey(
            fluentlang = form.fluentlang.data,
            homelang = form.homelang.data,
            classlang = form.classlang.data,
            parentlang = form.parentlang.data
        )
        newSurvey.save()

        return redirect(url_for('surveyNew2',sid=newSurvey.id))

    return render_template('surveyform.html',form=form)

@app.route('/survey2/new/<sid>', methods=['GET', 'POST'])
def surveyNew2(sid):
    form = SurveyForm2()
    editSurvey = Survey.objects.get(id=sid)
    randLang = sampleList[random.randint(0,len(sampleList)-1)]

    if form.validate_on_submit():
 
        editSurvey.update(
            familiarity = form.familiarity.data,
            beauty = form.beauty.data,
            melody = form.melody.data,
            softness = form.softness.data,
            orderliness = form.orderliness.data,
            sweetness = form.sweetness.data
            )

        return redirect(url_for('surveyNew3',sid=editSurvey.id))
    form.familiarity.data = 50
    form.beauty.data = 50
    form.melody.data = 50
    form.softness.data = 50
    form.orderliness.data = 50
    form.sweetness.data = 50

    return render_template('surveyform2.html',form=form,randLang=randLang)

@app.route('/survey3/new/<sid>', methods=['GET', 'POST'])
def surveyNew3(sid):
    form = SurveyForm3()
    editSurvey = Survey.objects.get(id=sid)

    if form.validate_on_submit():

        editSurvey.update(
            age = form.age.data,
            gender = form.gender.data,
            ethnicity = form.ethnicity.data
        )

        return redirect(url_for('survey',surveyID=editSurvey.id))

    return render_template('surveyform3.html',form=form)