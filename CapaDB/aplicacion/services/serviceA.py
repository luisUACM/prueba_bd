from sqlalchemy.orm import Session
from aplicacion.database.schemas import Usuario, UsuarioDTO
from aplicacion.database.config import db

def guardar_usuario(json):
    usuario = Usuario()
    usuario.correo = json['correo']
    usuario.password = json['password']
    session = db.session()
    session.add(usuario)
    session.commit()
    session.close()
    return 201

def get_usuario(id):
    usuario = db.get_or_404(Usuario, id)
    usuario_dto = UsuarioDTO(usuario.correo, usuario.password)
    return usuario_dto