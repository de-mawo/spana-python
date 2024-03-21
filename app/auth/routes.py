"""Auth API routes"""

import uuid
import requests
from flask import (
    redirect,
    current_app,
    session,
    abort,
    url_for,
    request as req,
    jsonify,
)
from . import auth
import secrets
from urllib.parse import urlencode, parse_qs
from app.models.user import User
from app.extensions import db


@auth.route("/authorize/<provider>")
def oauth2Auth(provider):
    data = current_app.config["OAUTH2_PROVIDERS"].get(provider)
    if data is None:
        abort(404)
    # generate a random string for the state parameter
    session["oauth2_state"] = secrets.token_urlsafe(16)

    # create a query string with all the OAuth2 parameters
    queryString = urlencode(
        {
            "client_id": data["client_id"],
            "redirect_uri": url_for(
                "auth.oauth2Callback", provider=provider, _external=True
            ),
            "response_type": "code",
            "scope": " ".join(data["scopes"]),
            "state": session["oauth2_state"],
        }
    )
    print(queryString)
    # redirect the user to the OAuth2 provider authorization URL
    return redirect(data["authorize_url"] + "?" + queryString)


@auth.route("/callback/<provider>")
def oauth2Callback(provider):
    data = current_app.config["OAUTH2_PROVIDERS"].get(provider)

    if data is None:
        abort(404)

    # if there was an authentication error, return the error messages and exit
    if "error" in req.args:
        for k, v in req.args.items():
            if k.startswith("error"):
                error = f"{k}: {v}"

        return error

    # make sure that the state parameter matches the one we created in the
    # authorization request // often used to prevent CSRF attacks
    # if req.args['state'] != session.get('oauth2_state'):
    #     abort(401)

    # make sure that the authorization code is present
    if "code" not in req.args:
        abort(401)

    # exchange the authorization code for an access token
    response = requests.post(
        data["token_url"],
        data={
            "client_id": data["client_id"],
            "client_secret": data["client_secret"],
            "code": req.args["code"],
            "grant_type": "authorization_code",
            "redirect_uri": url_for(
                "auth.oauth2Callback", provider=provider, _external=True
            ),
        },
        headers={"Accept": "application/json"},
    )
    if response.status_code != 200:
        abort(401)
    oauth2_token = response.json().get("access_token")
    if not oauth2_token:
        abort(401)

    # use the access token to get the user's email address
    response = requests.get(
        data["userinfo"]["url"],
        headers={
            "Authorization": "Bearer " + oauth2_token,
            "Accept": "application/json",
        },
    )
    if response.status_code != 200:
        abort(401)
    # This is the values from Google , check the documentation from other providers
    name, picture, email = (
        response.json().get("name"),
        response.json().get("picture"),
        response.json().get("email"),
    )

    # find or create the user in the database
    user = User.query.filter_by(email=email).first()

    if user is None:
        # Create a new user if not exists
        id = str(uuid.uuid4())
        new_user = User(id=id, name=name, email=email, image=picture)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
    else:
        # Use the existing user's id
        session["user_id"] = user.id
    # log the user in

    clientUrl = current_app.config["CLIENT_URL"]

    return redirect(clientUrl)


@auth.route("/getMe")
def getCurrentUser():
    if "user_id" in session:
        user_id = session["user_id"]

        # Fetch user details from database using user_id
        user = User.query.get(user_id)
        # Only send minimal fields for a logged in user
        if user:
            return {
                # "id": user.id,
                "name": user.name,
                "email": user.email,
                "image": user.image,
                "role": user.role.value,
                # "phone": user.phone,
                # "title": user.title,
                # "manager": user.manager,
                # "department": user.department,
            }
        else:
            return jsonify({"error": "User not found"}), 404  # Not Found
    else:
        return jsonify({"error": "User not logged in"}), 401  # Unauthorized


@auth.route("/logout", methods=["POST"])
def logout_user():
    session.pop("user_id")
    return jsonify({"success": "Logged Out"}), 201
