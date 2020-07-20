from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# DB login info to connect to pythonanywhere db
DB_USER = 'dogsdream'
DB_PASS = 'group3osu'
DB_HOST = 'dogsdream.mysql.pythonanywhere-services.com'
DB_PORT = '3306'
DATABASE = 'dogsdream$dogsdream'

# DB_USER = 'root'
# DB_PASS = '1234'
# DB_HOST = '127.0.0.1'
# DB_PORT = '3306'
# DATABASE = 'dogsdream'


# Set up flask app to connect to db
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql://{}:{}@{}:{}/{}'.\
    format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# initialize database
db = SQLAlchemy(app)

# # initialize migrate object to allow for easily updating dbs with models
# migrate = Migrate(app, db)
#
#
# # SQLAlchemy models for all tables in app
# class Sitters(db.Model):
#     __tablename__ = "Sitters"
#     id = db.Column(db.Integer, primary_key=True)
#     firstName = db.Column(db.String(256), nullable=False)
#     lastName = db.Column(db.String(256), nullable=False)
#     phoneNumber = db.Column(db.Integer, nullable=False)
#     streetAddress = db.Column(db.String(256), nullable=False)
#     city = db.Column(db.String(128), nullable=False)
#     state = db.Column(db.String(2), nullable=False)
#     zipCode = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String(256), nullable=False)
#     password = db.Column(db.String(256), nullable=False)
#
#
# class PetOwners(db.Model):
#     __tablename__ = "PetOwners"
#     id = db.Column(db.Integer, primary_key=True)
#     firstName = db.Column(db.String(256), nullable=False)
#     lastName = db.Column(db.String(256), nullable=False)
#     phoneNumber = db.Column(db.Integer, nullable=False)
#     streetAddress = db.Column(db.String(256), nullable=False)
#     city = db.Column(db.String(128), nullable=False)
#     state = db.Column(db.String(2), nullable=False)
#     zipCode = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String(256), nullable=False)
#     password = db.Column(db.String(256), nullable=False)
#     dogs = db.relationship('Dogs')
#
#     def __repr__(self):
#         return '<Dogs %r>' % self.id
#
#
# class DogSizes(db.Model):
#     __tablename__ = "DogSizes"
#     id = db.Column(db.Integer, primary_key=True)
#     size = db.Column(db.String(256), nullable=False)
#     dog = db.relationship('Dogs')
#
#     def __repr__(self):
#         return'<DogSizes %r>' % self.id
#
#
# class Dogs(db.Model):
#     __tablename__ = "Dogs"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     size = db.Column(db.Integer, db.ForeignKey(DogSizes.id), nullable=False)
#     petOwner = db.Column(db.Integer,
#                          db.ForeignKey(PetOwners.id), nullable=False)
#     service = db.relationship('Services')
#
#     def __repr__(self):
#         return '<Dogs %r>' % self.id
#
#
# class ServiceTypes(db.Model):
#     __tablename__ = "ServiceTypes"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)
#     service = db.relationship('Services')
#
#     def __repr__(self):
#         return '<ServiceTypes %r>' % self.id
#
#
# class FrequencyOfServices(db.Model):
#     __tablename__ = "FrequencyOfServices"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)
#     service = db.relationship('Services')
#
#     def __repr__(self):
#         return '<FrequencyOfServices %r>' % self.id
#
#
# class Certifications(db.Model):
#     __tablename__ = "Certifications"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)
#     date = db.Column(db.DateTime, nullable=False)
#
#     def __repr__(self):
#         return '<Certifications %r>' % self.id
#
#
# class Vaccines(db.Model):
#     __tablename__ = "Vaccines"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)
#     date = db.Column(db.DateTime, nullable=False)
#
#     def __repr__(self):
#         return '<Vaccines %r>' % self.id
#
#
# class Services(db.Model):
#     __tablename__ = "Services"
#     id = db.Column(db.Integer, primary_key=True)
#     startDate = db.Column(db.DateTime, nullable=False)
#     time = db.Column(db.DateTime, nullable=False)
#     endDate = db.Column(db.DateTime, nullable=False)
#     serviceType = db.Column(db.Integer,
#                             db.ForeignKey(ServiceTypes.id),
#                             nullable=False)
#     frequency = db.Column(db.Integer,
#                           db.ForeignKey(FrequencyOfServices.id),
#                           nullable=False)
#     sitter = db.Column(db.Integer,
#                        db.ForeignKey(Sitters.id),
#                        nullable=False)
#     dog = db.Column(db.Integer,
#                     db.ForeignKey(Dogs.id),
#                     nullable=False)
#     # Pet owner will be fetched from Dog id but this is used for HTML testing
#     owner = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return '<Services %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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
        if request.form['username'] == 'admin' and \
           request.form['password'] == 'admin':
            return redirect(url_for('administrator'))
        else:
            if request.form['username'] == 'sitter' and \
                    request.form['password'] == 'sitter' and request.form['profiles'] == 'sitter':
                return redirect(url_for('sitter_profile'))
            elif request.form['username'] == 'owner' and \
                    request.form['password'] == 'owner' and request.form['profiles'] == 'owner':
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
def owner_profile():
    # if request.method == 'POST':
    #     print(request.form)
    #     if request.form.get('name') == 'schedule':
    #         return render_template('owner/add_jobs.html')
    #     elif request.form == 'view_appointments':
    #         return render_template('owner/view_appointments.html')
    #     elif request.form == 'add_dogs':
    #         return render_template('owner/add_dogs.html')
    #     elif request.form == 'view_dogs':
    #         return render_template('owner/view_dogs.html')
    # else:
    #     # Fake person to make sure person can be displayed
    #     kc = PetOwners(id='1', firstName='KC', lastName='Willard',
    #                    phoneNumber='(111)111-1111',
    #                    streetAddress='123 dog lane', city='Portland',
    #                    state='OR', zipCode='97266',
    #                    email='willarke@oregonstate.edu',
    #                    password='******',
    #                    dogs=[Dogs(name='Arya'), Dogs(name='Fluffy')])
    #
        return render_template('owner/profile.html')


