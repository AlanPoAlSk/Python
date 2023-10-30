from flask import Flask , render_template ,session, request , redirect 

app = Flask(__name__)
app.secret_key = "number"



@app.route('/')
def start():
    count_num = session.get("count_num" , 1)
    if "count_num" not in session:
        session["count_num"] = 2
    else:
        session["count_num"] += 1
    print(f'Count Streak : {count_num}')
    return render_template("index.html", count_num = count_num)

@app.route('/count' , methods= ['POST'])
def click():
    return redirect('/')


@app.route('/destroy_session' , methods = ['POST'])
def restart():
    session.pop('count_num')
    print('Reset')
    return redirect('/')






if __name__=="__main__":  
    app.run(debug=True)