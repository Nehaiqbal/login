from flask import Flask, render_template, request, redirect, url_for, flash

import pyodbc 

import mysql.connector
from forms import LoginForm

from flask_mysqldb import MySQL
# app = Flask(__name__)

app = Flask(__name__,static_folder='static')



# settings
app.secret_key = 'mysecretkey'
#app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



