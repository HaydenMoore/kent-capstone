#!/usr/bin/python

#import flask library
from flask import Flask, render_template, url_for, request
import sqlite3
import time
import datetime


def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS users(datestamp TEXT, username TEXT, password TEXT)')

def data_entry(c,conn, username, password):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO users (datestamp, username, password) VALUES (?, ?, ?)", (date, username, password))
    conn.commit()
    c.close()
    conn.close()

def authorize_user(c, conn, password):
    c.execute('SELECT password FROM users WHERE username ="hayden"')
    authenticated = False
    for row in c.fetchall():
        db_password = row
        db_password = ''.join(db_password)

        print(db_password)

        if(password == db_password):
            authenticated = True
        else:
            authenticated = False
    conn.commit
    conn.close()
    return authenticated

#create app object
app = Flask(__name__)

#define routes
@app.route('/')
def run():
    return render_template('index.html')

@app.route('/courses', methods=['POST'])
def courses():
    username = request.form['username']
    password = request.form['password']
    # QUERY DATABASE HERE
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    #This will create a new table
    #create_table(c)
    # data_entry(c, conn, username, password)
    authenticated = authorize_user(c, conn, password)
    print(authenticated)
    # #Debugging
    # print('RECIEVED DATA')
    # print(username, password)
    if(authenticated):
        return render_template('courses.html')
    else:
        return render_template('index.html')


#run server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8003, passthrough_errors=True)