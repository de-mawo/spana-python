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
    
    
    @app.route('/test/')
    def test_page():
        return '<h1> Test 1234 </h1>'
    
    return app