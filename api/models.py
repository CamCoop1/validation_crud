from datetime import datetime
from api import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,   
    ForeignKey,
    Boolean
        
)

class Campaign(Base):
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
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique = True)
    exp_range = Column(String(20))
    start_date = Column(Date, default=datetime.utcnow)
    active_campaign = Column(Boolean, default=True)
    datasets = relationship("Dataset", back_populates="campaign")
    
    @property
    def start(self):
        return int(self.experiment_range.split('-')[0])

    @property
    def end(self):
        parts = self.experiment_range.split('-')
        return int(parts[1]) if len(parts) > 1 else self.start

    @property
    def is_range(self):
        return '-' in self.experiment_range
    def __repr__(self):
        return f"<Campaign Name: {self.name}, exp_range: {self.exp_range}>"
    

class Dataset(Base):
    __tablename__ = "Dataset"
    
    id = Column(Integer, primary_key = True)
    collection_lpn = Column(String(50), unique=True)
    date_added = Column(Date, default=datetime.utcnow)
    
    campaign_id = Column(Integer, ForeignKey("Campaign.id"))
    campaign = relationship("Campaign", back_populates='datasets')
    
    def __repr__(self):
        return f'<Campaign: {self.campaign}, collection LPN: {self.collection_lpn}>'
