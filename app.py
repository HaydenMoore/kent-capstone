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

def del_and_update(c, conn):
    c.execute('SELECT password FROM users WHERE username = hayden')
    for row in c.fetchall():
        password = row[2]
        print(password)
    conn.commit
    conn.close()

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
    #del_and_update(c, conn)

    #Debugging
    print('RECIEVED DATA')
    print(username, password)

    return render_template('courses.html')

#run server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8003, passthrough_errors=True)