"""Leave Model"""

import datetime
import enum
from app.extensions import db

YEAR = (datetime.date.today()).year
STRING_YEAR = str(YEAR)


class LeaveType(enum.Enum):
    """Leave Enum type definition"""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    INMODERATION = "INMODERATION"
    REJECTED = "REJECTED"


class Leave(db.Model):
    """Class for defining Leave Table columns"""

    __tablename__ = "leave"
    id = db.Column(db.Uuid(), primary_key=True, unique=True, nullable=False)
    leave_type = db.Column(db.String())
    year = db.Column(db.String(), default=STRING_YEAR)
    start_date = db.Column(db.DateTime(timezone=True), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    days = db.Column(db.Integer(2), nullable=False)
    name = db.Column(db.String(), nullable=False)
    note = db.Column(db.String())
    link = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    moderator = db.Column(db.String())
    moderatorNote = db.Column(db.String())
    status = db.Column(db.String(), default=LeaveType.PENDING)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime(timezone=True), default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
    
    def __rep__(self):
        return f'<Leave "{self.name}"'
