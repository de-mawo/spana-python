"""Auth API routes"""

from flask import redirect, current_app, session, abort, url_for, request as req
from flask_login import login_user
from . import auth
import secrets
from urllib.parse import urlencode, parse_qs
import requests


@auth.route("/authorize/<provider>")
def oauth2Auth(provider):
    data = current_app.config['OAUTH2_PROVIDERS'].get(provider)
    if data is None:
        abort(404)
    # generate a random string for the state parameter
    session['oauth2_state'] = secrets.token_urlsafe(16)

    # create a query string with all the OAuth2 parameters
    queryString = urlencode({
        'client_id': data['client_id'],
        'redirect_uri': "http://localhost:5000/auth/google/callback",
        'response_type': 'code',
        'scope': ' '.join(data['scopes']),
        'state': session['oauth2_state'],
    })

    # redirect the user to the OAuth2 provider authorization URL
    return redirect(data['authorize_url'] + '?' + queryString)  


@auth.route('/google/callback')
def oauth2Callback():
    data = current_app.config['OAUTH2_PROVIDERS'].get("google")
    print(data)
    if data is None:
        abort(404)  


    # if there was an authentication error, return the error messages and exit
    if 'error' in req.args:
        for k, v in req.args.items():
            if k.startswith('error'):
                error = (f'{k}: {v}')
        return error

    # make sure that the state parameter matches the one we created in the
    # authorization request
    if req.args['state'] != session.get('oauth2_state'):
        abort(401)

    # make sure that the authorization code is present
    if 'code' not in req.args:
        abort(401)

    # exchange the authorization code for an access token
    response = requests.post(data['token_url'], data={
        'client_id': data['client_id'],
        'client_secret': data['client_secret'],
        'code': req.args['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:5000/auth/google/callback',
    }, headers={'Accept': 'application/json'})
    if response.status_code != 200:
        abort(401)
    oauth2_token = response.json().get('access_token')
    if not oauth2_token:
        abort(401)

    # use the access token to get the user's email address
    response = requests.get(data['userinfo']['url'], headers={
        'Authorization': 'Bearer ' + oauth2_token,
        'Accept': 'application/json',
    })
    if response.status_code != 200:
        abort(401)
    email = data['userinfo']['email'](response.json())
    print(response)

    # find or create the user in the database
   

    # log the user in
    
    return redirect('http://localhost:3000/')
  