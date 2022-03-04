#forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    color = StringField('Color of Puppy:')
    age = IntegerField('Age of Puppy:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner:')
    puppy_id = IntegerField("ID of Puppy:")
    submit = SubmitField("Add Owner:")