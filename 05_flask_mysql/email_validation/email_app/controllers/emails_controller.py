from flask import render_template , redirect , request

from email_app import app

from email_app.models.email_model import Email


@app.route('/')
def home():
    return render_template('create.html')


@app.route('/create', methods = ['POST'])
def create_email():
    
    if not Email.validate(request.form):
        return redirect('/')
    else:
        Email.create(request.form)
        return redirect('/show')

@app.route('/show')
def show():
    emails = Email.show()
    return render_template('show.html' ,emails = emails)

@app.route('/delete/<int:id>')
def delete(id):
    Email.delete(id)
    return redirect('/show')