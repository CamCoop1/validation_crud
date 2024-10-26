from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, DateField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
import sqlalchemy as sa
from app import db, models
from datetime import datetime


class AddCampaign(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    exp_range = StringField('Experiment Range', validators=[DataRequired()])
    start_date = DateField('Start Date', default=datetime.utcnow )
    submit = SubmitField('Add')

class AddDataset(FlaskForm):
    
    collection_lpn = StringField('Collection LPN', validators=[DataRequired()])
    campaign = SelectField(
        'Campaign', 
        validators=[DataRequired()],
        choices=[(camp.name, camp.name) for camp in db.session.query(models.Campaign).all() ]                
    )
    submit = SubmitField('Add')
    
 