import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message


from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
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


