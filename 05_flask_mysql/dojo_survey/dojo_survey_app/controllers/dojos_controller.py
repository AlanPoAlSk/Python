from flask import render_template , redirect , request , session

from dojo_survey_app import app

from dojo_survey_app.models.dojo_model import Dojo




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_post' , methods = ['POST'])
def create_post():
    if not Dojo.validate_post(request.form):
        return redirect('/')
    Dojo.create_post(request.form)
    return redirect('/show')

@app.route('/show')
def show():
    post = Dojo.show()
    return render_template('show_post.html', post = post)
