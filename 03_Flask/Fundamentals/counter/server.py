from flask import Flask , render_template ,session, request , redirect 

app = Flask(__name__)
app.secret_key = "number"



@app.route('/')
def start():
    count_num = session.get("count_num", 1)
    print(f'Count Streak : {count_num}')
    return render_template("index.html", count_num = count_num)

@app.route('/count' , methods= ['POST'])
def click():
    if "count_num" in session:
        session["count_num"] += 1
    else:
        session["count_num"] = 1
    print(request.form)
    return redirect('/')


@app.route('/destroy_session' , methods = ['POST'])
def restart():
    session.pop('count_num')
    print('Reset')
    return redirect('/')






if __name__=="__main__":  
    app.run(debug=True)