

from app.config import Config
from tools.dirs import find_file
from tools.database_meta import metadata

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from app import routes, models

app.app_context().push()