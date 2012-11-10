from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import fetcher
import db_layer

DATABASE = 'db/cache.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

#@app.before_request
#def before_request():
#    g.db = db_layer.connect_db(app.config['DATABASE'])

#@app.teardown_request
#def teardown_request(exception):
#    g.db.close()

@app.route('/')
def show_website_form():
    return render_template('website_form.html')    

@app.route('/,', methods=['POST'])
def get_remote_site():
    return fetcher.get_url_contents(request.form['url'])

if __name__ == '__main__':
    app.run()