from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
# DB login info to connect to pythonanywhere db
app.config['MYSQL_HOST'] = 'dogsdream.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'dogsdream'
app.config['MYSQL_PASSWORD'] = 'group3osu'
app.config['MYSQL_DB'] = 'dogsdream$dogsdream'

mysql = MySQL(app)
Bootstrap(app)


# Add task
@app.route('/testdb', methods=['GET', 'POST'])
def testdb():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Persons''')
    rv = cur.fetchall()
    return str(rv)


@app.route('/createtables', methods=['GET', 'POST'])
def create_tables():
    connection = mysql.connection
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ServiceTypes ( 
    `id` INT(11) AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)   
)ENGINE=INNODB;
''')
    cur.execute('''CREATE TABLE IF NOT EXISTS FrequencyOfServices ( 
    `id` INT(11) AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)   
)ENGINE=INNODB;
''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Certifications ( 
    `id` INT(11) AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)     
)ENGINE=INNODB;
''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Vaccines ( 
    `id` INT(11) AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`) 
)ENGINE=INNODB;
''')
    cur.execute('''CREATE TABLE IF NOT EXISTS DogSizes( 
    `id` INT(11) AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)    
)ENGINE=INNODB;
     ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS PetOwners( 
    `id` INT(11) AUTO_INCREMENT,
    `firstName` VARCHAR(256) NOT NULL,
    `lastName` VARCHAR(255)  NOT NULL ,
    `phoneNumber` BIGINT(10) NOT NULL,
    `streetAddress` VARCHAR(256) NOT NULL,
    `city` VARCHAR(128) NOT NULL,
    `state` VARCHAR(2) NOT NULL,
    `zipCode` INT(5) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `password` VARCHAR(256) NOT NULL,    
    PRIMARY KEY(`id`)       
) ENGINE=INNODB;
''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Sitters ( 
    `id` INT(11) AUTO_INCREMENT,
    `firstName` VARCHAR(256) NOT NULL,
    `lastName` VARCHAR(255)  NOT NULL ,
    `phoneNumber` BIGINT(10) NOT NULL,
    `streetAddress` VARCHAR(256) NOT NULL,
    `city` VARCHAR(128) NOT NULL,
    `state` VARCHAR(2) NOT NULL,
    `zipCode` INT(5) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `password` VARCHAR(256) NOT NULL,    
    PRIMARY KEY(`id`)     
)ENGINE=INNODB;
''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Dogs ( 
    `id` INT(11) AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    `age` INT(2) NOT NULL,
    `dogSizesId` INT,
    `petOwnersId` INT NOT NULL, 
    PRIMARY KEY(`id`),
    CONSTRAINT dogs_ibfk_1 FOREIGN KEY (dogSizesId) REFERENCES DogSizes(id),
	 CONSTRAINT dogs_ibfk_2 FOREIGN KEY (petOwnersId) REFERENCES PetOwners(id)    
)ENGINE=INNODB;
''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Services ( 
    `id` INT(11) AUTO_INCREMENT,
	 `startDate` DATETIME NOT NULL,
	 `endDate` DATETIME NOT NULL,
	 `serviceTypesId` INT NOT NULL,
	 `frequencyOfServicesId` INT NOT NULL,
	 `sittersId` INT,
	 `dogsId` INT NOT NULL,
	 PRIMARY KEY(`id`), 
    CONSTRAINT services_ibfk_1 FOREIGN KEY (serviceTypesId) REFERENCES ServiceTypes(id),
	 CONSTRAINT services_ibfk_2 FOREIGN KEY (frequencyOfServicesId) REFERENCES FrequencyOfServices(id),
	 CONSTRAINT services_ibfk_3 FOREIGN KEY (sittersId) REFERENCES Sitters(id),
	 CONSTRAINT services_ibfk_4 FOREIGN KEY (dogsId) REFERENCES Dogs(id)    
)ENGINE=INNODB;
''')

    try:
        cur.execute('''INSERT INTO DogSizes (`name`)
VALUES
('Very Small <10lbs'),
('Small 11-20lbs'),
('Medium 21-49lbs'),
('Large 50-84lbs'),
('Very Large >85lbs');''')
        cur.execute('''INSERT INTO ServiceTypes (`name`)
VALUES
('Walk'),
('Watch'),
('Groom'),
('Train');''')

        cur.execute('''INSERT INTO FrequencyOfServices(`name`)
        VALUES
        ('Once'),
        ('Daily'),
        ('Weekly'),
        ('Bi-Weekly'),
        ('Monthly'),
        ('Yearly');''')

        cur.execute('''INSERT INTO Certifications(`name`)
        VALUES
        ('Dog Groomer'),
        ('Pro Walker'),
        ('Dog Watcher'),
        ('Pro Trainer');''')

        cur.execute('''INSERT INTO Vaccines(`name`)
        VALUES
        ('Rabies'),
        ('Parvo'),
        ('Distemper'),
        ('Hepatitis');''')

        cur.execute('''INSERT INTO PetOwners(firstName, lastName, phoneNumber, streetAddress, city, state, zipCode, email, `password`)
        VALUES
        ('John', 'Doe', '5411111111', '123 SE Woof Ln', 'Amarillo', 'TX', '25172', 'dog@dog.com', 'woofwoof'),
        ('Mary', 'Ellis', '5031111111', '123 SE Bark Ln', 'Lexington', 'KY', '23029', 'meow@dog.com', 'barkwoof'),
        ('Xavier', 'Brown', '5981111111', '123 SE Growl Ln', 'Corvallis', 'OR', '97333', 'dream@dog.com', 'woofbark');''')

        cur.execute('''INSERT INTO Sitters(firstName, lastName, phoneNumber, streetAddress, city, state, zipCode, email, `password`)
        VALUES
        ('Joe', 'Douglas', '1111111111', '123 SE Bitey Ln', 'Amarillo', 'TX', '25172', 'dog@dog.com', 'woofwoof'),
        ('Jeff', 'Duncan', '1231111111', '123 SE Yippie Ln', 'Lexington', 'KY', '23029', 'meow@dog.com', 'barkwoof'),
        ('Marisa', 'Hunter', '4561111111', '456 SE Growl Ln', 'Corvallis', 'OR', '97333', 'dream@dog.com', 'woofbark');''')

        cur.execute('''INSERT INTO Dogs(`name`, age, dogSizesId, petOwnersId)
        VALUES
        ('Fluffy', '3', '2', '1'),
        ('Scooby', '10', '4', '1'),
        ('Scrappy', '2', '3', '1'),
        ('Molly', '3', '2', '2'),
        ('Brandi', '6', '4', '2'),
        ('Koda', '11', '5', '3'),
        ('Arya', '8', '2', '2'),
        ('Tank', '4', '5', '3');''')

        cur.execute('''INSERT INTO Services(startDate, endDate, serviceTypesId, frequencyOfServicesId, sittersId, dogsId)
        VALUES
        ('2020/1/11', '2020/1/12', '1', '1', '1', '1'),
        ('2020/2/15', '2020/3/15', '2', '4', '1', '5'),
        ('2020/3/20', '2020/3/20', '3', '3', '3', '3'),
        ('2020/4/11', '2020/4/11', '1', '1', '2', '2'),
        ('2020/6/11', '2020/6/11', '4', '2', '2', '4');''')
        connection.commit()
        return 'Initialized tables'
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return 'Failed to init'

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
        if request.form['username'] == 'admin@admin.com' and \
                request.form['password'] == 'admin':
            return redirect(url_for('administrator'))
        # else:
        #     if request.form['username'] == 'sitter' and \
        #             request.form['password'] == 'sitter' and request.form['profiles'] == 'sitter':
        #         return redirect(url_for('sitter_profile'))
        #     elif request.form['username'] == 'owner' and \
        #             request.form['password'] == 'owner' and request.form['profiles'] == 'owner':
        #         return redirect(url_for('owner_profile'))
    return render_template('login.html', error=error)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    return render_template('administrator/add_user.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/owner', methods=['POST', 'GET'])
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
    return render_template('administrator/all_owners.html')


