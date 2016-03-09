"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from app import app
from app import db
from datetime import *
from app.models import User
from flask import render_template, request, redirect, url_for, jsonify
from app.forms import UserForm
import json
import time
from werkzeug import secure_filename



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods=['POST','GET'])
def profile():
    form = UserForm(request.form)
    if request.method=="POST":
        file = request.files['file']
        savefile = form.username.data + "_" + secure_filename(file.filename)
        savefilepath = os.path.join(os.getcwd() + '/app/static/img/',savefile)
        file.save(savefilepath)
        user = User(savefile, form.username.data, form.fname.data, form.lname.data, form.age.data, form.sex.data, datetime.now())
        db.session.add(user)
        db.session.commit()
        return redirect('/profile/'+str(User.query.filter_by(username=user.username).first().id))
    else:
        return render_template('profileadd.html',form=form)

@app.route('/profiles',methods=['POST','GET'])
def profiles():
    
    return render_template('profiles.html')

@app.route('/profile/<userid>',methods=['POST','GET'])
def profileselect(userid):
    user = User.query.filter_by(id=userid).first()
    return render_template('profile.html')
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
