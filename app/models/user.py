"""User Model"""

import enum
from app.extensions import db
from app.models import TimeStampIDMixin
from app.models import leave 


class UserType(enum.Enum):
    """User Enum type definition"""

    USER = "USER"
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"


class User(TimeStampIDMixin, db.Model):
    """Class for defining User Table columns"""

    __tablename__ = "user"

    name = db.Column(db.String())
    email = db.Column(db.String(100), unique=True)
    image = db.Column(db.String())
    phone = db.Column(db.String(100))
    title = db.Column(db.String())
    manager = db.Column(db.String())
    department = db.Column(db.String())
    role = db.Column(db.String(100), default=UserType.USER)
    balances = db.relationship('Balance', backref='balance', lazy=True)  
    leaves = db.relationship('Leave', backref='leave', lazy=True)

    def __rep__(self):
        return f'<User "{self.name}"'
