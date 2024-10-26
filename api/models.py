from datetime import datetime
from api import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,   
    ForeignKey     
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
    datasets = relationship("Dataset", back_populates="campaign")
    
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
