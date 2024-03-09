"""User Model"""

import enum
from app.extensions import db


class UserType(enum.Enum):
    """User Enum type definition"""

    USER = "USER"
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"


class User(db.Model):
    """Class for defining User Table columns"""

    __tablename__ = "user"
    id = db.Column(db.Uuid(), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String())
    email = db.Column(db.String(100), unique=True)
    image = db.Column(db.String())
    phone = db.Column(db.String(100))
    title = db.Column(db.String())
    manager = db.Column(db.String())
    department = db.Column(db.String())
    role = db.Column(db.String(100), default=UserType.USER)

    def __rep__(self):
        return f'<User "{self.name}"'
