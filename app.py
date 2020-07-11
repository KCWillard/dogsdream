from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


DB_USER = 'cs340_willarke'
DB_PASS = '9661'
DB_HOST = 'classmysql.engr.oregonstate.edu'
DB_PORT = '3306'
DATABASE = 'cs340_willarke'


# Set up flask app to connect to db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.\
    format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)

# initialize database
db = SQLAlchemy(app)


# Create models
class Sitters(db.Model):
    sitterId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(256), nullable=False)
    lastName = db.Column(db.String(256), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    streetAddress = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String, nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/owner/')
def owner():
    return render_template('owner/owner.html')


@app.route('/owner/view', methods=['POST', 'GET'])
def view():
    return render_template('owner/view.html')


@app.route('/owner/add-dog', methods=['POST', 'GET'])
def add_dog():
    return render_template('owner/add-dog.html')


@app.route('/sitter/')
def sitter():
    return render_template('sitter/sitter.html')


@app.route('/sitter/add-job')
def add_job():
    return render_template('sitter/add-job.html')


@app.route('/sitter/view-job')
def view_job():
    return render_template('sitter/view-job.html')


if __name__ == '__main__':
    app.run(debug=True)
