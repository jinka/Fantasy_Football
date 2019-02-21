from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
import http.client
import json

@main.route('/')
def index():
    
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'bb52f0e668d34b85eacfd16806964fa745d1c914db184ebc8f028ad3099cff5c' }
    connection.request('GET', '/v2/competitions/DED', None, headers )
    response = json.loads(connection.getresponse().read().decode())


    return response

    # title = 'Football Fantasy'

    # return render_template("index.html", response = response, title = title)
    
    
