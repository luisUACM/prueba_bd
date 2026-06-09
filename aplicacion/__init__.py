from flask import Flask
from aplicacion.database.config import db

def crear_app():
    
    app = Flask(__name__)
                                                                   #usuario :  contraseña              /nombre_bd
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin_agent:9q70MdN915@localhost/isolated_db_test'
    app.config['DEBUG'] = True
    
    db.init_app(app)

    with app.app_context():
        from .api import rutas
        from aplicacion.database.schemas import DocumentoEvento

        db.create_all()
        return app