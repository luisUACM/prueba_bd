from flask import Flask

def crear_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin_agent:9q70MdN915@localhost/isolated_db_test'
    app.config['DEBUG'] = True
    
    with app.app_context():
        from .api import rutas

        return app