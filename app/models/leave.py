"""Leave Model"""

import enum
from app.extensions import db
from app.constants import STRING_YEAR
from app.models import TimeStampIDMixin


class LeaveType(enum.Enum):
    """Leave Enum type definition"""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    INMODERATION = "INMODERATION"
    REJECTED = "REJECTED"


class Leave(TimeStampIDMixin, db.Model):
    """Class for defining Leave Table columns"""

    __tablename__ = "leave"

    leave_type = db.Column(db.String())
    year = db.Column(db.String(), default=STRING_YEAR)
    start_date = db.Column(db.DateTime(timezone=True), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    days = db.Column(db.Integer(2), nullable=False)
    name = db.Column(db.String(), nullable=False)
    note = db.Column(db.Text())
    link = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    moderator = db.Column(db.String())
    moderatorNote = db.Column(db.String())
    status = db.Column(db.String(), default=LeaveType.PENDING)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f'<Leave "{self.name}"'
