from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
import sqlalchemy as sa
from app import db
from datetime import datetime

class AddCampaign(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    exp_range = StringField('Experiment Range', validators=[DataRequired()])
    start_date = DateField('Start Date', default=datetime.utcnow )
    submit = SubmitField('Add')
