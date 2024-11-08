from app import db
from datetime import datetime 
from enum import Enum, auto

class VIBEGroups(Enum):
    tracking = 'tracking'
    physics = 'physics'
    slme = 'slme'
    neutrals = 'neutrals'

class Campaign(db.Model):
    """
    Parameters
    ------------
    id: int
        primary key
    name: str
        name of campaign
    exp_range: str
        range of experiments
    datasets: relationship 
        one to many with Dataset
    """
    __tablename__ = "Campaign"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique = True)
    exp_range = db.Column(db.String(20))
    start_date = db.Column(db.Date, default=datetime.utcnow)
    active_campaign = db.Column(db.Boolean, default = True)
    
    datasets = db.relationship("Dataset", back_populates="campaign")
    
    
    def __repr__(self):
        return f"<Campaign Name: {self.name}, exp_range: {self.exp_range}, active: {self.active_campaign}>"

class Dataset(db.Model):
    __tablename__ = "Dataset"
    
    id = db.Column(db.Integer, primary_key = True)
    collection_lpn = db.Column(db.String(50), unique=True)
    date_added = db.Column(db.Date, default=datetime.utcnow)
    
    campaign_id = db.Column(db.Integer, db.ForeignKey("Campaign.id"))
    campaign = db.relationship("Campaign", back_populates='datasets')
    
    def __repr__(self):
        return f'<Campaign: {self.campaign}, collection LPN: {self.collection_lpn}>'

class Mode(db.Model):
    __tablename__ = "Mode"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique=True)
    group = db.Column(db.Enum(VIBEGroups), nullable=False, default=VIBEGroups.physics)
    
    def __repr__(self):
        return f"<Name: {self.name}, Group: {self.group}>"