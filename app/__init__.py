

from app.config import Config
from tools.database_meta import metadata


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
        
db = SQLAlchemy(app=app, metadata=metadata)

migrate = Migrate(app, db)

app.app_context().push()                

from app import routes, models

        