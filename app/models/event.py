"""Events Model"""


from app.extensions import db
from app.models import TimeStampIDMixin


class Event(TimeStampIDMixin, db.Model):
    """Class for defining Event Table columns"""

    __tablename__ = "event"

    title = db.Column(db.String())
    description = db.Column(db.Text())
    startDate = db.Column(db.DateTime(timezone=True))
    endDate = db.Column(db.DateTime(timezone=True))

    def __rep__(self):
        return f'<Event "{self.name}"'
