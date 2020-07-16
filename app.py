from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# DB login info to connect to pythonanywhere db
# DB_USER = 'dogsdream'
# DB_PASS = 'group3osu'
# DB_HOST = 'dogsdream.mysql.pythonanywhere-services.com'
# DB_PORT = '3306'
# DATABASE = 'dogsdream$dogsdream'

DB_USER = 'root'
DB_PASS = '1234'
DB_HOST = '127.0.0.1'
# DB_PORT = '3306'
DATABASE = 'dogsdream'


# Set up flask app to connect to db
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://{}:{}@{}/{}'.\
    format(DB_USER, DB_PASS, DB_HOST, DATABASE)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# initialize database
db = SQLAlchemy(app)

# initialize migrate object to allow for easily updating dbs with models
migrate = Migrate(app, db)


# SQLAlchemy models for all tables in app
class Sitters(db.Model):
    __tablename__ = "Sitters"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(256), nullable=False)
    lastName = db.Column(db.String(256), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    streetAddress = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)


class PetOwners(db.Model):
    __tablename__ = "PetOwners"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(256), nullable=False)
    lastName = db.Column(db.String(256), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    streetAddress = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    dogs = db.relationship('Dogs')

    def __repr__(self):
        return '<Dogs %r>' % self.id


class DogSizes(db.Model):
    __tablename__ = "DogSizes"
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(256), nullable=False)
    dog = db.relationship('Dogs')

    def __repr__(self):
        return'<DogSizes %r>' % self.id


class Dogs(db.Model):
    __tablename__ = "Dogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, db.ForeignKey(DogSizes.id), nullable=False)
    petOwner = db.Column(db.Integer,
                         db.ForeignKey(PetOwners.id), nullable=False)
    service = db.relationship('Services')

    def __repr__(self):
        return '<Dogs %r>' % self.id


class ServiceTypes(db.Model):
    __tablename__ = "ServiceTypes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    service = db.relationship('Services')

    def __repr__(self):
        return '<ServiceTypes %r>' % self.id


class FrequencyOfServices(db.Model):
    __tablename__ = "FrequencyOfServices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    service = db.relationship('Services')

    def __repr__(self):
        return '<FrequencyOfServices %r>' % self.id


class Certifications(db.Model):
    __tablename__ = "Certifications"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<Certifications %r>' % self.id


class Services(db.Model):
    __tablename__ = "Services"
    id = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    serviceType = db.Column(db.Integer,
                            db.ForeignKey(ServiceTypes.id),
                            nullable=False)
    frequency = db.Column(db.Integer,
                          db.ForeignKey(FrequencyOfServices.id),
                          nullable=False)
    sitter = db.Column(db.Integer,
                       db.ForeignKey(Sitters.id),
                       nullable=False)
    dog = db.Column(db.Integer,
                    db.ForeignKey(Dogs.id),
                    nullable=False)    
    
    def __repr__(self):
        return '<Services %r>' % self.id


# Set up route endpoints to serve webpages


class Persons(db.Model):
    __tablename__ = "Persons"
    ID = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<ID %r>' % self.ID


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/testdb')
# def testdb():
#     person = Persons(ID=3, LastName="Gosia")
#     db.session.add(person)
#     db.session.commit()
#     return 'Testing db connection'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            if request.form['profiles'] == 'sitter':
                return redirect(url_for('sitter_profile'))
            else:
                return redirect(url_for('owner_profile'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'a' or \
           request.form['password'] != 'a' \
           or request.form['fname'] != 'a' \
           or request.form['lname'] != 'a' \
           or request.form['phone'] != '1' \
           or request.form['address'] != 'a' \
           or request.form['city'] != 'a' \
           or request.form['state'] != 'AL' \
           or request.form['zip'] != '1':
            error = 'Invalid Credentials. Please try again.'
        else:
            if request.form['reg_type'] == 'sitter':
                return redirect(url_for('sitter_profile'))
            else:
                return redirect(url_for('owner_profile'))
    return render_template('register.html', error=error)


@app.route('/owner/profile', methods=['POST', 'GET'])
def owner():
    if request.method == 'POST':
        print(request.form)
        if request.form == 'schedule':
            return render_template('owner/add_jobs.html')
        elif request.form == 'view_appointments':
            return render_template('owner/view_appointments.html')
        elif request.form == 'add_dogs':
            return render_template('owner/add_dogs.html')
        elif request.form == 'view_dogs':
            return render_template('owner/view_dogs.html')
    else:
        # Fake person to make sure person can be displayed
        kc = PetOwners(id='1', firstName='KC', lastName='Willard',
                       phoneNumber='(111)111-1111',
                       streetAddress='123 dog lane', city='Portland',
                       state='OR', zipCode='97266',
                       email='willarke@oregonstate.edu',
                       password='******',
                       dogs=[Dogs(name='Arya'), Dogs(name='Fluffy')])
        #arya = Dogs(id='0', name='Arya',
        #            age='8', size=DogSizes(id=1),
        #            petOwner=PetOwners(id='1'))
        #fluffy = Dogs(id='0', name='Fluffy',
        #              age='3', size=DogSizes(id=1),
        #              petOwner=PetOwners(id='0'))
        #dogs = Dogs.query.filter_by(petOwner == kc.id).all()
        
        return render_template('owner/profile.html', owners=kc, dogs=kc.dogs,)


@app.route('/owner/view_appointments', methods=['POST', 'GET'])
def view():
    return render_template('owner/view_appointments.html')


@app.route('/owner/add_dogs', methods=['POST', 'GET'])
def add_dog():
    # if request.method == 'POST':
    #    dog_name = request.form['name']
    #    dog_age = request.form['age']
    #    dog_size = request.form['size']
    #    dog_owner = 'Admin'
    #    new_dog = Dogs(name = dog_name,age=dog_age,petOwner=dog_owner)

    return render_template('owner/add_dogs.html')


@app.route('/sitter/view_jobs', methods=['GET'])
def view_jobs():
    return render_template('sitter/view_jobs.html')


@app.route('/sitter/pickup_job', methods=['POST', 'GET'])
def pickup_job():
    return render_template('sitter/pickup_job.html')


@app.route('/sitter/profile', methods=['POST', 'GET'])
def sitter_profile():
    return render_template('sitter/profile.html')


@app.route('/sitter/certification', methods=['POST', 'GET'])
def certification():
    return render_template('sitter/certification.html')


if __name__ == '__main__':
    app.run(debug=True)
