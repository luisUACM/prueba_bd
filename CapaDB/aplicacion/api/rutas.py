from flask import current_app as app
from ..services.serviceA import guardar_usuario, get_usuario
from flask import request, jsonify

@app.route('/usuario', methods=['POST', 'GET'])
def api_usuario():
    if request.method == 'POST':
        status = guardar_usuario(request.json)
        return '', status
    elif request.method == 'GET':
        usuario = get_usuario(request.json['id'])
        return jsonify(usuario)
    else: 
        return '', 400

@app.route('/dummy')
def dummy():
    return 'Success'