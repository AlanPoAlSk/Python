from flask import Flask , render_template , request , redirect , session
import random
app = Flask(__name__)
app.secret_key = "luck"

@app.route('/')
def home():
    if "number" not in session:
        session['number'] = random.randint(1,100)
    return render_template('index1.html')

@app.route('/play' , methods=['POST'])
def play():
    session['play'] = int(request.form['play'])
    return redirect('/')

@app.route('/reset')
def replay():
    session.clear()
    return redirect('/')


if __name__ =='__main__':
    app.run(debug=True)