from flask import render_template , redirect , request

from dojos_and_ninjas_app import app

from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app.models.dojo import Dojo


@app.route('/')
def dojos():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    
    dojos = Dojo.get_all()
    
    return render_template('all_dojos.html', dojos = dojos)



@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')


