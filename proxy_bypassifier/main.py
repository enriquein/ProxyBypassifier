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
    is_google_result = 'false'

    try:
        is_google_result = request.form['googleresult']
    except KeyError:
        pass

    return fetcher.get_url_contents(request.form['url'], is_google_result)

@app.route('/file', methods=['POST'])
def get_remote_file():
    contents = None
    filename = None

    try:
        contents = fetcher.get_file(request.form['file'])
        filename = fetcher.get_filename_from_url(request.form['file'])
    except KeyError
        return 'Error: Url for file is required. Go back and fix that. Also, stop bypassing my javascript validations.'

    resp = make_response(contents)
    resp.headers['Content-Type'] = 'application/force-download'
    resp.headers['Content-Length'] = len(resp)
    resp.headers['Content-Disposition'] = 'attachment; filename=' + filename + '_'
    return resp

if __name__ == '__main__':
    app.run()