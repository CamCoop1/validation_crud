
import os
from dotenv import load_dotenv
from tools.dirs import find_file

load_dotenv(dotenv_path=find_file('.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = ( 
        os.getenv("DATABASE_URL") or
        f'sqlite:///{find_file()}/db.sqlite'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")