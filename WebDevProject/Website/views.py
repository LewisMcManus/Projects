from flask import Blueprint, render_template, Flask, session, request, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector, gc

conn = mysql.connector.connect(host='127.0.0.1',
                               user='root',
                               password = 'Lewis180805!')



views = Blueprint('views', __name__)

@views.route('/')
def home():
    if 'email' in session:
        return render_template('HomePageV2.html', email=session['email'])
    else:
        return render_template('HomePageV2.html')
    
@views.route('/Aberdeen')
def Aberdeen():
    if 'email' in session:
        return render_template('Aberdeen.html', email=session['email'] )
    else:
        return render_template('Aberdeen.html')
    
@views.route('/Belfast')
def Belfast():
    if 'email' in session:
        return render_template('Belfast.html', email=session['email'] )
    else:
        return render_template('Belfast.html')
    
@views.route('/Birmingham')
def Birmingham():
    if 'email' in session:
        return render_template('Birmingham.html', email=session['email'] )
    else:
        return render_template('Birmingham.html')
    
@views.route('/Bristol')
def Bristol():
    if 'email' in session:
        return render_template('Bristol.html', email=session['email'] )
    else:
        return render_template('Bristol.html')



@views.route('/booking')
def booking():
    if 'email' in session:
        return render_template('booking.html',email=session['email'] )
    else:
        return render_template('booking.html')
    
@views.route('/BookingSuccess')
def BookingSuccess():
    if 'email' in session:
        return render_template('BookingSuccess.html', email=session['email'])
    else:
        return render_template('Login.html')
    
@views.route('/admin')
def admin():
    return render_template('admin.html', email=session['email'])



@views.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        dbcursor = conn.cursor()
        dbcursor.execute('USE {};'.format('worldhotels'))
        dbcursor.execute("SELECT Password, AccountType \
                         FROM userdata WHERE Email = %s;", (email,))
        data = dbcursor.fetchone()
        if pwd == str(data[0]):
            session['email'] = email
            session['AccountType'] = str(data[1])
            return redirect('/')
        else:
            return render_template('Login.html')
    return render_template('Login.html')

@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        dbcursor = conn.cursor()
        dbcursor.execute('USE {};'.format('worldhotels'))
        dataset = (email, pwd)
        TABLE_NAME = 'userdata'
        INSERT_statement = 'INSERT INTO ' + TABLE_NAME + ' (\
            Email, Password) VALUES (%s, %s);'
        dbcursor.execute(INSERT_statement, dataset)
        conn.commit()
        dbcursor.close()
        return redirect(url_for('views.Login'))
    return render_template('register.html')

@views.route('/logout')
def logout():
    session.clear()
    gc.collect()
    return render_template('HomePageV2.html')

        