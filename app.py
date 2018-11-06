#!/usr/bin/python

#import flask library
from flask import Flask, render_template, url_for, request
import sqlite3
import time
import datetime
import json


def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS users(datestamp TEXT, username TEXT, password TEXT)')

def data_entry(c,conn, username, password):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO users (datestamp, username, password) VALUES (?, ?, ?)", (date, username, password))
    conn.commit()
    c.close()
    conn.close()

def data_entry_courses(c,conn):
    c.execute("INSERT INTO courses (course_title, course_number, tutor_name, day, time, end, notes) VALUES (?, ?, ?, ?, ?, ?, ?)", ("HUMAN-COMPUTER INTERACTION", 33310, "Drew Jackson, Foster Johnson", "Monday", 4, 10, "Tutoring to this course is offered every Monday"))
    conn.commit()
    c.close()
    conn.close()

def authorize_user(c, conn, username, password):
    c.execute('SELECT password FROM users WHERE username =?', (username,))
    authenticated = False
    for row in c.fetchall():
        db_password = row
        db_password = ''.join(db_password)

        if(password == db_password):
            authenticated = True
        else:
            authenticated = False
    conn.commit
    conn.close()
    return authenticated

def get_courses(c, conn):
    c.execute('SELECT course_title, course_number FROM courses')
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    json_data = json.dumps(data)
    return json_data

def get_days(c, conn):
    c.execute('SELECT day FROM courses')
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    json_data = json.dumps(data)
    return json_data




#create app object
app = Flask(__name__)

#define routes
@app.route('/')
def run():
    return render_template('index.html')

@app.route('/courses', methods=['POST'])
def courses():
    # Captures user data
    username = request.form['username']
    password = request.form['password']
    # QUERY DATABASE HERE
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # #---------------------------------- DEBUGGING
    # print('RECIEVED DATA')
    # print(username, password)
    #This will create a new table
    #create_table(c)
    # data_entry_courses(c, conn)
    #data_entry(c, conn, username, password)
    courses = get_courses(c, conn)
    days = get_days(c, conn)
    # #---------------------------------- END DEBUGGING

    authenticated = False
    authenticated = authorize_user(c, conn, username, password)

    if(authenticated):

        return render_template('courses.html', courses = courses, days=days)
    else:
        return render_template('index.html', auth = authenticated)


#run server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8003, passthrough_errors=True)