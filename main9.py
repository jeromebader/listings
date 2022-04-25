from flask import Flask, request, render_template, redirect, url_for, session, escape, g, flash, abort
import sqlalchemy
from config import Config, Emailserver
from forms import SignupForm, ListingForm
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session
from datetime import datetime
from datetime import date
import pymysql
import re
import os
import random
from models import User, Listing
from flask_paginate import Pagination, get_page_args,  get_page_parameter
from functools import wraps
from flask_mail import Mail, Message, email_dispatched
from passlib.hash import sha256_crypt


# Connecting to MySQL server at localhost using PyMySQL DBAPI
engine = create_engine('mysql+mysqldb://root:root@localhost/listingpage', echo=True)

machine = engine.connect()
## Database for Alchemy is prepared
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)

### ORM and classi MySQL querys

## Control inicio SQL Machine in Console
print(machine)
db = pymysql.connect(host='localhost',user='root',password='root',database='listingpage',charset='utf8mb4')

db.autocommit(True)
db.get_autocommit()

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)

# Secretkey in Config
app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object('config.Emailserver')
mail = Mail()
mail.init_app(app)



## Inition of app
if __name__ == '__main__':
    app.run()





## DECORATORS
### Login required Decorator for each relevant section
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            return f(*args, **kwargs)

        else:
            flash("!")
            return redirect(url_for('login'))

    return wrap


### Protection Admin views, Adminrights with roleid =
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            sessiondb = Session()
            username = session['username']
            result = sessiondb.query(User).filter_by(username=username, roleid=1).first()

            if result != None:

                return f(*args, **kwargs)

            else:
                flash("!")
                return redirect(url_for('login'))

    return wrap


