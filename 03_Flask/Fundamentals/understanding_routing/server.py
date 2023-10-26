from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def response(name):
    print(str(name))
    return 'Hello ' +  str(name)

@app.route('/<num>/<name>')
def num_x_name(num,name):
    return int(num) * ( " " + str(name))

# if app.route != 'dojo' and app.route != 'say' and app.route != 'num':
#     print('Error. Sorry, try again')

if __name__=="__main__":  
    app.run(debug=True)
    
