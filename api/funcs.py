import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tools.dirs import find_file

load_dotenv()

def get_engine():
    db_url = ( 
        os.getenv("DATABASE_URL") or
        f'sqlite:///{find_file()}/db.sqlite'
)
    return create_engine(db_url)

def get_session():
    return sessionmaker(bind=get_engine())()