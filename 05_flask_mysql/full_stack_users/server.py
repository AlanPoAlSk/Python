from flask import Flask , render_template , redirect , request

app = Flask(__name__)

from users import User

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


if __name__ == '__main__':
    app.run(debug=True)