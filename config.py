"""Config Class"""

from os import environ, path
from dotenv import load_dotenv
import redis

from app.constants import BASE_DIR

# load_dotenv()

load_dotenv(path.join(BASE_DIR, ".env"))  # Load environment variables from .env file


class Config:
    """Class that defines Environmental Variables for the App"""

    # Flask-SQLAlchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")

    # Flask-Session
    REDIS_URI = environ.get("REDIS_URI")
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(environ.get("REDIS_URI"))
    
    # OAuth2 Providers
    OAUTH2_PROVIDERS = {
        'google': {
            'client_id': environ.get('GOOGLE_CLIENT_ID'),
            'client_secret': environ.get('GOOGLE_CLIENT_SECRET'),
            'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
            'token_url': 'https://accounts.google.com/o/oauth2/token',
            'userinfo': {
                'url': 'https://www.googleapis.com/oauth2/v3/userinfo',
                'email': lambda json: json['email'],
            },
            'scopes': ['https://www.googleapis.com/auth/userinfo.email'],
        },
        # 'github': {
        #     'client_id': environ.get('GITHUB_CLIENT_ID'),
        #     'client_secret': environ.get('GITHUB_CLIENT_SECRET'),
        #     'authorize_url': 'https://github.com/login/oauth/authorize',
        #     'token_url': 'https://github.com/login/oauth/access_token',
        #     'userinfo': {
        #         'url': 'https://api.github.com/user/emails',
        #         'email': lambda json: json[0]['email'],
        #     },
        #     'scopes': ['user:email'],
        # },
    }
