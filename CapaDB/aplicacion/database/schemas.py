from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import Integer

from .config import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    correo: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))

@dataclass
class UsuarioDTO():
    correo: str
    password: str
