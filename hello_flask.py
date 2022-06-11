from crypt import methods
from unicodedata import name
from flask import Flask, redirect, render_template, request,url_for,session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Registration.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)
app.secret_key = "secretkey"
app.permanent_session_lifetime = timedelta(seconds=40)
app = Flask(__name__)


class Registration(db.Model):
    id = db.Column('id',db.Integer, primary_key=True)
    username = db.Column('Username',db.String(30), unique=True, nullable=False)
    password = db.Column('Password',db.String(30), unique=True, nullable=False)

db.create_all()

@app.route("/home", methods=['POST', 'Get'])
def registration():
    if request.method == 'POST':
        name = request.form ['name']
        password = request.form ['password']
        session ['name']= name
        session ['password'] = password
        return redirect (url_for('name','password'))
        
    else:
        if "name" in session:
            return redirect(url_for("name"))
        elif "password" in session:
            return redirect(url_for("password"))
        return render_template ("reg.html")
    
@app.route("/login", methods=['POST', 'Get'])
def login():
    if request.method == 'POST':
        name = request.form ['name']
        password = request.form ['password']
        session ['name']= name
        session ['password']=password
        return redirect (url_for('name','password'))
    else:
        if "name" in session:
            return redirect(url_for("name"))
        elif "password" in session:
            return redirect(url_for("password"))
            
        return render_template ("log.html")    
    
 
    
if __name__ == '__main__':
    app.run(debug=True)
           
# from flask import Flask
# app = Flask (__name__)

# @app.route('/')  
# def Home():
#     return "for devops"

# if __name__=='__main__':
#     app.run(debug=True)