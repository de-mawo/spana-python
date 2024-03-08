"""Entry Point to run the App"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)