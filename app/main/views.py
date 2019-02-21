from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from flask_login import login_required
from ..models import User
from .. import db, photos
import urllib.request, json
from pprint import pprint



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add()
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/livescore')
def live():
    response = urllib.request.urlopen
    response = urllib.request.urlopen('http://livescore-api.com/api-client/scores/live.json?key=BqTIFtifL0AOicqs&secret=T6xotmiNFNW8qgk2HdLnH3Ct4dimpIPj')
    data = response.read()
    JSON_object = json.loads(data.decode('UTF-8'))
    data = JSON_object
    data1=data["data"]
    
    print(data1["match"])
    return render_template('livescore.html', data =data1) 

@main.route('/fixtures')
def fixtures():
    response = urllib.request.urlopen
    response = urllib.request.urlopen('http://livescore-api.com/api-client/fixtures/matches.json?key=BqTIFtifL0AOicqs&secret=T6xotmiNFNW8qgk2HdLnH3Ct4dimpIPj')
    data = response.read()
    JSON_object = json.loads(data.decode('UTF-8'))
    data = JSON_object
    data1=data["data"]
    print(data1["fixtures"])
    return render_template('fixtures.html', data = data1)