# @app.route('/owner/view_appointments', methods=['POST', 'GET'])
# def view_appointments():
#     return render_template('owner/view_appointments.html')


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


@app.route('/owner/update', methods=['GET', 'POST'])
def owner_update():
    return render_template('owner/profile_update.html')


@app.route('/owner/delete', methods=['GET', 'POST'])
def owner_delete():
    return render_template('administrator/all_owners.html')


@app.route('/dogs/update', methods=['GET', 'POST'])
def owner_dogs_update():
    return render_template('owner/add_dogs.html')


@app.route('/dogs/delete', methods=['GET', 'POST'])
def owner_dogs_delete():
    return render_template('administrator/all_dogs.html')


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
    return render_template('administrator/all_sitters.html')


@app.route('/sitter/update', methods=['POST', 'GET'])
def profile_update():
    return render_template('sitter/profile_update.html')


@app.route('/owner/profile_update', methods=['POST', 'GET'])
def profile_update2():
    return render_template('owner/profile_update.html')


@app.route('/administrator/administrator', methods=['POST', 'GET'])
def administrator():
    return render_template('administrator/administrator.html')


@app.route('/sitter', methods=['POST', 'GET'])
def all_sitters():
    return render_template('administrator/all_sitters.html')


@app.route('/certifications', methods=['POST', 'GET'])
def full_certifications():
    return render_template('administrator/full_certifications.html')


