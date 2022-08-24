from flask import Flask,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from forms import ContactForm


app = Flask(__name__,template_folder='templates',static_folder='static')

app.config['SECRET_KEY'] = 'jLFhJFfihO'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)


class Contacts(db.Model):

    __tablename__ = 'Contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    message = db.Column(db.Text)

    def __init__(self,name,email,message):
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f"The person with email id {self.email} has sent a message as {self.message}"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sayhi',methods=['GET', 'POST'])
def sayhi():

    try:
        form = ContactForm()

        if form.validate_on_submit():
            
            name = form.name.data
            email = form.email.data
            message = form.message.data

            new_message = Contacts(name,email,message)
            db.session.add(new_message)
            db.session.commit()

            return redirect(url_for('thankyou'))

        return render_template('sayhi.html',form=form)

    except:
        error = "OOPS! Some error occurred! Please try again after some time. Shivam is working on the issue."
        return render_template('error.html',error=error)

@app.route('/thankyou',methods=['GET','POST'])
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)