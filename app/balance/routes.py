"""Balances API routes"""

import os
import json
from flask import jsonify
from app.balance import balance


@balance.route("/")
def index():
    json_path = os.path.join(os.path.dirname(__file__), "balances.json")
    with open(json_path) as file:
        data = json.load(file)
    return jsonify(data)
