import os

from tools.dirs import find_file
from tools.database_meta import metadata

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv(dotenv_path=find_file('.env'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ( 
        os.getenv("DATABASE_URL") or
        f'sqlite:///{find_file()}/db.sqlite'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from app import routes, models

app.app_context().push()