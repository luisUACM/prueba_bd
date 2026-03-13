from flask import current_app as app
from flask import render_template
import requests
from ..modelo.dto import UsuarioDTO
from flask import request

@app.route('/usuario/guardar')
def usuario_guardar():
    return render_template('crear_usuario.html')

@app.route('/usuario/get/<int:id>')
def usuario_get(id):
    response = requests.get('http://127.0.0.1:5001/usuario', json={'id':id}).json()
    user = UsuarioDTO(response['correo'], response['password'])
    return render_template('get_usuario.html', usuario=response)

@app.post('/usuario/guardar/redirect')
def usuario_guardar_redirect():
    response = requests.post('http://127.0.0.1:5001/usuario', json={'correo':request.form['correo'], 'password':request.form['password']})
    return '', response.status_code