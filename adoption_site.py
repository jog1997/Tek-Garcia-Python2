#adoption_site.py
##Here are the app routes for the website

import os
from Forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, app, Puppy, Toy, Owner





##### MODELS on models.py file


#######View Functions

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_Owner',methods = ['GET','POST'])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data

        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit

        return redirect(url_for('list_pup'))
    return render_template('add_owner.html', form = form)

@app.route('/add',methods = ['GET','POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        color = form.color.data
        age = form.age.data


        new_puppy = Puppy(name)
        new_puppy.color = color
        new_puppy.age = age
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form = form)


@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET','POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)

