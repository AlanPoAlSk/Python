from flask import Flask , render_template ,request, redirect, session

app = Flask(__name__)
app.secret_key = 'yet'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user' , methods=['POST'])
def login():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    session['username'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(request.form) 
    return render_template('return.html')


if __name__=="__main__":  
    app.run(debug=True)