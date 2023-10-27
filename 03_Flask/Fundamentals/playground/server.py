from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def intro():
    return "Ready?"

@app.route('/play')
def three():
    return render_template('index1.html', number =3)

@app.route('/play/<int:x>')
def numchange(x):
    return render_template('index2.html', x = x)

@app.route('/play/<int:y>/<color>')
def numcolchange(y,color):
    return render_template('index3.html', y=y, color=color)

if __name__=="__main__":  
    app.run(debug=True)