@app.route('/certification/delete', methods=['POST', 'GET'])
def certification_delete():
    return render_template('administrator/full_certifications.html')


@app.route('/certification/update', methods=['POST', 'GET'])
def certification_update():
    return render_template('administrator/update_certification.html')


@app.route('/certification/add', methods=['POST', 'GET'])
def certification_add():
    return render_template('administrator/add_certification.html')


@app.route('/jobs', methods=['POST', 'GET'])
def all_jobs():
    return render_template('administrator/all_jobs.html')


@app.route('/jobs/delete', methods=['POST', 'GET'])
def jobs_delete():
    return render_template('administrator/all_jobs.html')


@app.route('/jobs/update', methods=['POST', 'GET'])
def jobs_update():
    return render_template('administrator/all_jobs.html')


@app.route('/jobs/add', methods=['POST', 'GET'])
def jobs_add():
    return render_template('administrator/add_service.html')


@app.route('/jobs/filter', methods=['POST', 'GET'])
def jobs_filter():
    return render_template('administrator/all_jobs.html')


@app.route('/service_frequency', methods=['POST', 'GET'])
def frequency():
    return render_template('administrator/frequency.html')


@app.route('/service_frequency/delete', methods=['POST', 'GET'])
def frequency_delete():
    return render_template('administrator/frequency.html')


@app.route('/service_frequency/update', methods=['POST', 'GET'])
def frequency_update():
    return render_template('administrator/update_service_frequency.html')


@app.route('/service_frequency/add', methods=['POST', 'GET'])
def frequency_add():
    return render_template('administrator/add_service_frequency.html')


@app.route('/service_type', methods=['POST', 'GET'])
def types():
    return render_template('administrator/types.html')


@app.route('/service_type/delete', methods=['POST', 'GET'])
def service_delete():
    return render_template('administrator/types.html')


@app.route('/service_type/update', methods=['POST', 'GET'])
def service_update():
    return render_template('administrator/update_service_type.html')


@app.route('/service_type/add', methods=['POST', 'GET'])
def service_add():
    return render_template('administrator/add_service_type.html')


@app.route('/sizes', methods=['POST', 'GET'])
def dog_sizes():
    return render_template('administrator/dog_sizes.html')


@app.route('/sizes/delete', methods=['POST', 'GET'])
def sizes_delete():
    return render_template('administrator/dog_sizes.html')


@app.route('/sizes/update', methods=['POST', 'GET'])
def sizes_update():
    return render_template('administrator/update_dog_size.html')


@app.route('/sizes/add', methods=['POST', 'GET'])
def sizes_add():
    return render_template('administrator/add_dog_size.html')


@app.route('/vaccines', methods=['POST', 'GET'])
def all_vaccines():
    return render_template('administrator/all_vaccines.html')


@app.route('/vaccines/add', methods=['POST', 'GET'])
def add_vaccines():
    return render_template('administrator/add_vaccines.html')


@app.route('/vaccines/delete', methods=['POST', 'GET'])
def vaccines_delete():
    return render_template('administrator/all_vaccines.html')


@app.route('/vaccines/update', methods=['POST', 'GET'])
def vaccines_update():
    return render_template('administrator/update_vaccines.html')


@app.route('/vaccines/add', methods=['POST', 'GET'])
def vaccines_add():
    return render_template('administrator/all_vaccines.html')


@app.route('/administrator/all_dogs', methods=['POST', 'GET'])
def all_dogs():
    return render_template('administrator/all_dogs.html')


@app.route('/administrator/all_owners', methods=['POST', 'GET'])
def all_owners():
    return render_template('administrator/all_owners.html')


if __name__ == '__main__':
    app.run(debug=True)
