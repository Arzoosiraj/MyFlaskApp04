from flask import Flask,jsonify,request,redirect,url_for,session
app=Flask(__name__)

app.config['DEBUG']=True
app.config['SECRET_KEY']='Thisisasecret'
@app.route("/")
def index():
    return '<h1>Hello </h1>'
@app.route('/HOME',methods=['GET','POST'],defaults={'name':'default'})
@app.route('/HOME/<string:name>',methods=['GET','POST'])
def home(name):
    session['name']=name
    return '<h1>Hello {}</h1>'.format(name)

@app.route('/json')
def json():
    name=session['name']
    return jsonify({'key':'value','key2':'[1,2,3]',"name":'name'})


@app.route("/query")
def query():
    name=request.args.get('name')
    location=request.args.get('location')
    return 'hi {} you are on {}'.format(name,location)

@app.route("/theform",methods=['GET','POST'])
def theform():
    if request.method=='GET':
        return ''' <form method="POST" action='/theform'>
                <input type='text' name='name'>
                <input type='text' name='location'>
                <input type='submit' value='submit'>
                </form>
                '''
    else:
        name=request.form['name']
        # location=request.form['location']
        # return "hi {} you have submitted your form and you are from {}".format(name,location)
        return redirect(url_for('home', name=name))

# @app.route("/thepost",methods=['POST'])
# def thepost():
#     name=request.form['name']
#     location=request.form['location']
#     return "hi {} you have submitted your form and you are from {}".format(name,location)
@app.route("/processjson",methods=['POST','GET'])
def processjson():
    # data=request.get_json()
    # name=data["name"]
    # location=data["location"]
    # randomkey=data["randomkey"]
    name=session['name']
    return jsonify({"name":"name","location":"location","randomkey":"randomkey","name":"name"})
if __name__=='__main__':
    app.run(debug=True)
