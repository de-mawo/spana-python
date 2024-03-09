from flask import Flask

from config import Config

def create_app(config_class=Config):
    """Factory function
    @Return: application instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions
    
    
    
    
    # Register blueprints
    from app.balance import balance as balance_bp
    app.register_blueprint(balance_bp, url_prefix='/balance')
    
    
    @app.route('/test/')
    def test_page():
        return '<h1> Test 1234 </h1>'
    
    return app