from flask import current_app as app
from flask import render_template
import requests
from ..modelo.dto import UsuarioDTO
from flask import request
import os
from weasyprint import HTML
from flask import send_from_directory


@app.route('/documento')
def usuario_guardar():
    return render_template('buscar_documento.html')

@app.get('/documento/ver')
def usuario_get():
    nombre = request.form.get('nombre')
    nombre += '.pdf'
    return render_template('visor.html', ruta_archivo=nombre) 

@app.route('/documento/<path:filename>')
def documentos(filename):
    return send_from_directory('../documentos', filename)

@app.post('/documento/crear')
def crear_documento():
    texto = request.form.get('form-texto')
    datos = {
    "informacion": texto
    }

    html = render_template(
        "plantilla_pdf_prueba.html",
        **datos
    )
    
    HTML(string="<h1>Hola, Mundo!</h1>").write_pdf()