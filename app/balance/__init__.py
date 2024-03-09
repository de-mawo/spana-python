"""Blueprint for the Balances route"""

from flask import Blueprint

balance = Blueprint('balance', __name__)

from app.balance import routes