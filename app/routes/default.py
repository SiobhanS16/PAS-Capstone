from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/survey_form')
def survey():
    return render_template('survey_form.html')

@app.route('/')
def index():
    return render_template('homepage.html')
