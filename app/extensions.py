"""List of extensions required for the App"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_cors import CORS


migrate = Migrate()
db = SQLAlchemy()
server_session = Session()
cors = CORS()
