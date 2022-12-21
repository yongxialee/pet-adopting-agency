from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,BooleanField,IntegerField,RadioField,SelectField
from wtforms.validators import InputRequired, Optional,NumberRange,Length,URL
class AddPetForm(FlaskForm):
    name= StringField("Pet name",
                        validators=[InputRequired(message="please enter pet name")])
    
    species = StringField("Species")
    photo_url=StringField("Photo URL")
    age = IntegerField("Age",validators=[Optional(), NumberRange(min=0, max=30)])
    notes=TextAreaField("Comments",validators=[Optional(), Length(min=5)])
    
class EditPetForm(FlaskForm):
    """form for editing an existing pet"""
    photo_url=StringField("Photo URL", validators=[Optional(),URL()])
    notes = TextAreaField("Comments",validators=[Optional(),Length(10)])
    # available = BooleanField("Available")
    available = BooleanField("Available?")