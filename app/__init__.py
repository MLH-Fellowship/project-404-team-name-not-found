import datetime
import os
import re
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from playhouse.shortcuts import model_to_dict
from peewee import *

from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user= os.getenv ("MYSQL_USER"),
    password= os.getenv ("MYSQL_PASSWORD") ,
    host= os.getenv("MYSQL_HOST"),
    port= 3306)

print(mydb)

class TimelinePost (Model) :
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])



app.config.update(dict(
    MAIL_SERVER = 'smtp.mail.yahoo.com',
    MAIL_PORT = '465',
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'form.responses@yahoo.com',
    MAIL_PASSWORD = "adydfilgvbjovvqe",
    MAIL_DEBUG = True
))
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))
    

@app.route('/travels')
def travels():
    return render_template('travels.html', title="Oh, the places I've Been!", url=os.getenv("URL"))

@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method=="POST":
        first= str(request.form["first"])
        last=str(request.form["last"])
        email=str(request.form["email"])
        subject= str(request.form["subject"])
        message= str(request.form["message"])
        msg = Message(subject, sender='form.responses@yahoo.com', recipients=['smrithic@terpmail.umd.edu'])
        sendthis= first + ' ' + last + ' sent you a message, Smrithi!' + '\n' + 'Message: ' + message + '\n'+ "Respond at "+ email
        msg.body=sendthis
        mail.send(msg)
    return render_template('contact.html', title="Get in Touch!", url=os.getenv("URL"))

@app.route('/timeline')
def timeline():
    return render_template('timeline.html',title="Timeline")


@app.route('/api/timeline_post', methods=[ 'POST' ])
def post_time_line_post():
    if not 'name' in request.form or len(request.form['name']) == 0:
        return "Invalid name", 400

    if not 'content' in request.form or len(request.form['content']) == 0:
        return "Invalid content", 400
    

    if not 'email' in request.form or len(request.form['email']) == 0:
        return "Invalid email", 400

    name = request.form['name']
    email = request.form['email']
    content = request.form['content']

    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if not re.match(regex, email):
        return "Invalid email", 400
    
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)
    

        

    

@app.route('/api/timeline_post', methods=[ 'GET'])
def get_time_line_post():
    return {
        'timelineposts': [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=[ 'DELETE'])

def delete_time_line_post():
    todelete=TimelinePost.select().order_by(TimelinePost.id.desc()).get()
    TimelinePost.delete_by_id(todelete.id)
    return 'deleted' + ' ' + str(todelete.id)
