"""Balances API routes"""

import os
import json
from flask import jsonify, request as req
from . import balance
from .controller import createBalance, getAllBalances



@balance.route("/", methods=['GET','POST'])
def index():
    if req.method == 'GET': return getAllBalances()
    if req.method == 'POST': return createBalance()

