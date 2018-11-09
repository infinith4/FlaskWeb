"""
Routes and views for the flask application.
"""

# https://backlog.com/developer/applications/

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
import requests
import json

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

    params = {'projectKey': 'TYS_SRE', 'apiKey': BACKLOG_API_KEY_GLOBAL}
    r = requests.get(BACKLOG_HOST_GLOBAL + '/api/v2/issues', params=params)
    print(r.json())

    params = {'apiKey': BACKLOG_API_KEY_GLOBAL}
    r = requests.get(BACKLOG_HOST_GLOBAL + '/api/v2/projects/TYS_SRE', params=params)
    print(r.json())

    params = {'apiKey': BACKLOG_API_KEY_GLOBAL}
    r = requests.get(BACKLOG_HOST_GLOBAL + '/api/v2/space')
    print(r.json())

    issueIdOrKey = 'FFIS_SMAPHOSYS-489'
    url = BACKLOG_HOST_GLOBAL + '/api/v2/issues/' + issueIdOrKey
    print(url)
    params = {'apiKey': BACKLOG_API_KEY_GLOBAL}
    r = requests.get(url, params=params)
    print(r.json())

    params = {'apiKey': BACKLOG_API_KEY_GLOBAL}
    issueIdOrKey = 'FFIS_SMAPHOSYS-489'
    commentId = '39332511'
    url = BACKLOG_HOST_GLOBAL + '/api/v2/issues/' + issueIdOrKey + "/comments/" + commentId
    print(url)
    r = requests.get(url, params=params)
    print(r.json())
    print(json.dumps(r.json(), indent=2))
    #data = json.loads(r.json())
    #print(json.dumps(data, indent=2))

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
