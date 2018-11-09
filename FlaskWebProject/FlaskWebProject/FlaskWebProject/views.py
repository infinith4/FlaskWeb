"""
Routes and views for the flask application.
"""

# https://backlog.com/developer/applications/

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
import requests

BACKLOG_HOST_GLOBAL = 'https://toyoko.backlog.jp'
BACKLOG_HOST_IP = 'https://toyoko-ip.backlog.com'
BACKLOG_API_KEY_GLOBAL = ''
BACKLOG_API_KEY_IP = ''

@app.route('/')
@app.route('/home')

def home():
    params = {'apiKey': BACKLOG_API_KEY_GLOBAL}
    r = requests.get(BACKLOG_HOST_GLOBAL + '/api/v2/users/myself', params=params)
    print(r.json())
    params = {'projectId': '39299'}
    r = requests.get(BACKLOG_HOST_GLOBAL + '/api/v2/issues', params=params)
    print(r.json())

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
