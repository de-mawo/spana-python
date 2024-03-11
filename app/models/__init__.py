"""Models Initializer file """

import datetime
from app.extensions import db


class TimeStampIDMixin:
    """Class for common attributes"""

    id = db.Column(db.Uuid(), primary_key=True, unique=True, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
