from flask import render_template , redirect , request

from full_stack_users import app

from full_stack_users.config.mysqlconnection import connectToMySQL

from full_stack_users.models.user import User

@app.route('/')
def index():
    
    users = User.get_all()
    
    return render_template('read.html' , users = users)

@app.route('/new_user')
def new_user():
    return render_template('create.html')


@app.route('/create_user' , methods = ['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route ('/save_user' , methods=['POST'])
def save_user():
    User.edit(request.form)
    return redirect('/')


@app.route('/show/<int:id>')
def show(id):
    return render_template('show.html', user=User.get_one(id))

@app.route('/edit/<int:id>')
def edit_user(id):
    return render_template('edit.html', user=User.get_one(id))

    
    
@app.route('/user/edit/id', methods=['POST'])
def edit():
    User.edit(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')