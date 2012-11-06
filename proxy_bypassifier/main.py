import sqlite3
import urllib
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

DATABASE = 'db/cache.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_website_form():
    return render_template('website_form.html')    

@app.route('/,', methods=['POST'])
def get_remote_site():
    f = urllib.urlopen(request.form['url'])
    s = f.read()
    f.close()
    return s

if __name__ == '__main__':
    app.run()