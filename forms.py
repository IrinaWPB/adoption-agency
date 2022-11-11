from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, URLField
from wtforms.validators import InputRequired, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('por', 'porcupine')], validators=[InputRequired()])
    photo = URLField("Add photo URL")
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Add notes")

class EditPetForm(FlaskForm):
    """Editing Form"""

    photo = URLField("Add a new photo")
    notes = StringField("Add notes")
    available = BooleanField("This pet is available for adoption")



