"""List of extensions required for the App"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


migrate = Migrate()
db = SQLAlchemy()
