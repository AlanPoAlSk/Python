from flask import Flask , render_template
app= Flask(__name__)


@app.route('/')
def intro():
    return render_template('index.html', x=8 , y=8)

@app.route('/4')
def resize():
    return render_template('index.html', x=4 , y=8 )

@app.route('/<int:x>/<int:y>')
def resizexy(x,y):
    return render_template('index3.html', x=x , y=y )

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def resizerecolor(x,y,color1,color2):
    return render_template('index4.html', x=x , y=y , color1=color1 , color2 = color2)

if __name__=="__main__":  
    app.run(debug=True)

