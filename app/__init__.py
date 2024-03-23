"""Application Factory"""

from flask import Flask
from config import Config
from app.extensions import db
from app.extensions import migrate
from app.extensions import server_session
from app.extensions import cors


def create_app(config_class=Config):
    """Factory function
    @Return: application instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    server_session.init_app(app)

    cors.init_app(
        app,
        resources={r"/api/*": {"origins": [app.config["CLIENT_URL"]]}},
        supports_credentials=True,
    )

    # Register blueprints
    from app.user import user as user_bp
    from app.auth import auth as auth_bp
    from app.leave import leave as leave_bp
    from app.balance import balance as balance_bp
    from app.events import events as events_bp

    app.register_blueprint(user_bp, url_prefix="/api/v1/user")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(leave_bp, url_prefix="/api/v1/leave")
    app.register_blueprint(balance_bp, url_prefix="/api/v1/balance")
    app.register_blueprint(events_bp, url_prefix="/api/v1/events")

    @app.route("/")
    def test_page():
        return "<h1> HI I am Home </h1>"

    return app
