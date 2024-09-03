from flask import Flask, render_template ,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reg')
def ht():
    return render_template("reg.html")

@app.route('/sub', methods=['POST'])
def sumbit():
    #form la irunthu get panrom demo 
    name1=request.form['name1']
    name2=request.form['name2']
    gender1=request.form['gender']
    gender2=request.form['gender']
    email=request.form['email']
    phonenumber=request.form['phonenumber']
    address=request.form['address']
    school=request.form['sc-name']
    year=request.form['year']
    yes=request.form['yes']
    no=request.form['no']
    return name1+""+name2

if __name__ =="__main__":
    app.run(debug=True)