@app.route('/owner/view_appointments', methods=['POST', 'GET'])
def view_appointments():
    return render_template('owner/view_appointments.html')


@app.route('/owner/dogs', methods=['POST', 'GET'])
def dogs():
    return render_template('owner/dogs.html')


@app.route('/owner/add_dogs', methods=['POST', 'GET'])
def add_dog():
    # if request.method == 'POST':
    #    dog_name = request.form['name']
    #    dog_age = request.form['age']
    #    dog_size = request.form['size']
    #    dog_owner = 'Admin'
    #    new_dog = Dogs(name = dog_name,age=dog_age,petOwner=dog_owner)

    return render_template('owner/add_dogs.html')


@app.route('/owner/view_dogs', methods=['GET'])
def view_dogs():
    # arya = Dogs(id='0', name='Arya',
    #             age='8', size='Medium',
    #             petOwner='KC')
    # fluffy = Dogs(id='0', name='Fluffy',
    #               age='3', size='Very Small',
    #               petOwner='KC')
    # dogs = [arya, fluffy]
            
    return render_template('owner/view_dogs.html')

@app.route('/owner/vaccines', methods=['POST', 'GET'])
def vaccines():

    return render_template('owner/vaccines.html')

@app.route('/sitter/view_jobs', methods=['GET'])
def view_jobs():
    # job1 = Services(startDate='1/1/2020', time='12:00:00', endDate='1/2/2020',
    #                 serviceType='Walk', frequency='Weekly',
    #                 sitter='Jake', dog='Arya', owner='KC')
    # job2 = Services(startDate='5/22/2020', time='19:00:00', endDate='5/25/2020',
    #                 serviceType='Watch', frequency='Once',
    #                 sitter='Jake', dog='Fluffy', owner='Gosia')
    # jobs = [job1, job2]
    return render_template('sitter/view_jobs.html')


@app.route('/sitter/pickup_job', methods=['POST', 'GET'])
def pickup_job():
    return render_template('sitter/pickup_job.html')


@app.route('/sitter/profile', methods=['POST', 'GET'])
def sitter_profile():
    return render_template('sitter/profile.html')


@app.route('/sitter/certifications', methods=['POST', 'GET'])
def certifications():
    # cert1 = Certifications(id='0', name='Pro Walker')
    # cert2 = Certifications(id='1', name='Pro Watcher')
    # cert3 = Certifications(id='1', name='Pro Trainer')
    #
    # certs = [cert1, cert2, cert3]
    return render_template('sitter/certifications.html')


@app.route('/sitter/delete', methods=['GET'])
def delete_sitter():
    # delete this sitter from database
    return redirect(url_for('index'))


@app.route('/sitter/profile_update', methods=['POST', 'GET'])
def profile_update():
    return render_template('sitter/profile_update.html')

@app.route('/owner/profile_update', methods=['POST', 'GET'])
def profile_update2():
    return render_template('owner/profile_update.html')



@app.route('/administrator/administrator', methods=['POST', 'GET'])
def administrator():
    return render_template('administrator/administrator.html')


@app.route('/administrator/all_sitters', methods=['POST', 'GET'])
def all_sitters():
    return render_template('administrator/all_sitters.html')


@app.route('/administrator/full_certifications', methods=['POST', 'GET'])
def full_certifications():
    return render_template('administrator/full_certifications.html')


@app.route('/administrator/all_jobs', methods=['POST', 'GET'])
def all_jobs():
    return render_template('administrator/all_jobs.html')


@app.route('/administrator/frequency', methods=['POST', 'GET'])
def frequency():
    return render_template('administrator/frequency.html')


@app.route('/administrator/types', methods=['POST', 'GET'])
def types():
    return render_template('administrator/types.html')


@app.route('/administrator/dog_sizes', methods=['POST', 'GET'])
def dog_sizes():
    return render_template('administrator/dog_sizes.html')

@app.route('/administrator/all_vaccines', methods=['POST', 'GET'])
def all_vaccines():
    return render_template('administrator/all_vaccines.html')


@app.route('/administrator/all_dogs', methods=['POST', 'GET'])
def all_dogs():
    return render_template('administrator/all_dogs.html')

@app.route('/administrator/all_owners', methods=['POST', 'GET'])
def all_owners():
    return render_template('administrator/all_owners.html')


if __name__ == '__main__':
    app.run(debug=True)
