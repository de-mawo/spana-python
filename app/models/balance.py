"""Balance Model"""

from sqlalchemy import inspect
from app.extensions import db
from app.constants import STRING_YEAR
from app.models import TimeStampIDMixin
from app.models import (
    user,
)  # to solve NoReferencedTableError: Foreign key associated with column … could not find table


class Balance(TimeStampIDMixin, db.Model):
    """Class for defining Balance Table columns"""

    __tablename__ = "balance"

    year = db.Column(db.String(), default=STRING_YEAR)
    name = db.Column(db.String())
    email = db.Column(db.String())
    annualCredit = db.Column(db.Integer(), default=0)
    annualUsed = db.Column(db.Integer(), default=0)
    annualAvailable = db.Column(db.Integer(), default=0)
    healthCredit = db.Column(db.Integer(), default=0)
    healthUsed = db.Column(db.Integer(), default=0)
    healthAvailable = db.Column(db.Integer(), default=0)
    studyCredit = db.Column(db.Integer(), default=0)
    studyUsed = db.Column(db.Integer(), default=0)
    studyAvailable = db.Column(db.Integer(), default=0)
    maternityCredit = db.Column(db.Integer(), default=0)
    maternityUsed = db.Column(db.Integer(), default=0)
    maternityAvailable = db.Column(db.Integer(), default=0)
    familyCredit = db.Column(db.Integer(), default=0)
    familyUsed = db.Column(db.Integer(), default=0)
    familyAvailable = db.Column(db.Integer(), default=0)
    paternityCredit = db.Column(db.Integer(), default=0)
    paternityUsed = db.Column(db.Integer(), default=0)
    paternityAvailable = db.Column(db.Integer(), default=0)
    unpaidAvailable = db.Column(db.Integer(), default=0)
    userId = db.Column(db.Uuid(), db.ForeignKey("user.id"))

    # serialize SqlAlchemy PostgreSQL Query to JSON
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


    def __repr__(self):
        return f'<Balance "{self.email}">'