### Is user active or isn't?
### Protection Admin views, Adminrights with roleid =1 otherwise user
def active_user(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            sessiondb = Session()
            username = session['username']
            result = sessiondb.query(User).filter_by(username=username, userstatus='active').first()

            if result != None:

                return f(*args, **kwargs)

            else:
                flash("Your are not activated yet, please activate account")
                return redirect(url_for('login'))

    return wrap


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404


## FUNCTIONS ESSENTIAL
def send_email(subject, sender, recipients, text_body, template, link, **kwargs):

    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.body = text_body
    msg.html = render_template(template, **kwargs, link=link)
    mail.send(msg)
    app.logger.debug(msg.subject)
    email_dispatched.connect(log_message)

def log_message(message, app):
    app.logger.debug(message.subject)

email_dispatched.connect(log_message)


### Routes
## Mainpage
@app.route('/',methods=['GET'])


def home():
    # Check if user is loggedin
    # User is loggedin show them the home page
    # selected_element = flask.ext.reqarg.get('elemento', type=int d)
    # seite = selected_element +1
    # pagina = int(seite)

    if 'loggedin' in session:
        eingeloggt = True
        results, pagination, page, nupages = items(session['uid'])
        print(session['uid'])
        return render_template('home.html', username=session['username'], results=results, pagination=pagination, msg3=page, page=page, nupages=nupages)
    else:
       results, pagination, page, nupages = start(0)
    return render_template('main.html', results=results, pagination=pagination, msg3=page, page=page, nupages=nupages)


#https://damyanon.net/post/flask-series-views/
#https://smirnov-am.github.io/flask-pagination-macro/




# VIEW of the Items, 20 per page
@app.route('/items/',methods=['GET'])
def items(uid):

    # #return redirect(url_for('login'))
    # cursor = db.cursor()
    # sql = "SELECT * FROM listings WHERE listing_id > 10 AND listing_id < 15"
    # cursor.execute(sql)
    # results = cursor.fetchall()
    #  msg3 = len(results)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 20
    startpage = page * per_page



    if (startpage == per_page):
        startpage = 0
        cursor = db.cursor()
        cursor.execute("SELECT * FROM listings WHERE uid = %s LIMIT %s, %s", (uid, startpage, per_page))
        results = cursor.fetchall()
        nuitems = len(results)
        nupages = round((nuitems/per_page))
        pagination = Pagination(page=page, per_page=10, total=nuitems, search=False, alignment='right',
                                record_name='results', css_framework='bootstrap4')
    # cursor.execute("SELECT * FROM listings")

    else:
        startpage = (page * per_page) - (per_page)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM listings WHERE uid = %s LIMIT %s, %s", (uid, startpage, per_page))
        results = cursor.fetchall()
        nuitems = len(results)
        nupages = round((nuitems/per_page))
        pagination = Pagination(page=page, per_page=10, total=nuitems, search=False, alignment='right',
                                record_name='results', css_framework='bootstrap4')

    if results == '':
        nupages = page-1
     #pagination = Pagination(page=page, per_page=10, total=nuitems, search=False, alignment='right', record_name='results', css_framework='bootstrap4')
    return results, pagination, page, nupages




# VIEW of the Items on STARTPAGE
@app.route('/start/',methods=['GET'])
def start(uid):

    # #return redirect(url_for('login'))
    # cursor = db.cursor()
    # sql = "SELECT * FROM listings WHERE listing_id > 10 AND listing_id < 15"
    # cursor.execute(sql)
    # results = cursor.fetchall()
    #  msg3 = len(results)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 20
    startpage = page * per_page

    if (startpage == per_page):
        startpage = 0
        cursor = db.cursor()
        cursor.execute("SELECT * FROM listings WHERE uid >= %s LIMIT %s, %s", (uid, startpage, per_page))
        results = cursor.fetchall()
        nuitems = len(results)
        nupages = round((nuitems / per_page))
        pagination = Pagination(page=page, per_page=10, total=nuitems, search=False, alignment='right',
                                record_name='results', css_framework='bootstrap4')
    
    else:
        startpage = (page * per_page) - (per_page)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM listings WHERE uid >= %s LIMIT %s, %s", (uid, startpage, per_page))
        results = cursor.fetchall()
        nuitems = len(results)
        nupages = round((nuitems / per_page))
        pagination = Pagination(page=page, per_page=10, total=nuitems, search=False, alignment='right',
                                record_name='results', css_framework='bootstrap4')


    #pagination = Pagination(page=page, per_page=10, total=nuitems, search=False, alignment='right', record_name='results', css_framework='bootstrap4')
    return results, pagination, page, nupages



## Login Procedure
@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor = db.cursor()
    msg2 = 'Please enter your credentials'
    msg = 'Please enter your credentials'

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password1 = request.form['password']
        sessiondb = Session()

        result = sessiondb.query(User).filter_by(username=username, userstatus='Active').first()

        if result:
            passwr = result.password
            print(passwr)
            msg2 = passwr

            
            hashed = sha256_crypt.verify(password1, passwr)
            print(hashed)
            account = result
        else:
            return render_template('index.html', msg=msg, msg2=msg2)

        ## MYSQL CLASSIC
        # passwordrew = check_encrypted_password(password1, hashed)
        # passwordrew = compare
        # Check if account exists using MySQL
        # cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, passwordrew,))
        # Fetch one record and return result

        # If account exists in accounts table in out database
        if account and hashed == True:
        # #     # Create session data, we can access this data in other routes
          session['loggedin'] = True
          user = request.form['username']
          session['uid'] = result.uid
          print(result.uid)
          session['username'] = user
          login_msg = 'Loggedin as ' + user
          eingeloggt = True
          results = test()
          print(session['username'])
        # session = scoped_session(Session())
        #   sessiondb = Session()

          return redirect(url_for('home'))
          ## return render_template('test.html',user=user,results=results,eingeloggt=eingeloggt)
        else:
        #     # Account doesnt exist or username/password incorrect
         msg = 'Incorrect username/password!'
         #msg2 = 'mehrere Variablen¨zum übergeben möglich'
    return render_template('index.html', msg=msg, msg2=msg2)
       # gehoert zu else


## Logout procedure
@app.route('/logout')
@login_required
@active_user
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('uid', None)
   session.pop('username', None)
   session.clear()
   # Redirect to login page
   return redirect(url_for('home'))


## Sign-up form Logic
@app.route('/signup', methods=["GET", "POST"])
@admin_required
@active_user
def signup_form():
    form = SignupForm()
    msg2 = 'test'
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.hash(form.password.data)

        fullname = form.fullname.data
        roleid = 1
        start_date2 = form.start_date.data
        newformat = start_date2.strftime("%d-%m-%Y")
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        userstatus = 'inactive'
        next = request.args.get('next', None)
        sessiondb = Session()
        create_user = User(username=username, password=password, email=email, fullname=fullname, roleid=roleid,
                           userstatus=userstatus)
        request1 = sessiondb.query(User).filter_by(username=username).first()

        if request1:
            msg2= 'It seems that account already exit'
            return render_template("signup_form.html", form=form, msg=msg2)

        elif sessiondb.query(User).filter_by(email=email).first():
            msg2= 'email already exit'
            return render_template("signup_form.html", form=form, msg=msg2)

        else:
          sessiondb.add(create_user)
          sessiondb.commit()
          ##Confirmation mail
          link = '127.0.0.1:5000/responsemail?username=' + username
          ### Replace Email and replace smtp information in config.py
          send_email('User reviewed neu', 'confirmation@futurework.cl', email, '', 'mail/confirmation.html', link)


          return redirect(url_for('home'))

#### CHECK EMAIL

    return render_template("signup_form.html", form=form, msg=msg2)


## Creation of new listing items
@app.route('/listing_form', methods=["GET", "POST"])
# @active_user
# @admin_required
def listing_form():
    form = ListingForm()
    msg2 = 'test'
    uid = session['uid']
    print(uid)
    if form.validate_on_submit():
        listing_title = form.listing_title.data
        listing_domain = form.listing_domain.data
        listing_description = form.listing_description.data
        listing_price = form.listing_price.data
        listing_type = form.listing_type.data
        listing_special = form.listing_special.data
        listing_status = 'inactive'
        uid = uid
        listing_expiration = date.today()
        listing_start = date.today()

        sessiondb = Session()
        create_listing = Listing(listing_title=listing_title, listing_domain=listing_domain,
                                 listing_description=listing_description,
                                 listing_price=listing_price, listing_type=listing_type, listing_special=listing_special, listing_status=listing_status, uid=uid, listing_start=listing_start, listing_expiration=listing_expiration)
        sessiondb.add(create_listing)
        sessiondb.commit()

        return redirect(url_for('home'))
    else:
         msg2='NO EXITO'


    return render_template("listing_form.html", form=form, msg=msg2)


## Response from pages, generate information about clicks on pages
@app.route('/response', methods=['GET', 'POST'])
def response():
   selected_element = request.args.get('element')
   ##results, pagination, page, nupages = items(session['uid'])
   print (selected_element)
   return redirect(url_for('home'))
   ##return render_template('home.html', username=session['username'], results=results, pagination=pagination, msg3=page,
                 ##         page=page, nupages=nupages, selected_element=selected_element)















## Listings of items or content
def auflistung():
    cursor = db.cursor()
    sql = "SELECT * FROM listings WHERE uid=%s" % (session['uid'])
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        listing_id = row[0]
        listing_uid = row[1]
        listing_domain= row[2]
        listing_title = row[3]
        listing_description = row[4]
        listing_price = row[5]
        listing_expiration = row[6]
        listing_start = row[7]
        listing_creation = row[8]

    return results


## Erstellung von Auflistungen
def test():
     cursor = db.cursor()
     sql = "SELECT * FROM users WHERE uid=%s"%(session['uid'])
     cursor.execute(sql)
     results = cursor.fetchall()
     for row in results:
         uid = row[0]
         name = row[1]
         password = row[2]
         email = row[3]

     return results



## Profile Datas listing
@app.route('/profile')
@active_user
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        iduser = session['uid']
        #cursor = db.cursor()
        #cursor.execute('SELECT * FROM accounts WHERE uid = %s', (1,))
        #account = cursor.fetchone()
        # Show the profile page with account info

        cursor = db.cursor()
        #sql = "SELECT * FROM accounts WHERE uid=s%"%(iduser)
        cursor.execute('SELECT * FROM users WHERE uid= %s ', (iduser,))
        #cursor.execute(sql)
        account = cursor.fetchall()
        for row in account:
            uid = row[0]
            name = row[1]
            email = row[2]
            password= row[3]

        # link = '127.0.0.1:5000/responsemail?id=' + name
        # send_email('User reviewed neu', 'confirmation@futurework.cl', email, '', 'mail/confirmation.html', link)
        return render_template('profile.html', username=name, password=password, email=email)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




##APIS
##Reads user confirmation link from Email
@app.route('/responsemail', methods=['GET', 'POST'])
def responsemail():

   if 'username' in request.args:
       requser = request.args['username']
       print(requser)
       sessiondb = Session()
       q_user = sessiondb.query(User).filter(User.username == requser).first()
       q_user.userstatus = "active"
       sessiondb.commit()


       return render_template('testus.html', msg4=requser)
   else:
       return render_template('testus.html', msg4='error')


##API JSON
## Creates listings
@app.route('/json-listing', methods=['POST']) #GET requests will be blocked
def json_listing():
    req_data = request.get_json()

    listing_title = req_data['listing_title']
    listing_domain = req_data['listing_domain']
    listing_description = req_data['listing_description']
    listing_price = req_data['listing_price']
    listing_type = req_data['listing_type']
    listing_special = req_data['listing_special']
    listing_status = req_data['listing_status']
    uid = req_data['uid']
    listing_expiration = req_data['listing_expiration']
    listing_start = req_data['listing_start']
    sessiondb = Session()
    create_listing = Listing(listing_title=listing_title, listing_domain=listing_domain,
                             listing_description=listing_description, listing_price=listing_price,
                             listing_type=listing_type, listing_special=listing_special, listing_status=listing_status,
                             uid=uid, listing_start=listing_start, listing_expiration=listing_expiration)
    sessiondb.add(create_listing)
    sessiondb.commit()

    return '''
           Creation sucessful
           The listing title is: {}
           The listing domain is: {}
           The listing description is: {}
           The listing price is: {}
           The listing type is: {}
           The listing special is: {}
           The listing status is: {}
           The listing uid is: {}
           The listing start is: {}
           The listing expiration is: {}
           '''.format(listing_title, listing_domain, listing_description,listing_price, listing_type, listing_special, listing_status, uid, listing_start,listing_expiration)














