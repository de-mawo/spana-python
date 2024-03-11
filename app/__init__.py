"""Application Factory"""

from flask import Flask

from config import Config
from app.extensions import db, migrate, sess


def create_app(config_class=Config):
    """Factory function
    @Return: application instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)

    # Register blueprints
    from app.balance import balance as balance_bp

    app.register_blueprint(balance_bp, url_prefix="/balance")

    @app.route("/test/")
    def test_page():
        return "<h1> Test 1234 </h1>"

    return app
