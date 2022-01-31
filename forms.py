from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name", validators = [InputRequired()])

    species = SelectField("Species", choices=[('dog', 'dog'), ('cat', 'cat'), ('porcupine', 'porcupine')])

    photo_url = StringField("Photo URL")

    age = IntegerField("Age", validators = [NumberRange(0,30), InputRequired(message= "Enter Valid URL Please.")])

    notes = StringField("Notes")





