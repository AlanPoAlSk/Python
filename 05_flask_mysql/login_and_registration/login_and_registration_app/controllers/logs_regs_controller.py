from flask import render_template , redirect , request , session

from login_and_registration_app import app

from login_and_registration_app.models.log_reg_model import Profile
from login_and_registration_app.models import log_reg_model




@app.route('/')
def website():
    return redirect('/homepage')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/registration', methods = ['POST'])
def create():
    if Profile.validate(request.form):
        # Profile.register(request.form)
        return redirect('/welcome')
    else :
        return redirect('/homepage')


@app.route('/login' , methods = ['POST'])
def log():
    logged_profile = Profile.login(request.form)
    if logged_profile:
        session['uuid'] = logged_profile.id
        
        return redirect('/welcome' )
    else :
        return redirect('/homepage')

@app.route('/welcome')
def welcome():
    if not 'uuid' in session:
        return redirect('/homepage')
    profile = Profile.show_name(session['uuid'])
    return render_template('welcome.html',profile = profile)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/homepage')