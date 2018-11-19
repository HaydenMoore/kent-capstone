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

def get_course_numbers(c, conn):
    c.execute('SELECT course_number FROM courses')
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    json_data = json.dumps(data)
    return json_data

def get_tutors(c,conn):
    c.execute('SELECT tutor_name FROM courses')
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

def get_times(c, conn):
    c.execute('SELECT time, end FROM courses')
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    json_data = json.dumps(data)
    return json_data

def get_notes(c, conn):
    c.execute('SELECT notes FROM courses')
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    json_data = json.dumps(data)
    return json_data

############ PROFILE PAGE ###############

def get_id(c, conn, username):
    c.execute('SELECT KSU_ID FROM users WHERE username=?', (username,))
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    return data

def get_email(c, conn, username):
    c.execute('SELECT email FROM users WHERE username=?', (username,))
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    return data

def get_phone(c, conn, username):
    c.execute('SELECT phone FROM users WHERE username=?', (username,))
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    return data

def get_scheduled(c, conn, username):
    c.execute('SELECT course_number FROM users WHERE username=?', (username,))
    data = {}
    i = 0
    for row in c.fetchall():
        data[i] = row
        i = i + 1
    return data

#create app object
app = Flask(__name__)
global_username = ""
#define routes
@app.route('/')
def run():
    return render_template('index.html')

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    # QUERY DATABASE HERE
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # #---------------------------------- DEBUGGING
    # print('RECIEVED DATA')
    # print(username, password)
    # This will create a new table
    # create_table(c)
    # data_entry_courses(c, conn)
    # data_entry(c, conn, username, password)
    courses = get_courses(c, conn)
    days = get_days(c, conn)
    times = get_times(c, conn)
    # #---------------------------------- END DEBUGGING

    authenticated = True
    if request.method == 'POST':
        # Captures user data
        username = request.form['username']
        password = request.form['password']


        authenticated = False
        authenticated = authorize_user(c, conn, username, password)

        if (authenticated):
            return render_template('courses.html', courses=courses, days=days, times=times, username=username)
        else:
            return render_template('index.html', auth=authenticated)
    conn.commit()
    c.close()
    conn.close()

    if request.method != 'POST':
        return render_template('courses.html', courses=courses, days=days, times=times)


@app.route('/comments', methods=['GET', 'POST'])
def comments():

    return render_template('comments.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    #Query database to set appointment for student
    if request.method == 'POST':
        appointment = request.form['checkbox']
        print(appointment)

    courses = get_courses(c,conn)
    tutors = get_tutors(c,conn)
    days = get_days(c, conn)
    times = get_times(c, conn)
    notes = get_notes(c, conn)
    course_numbers = get_course_numbers(c, conn)
    # close connection
    conn.commit
    conn.close()
    return render_template('schedule.html', courses = courses, tutors = tutors, days = days, times = times, notes = notes, course_numbers = course_numbers)

@app.route('/profile', methods=['GET', 'POST'])
def profile():

    if request.method == 'POST':
        username = request.form['javascript_data']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        id = get_id(c, conn, username)
        email = get_email(c, conn, username)
        phone = get_phone(c, conn, username)
        scheduled = get_scheduled(c, conn, username)

        # close connection
        conn.commit
        conn.close()
        return render_template('profile.html', id=id[0], email=email[0], phone=phone[0], scheduled=scheduled[0])




    return render_template('profile.html')








#run server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8003, passthrough_errors=True)