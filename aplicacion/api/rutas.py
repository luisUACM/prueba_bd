from flask import current_app as app
from flask import render_template
import requests
from flask import request
import os
from weasyprint import HTML
from flask import send_from_directory
from ..database.schemas import DocumentoEvento
from aplicacion.database.config import db
from datetime import date, datetime
from flask import redirect
from flask import url_for
from weasyprint import CSS

@app.route('/documento')
def usuario_guardar():
    return render_template('buscar_documento.html')

@app.get('/documento/ver')
def documento_get():
    nombre = request.args.get('nombre')
    nombre += '.pdf'
    return render_template('visor.html', ruta_archivo=nombre) 

@app.route('/documento/<path:filename>')
def documentos(filename):
    return send_from_directory('../documentos', filename)

@app.post('/documento/crear')
def crear_documento():
    texto = request.form.get('form-texto')
    datos = {
    "informacion": texto,
    "nombre_imagen": 'prueba.jpg'
    }

    html = render_template(
        "plantilla_pdf_prueba.html",
        **datos
    )
    nombre_archivo = f'{texto}.pdf'

    css = CSS('./aplicacion/static/css/cartas.css')
    HTML(string=html, base_url=app.config['DIRECTORIO_BASE'] + '/documentos/imagenes').write_pdf(app.config['FOLDER_DOCUMENTOS'] + '/' + nombre_archivo, stylesheets=[css])
    
    documento_evento = DocumentoEvento()
    documento_evento.fecha_expiracion = date.today()
    documento_evento.hora_expiracion = datetime.now().time()
    documento_evento.tipo_documento = 'PRUEBA'
    documento_evento.subtipo_documento = 'PRUEBA2'
    documento_evento.ruta_archivo = nombre_archivo

    db.session.add(documento_evento)
    db.session.commit()

    return redirect( url_for('documento_get', nombre=texto)
)