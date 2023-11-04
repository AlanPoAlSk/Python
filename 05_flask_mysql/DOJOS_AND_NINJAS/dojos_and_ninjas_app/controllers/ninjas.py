from flask import render_template , redirect , request

from dojos_and_ninjas_app import app

from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

from dojos_and_ninjas_app.models.ninja import Ninja
from dojos_and_ninjas_app.models.dojo import Dojo


@app.route('/add_ninja')
def add_ninja():
    return render_template('new_ninja.html',dojos = Dojo.get_all())

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/dojos')


@app.route("/list_ninjas/<int:dojo_id>")
def dojo_members(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    ninjas = Ninja.get_all_by_city(dojo_id)
    return render_template("ninjas_of_dojos.html", ninjas=ninjas, dojo=dojo)