"""List of extensions required for the App"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session


migrate = Migrate()
db = SQLAlchemy()
sess = Session()
