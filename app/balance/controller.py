"""Balances Controllers """

import uuid
from flask import request as req, jsonify
from app.models.balance import Balance
from app.extensions import db
from app.auth.util import isAdmin

@isAdmin
def getAllBalances():
    """Func to get all Admin Balances"""
    balances = Balance.query.all()
    res = []
    for balance in balances:
        res.append(balance.toDict())
    return jsonify(res)


def createBalance():
    """Create Function for the Admin to create a Balance"""
    if not req.json:
        return "Content Type not accepted"

    else:
        body = req.json
        id = str(uuid.uuid4())
         # Access values directly from the dictionary using their keys
        annualCredit = body.get('annual')
        familyCredit = body.get('family')
        healthCredit = body.get('health')
        studyCredit = body.get('study')
        maternityCredit = body.get('maternity')
        paternityCredit = body.get('paternity')
        year = body.get('year')
        email = body.get('email')
        name = body.get('name')
        new_balance = Balance(
           id=id, annualCredit=annualCredit, familyCredit=familyCredit, healthCredit=healthCredit,
           studyCredit=studyCredit, maternityCredit=maternityCredit, paternityCredit=paternityCredit,
           year=year, email=email, name=name
        )
        db.session.add(new_balance)
        db.session.commit()

        res = Balance.query.get(id).toDict()
        return jsonify(res)
