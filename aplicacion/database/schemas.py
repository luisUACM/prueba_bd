from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import Time

from .config import db

class DocumentoEvento(db.Model):
    __tablename__ = "documento_evento"
    
    id_documento_evento: Mapped[int] = mapped_column(primary_key=True)
    fecha_expiracion: Mapped[Date] = mapped_column(Date)
    hora_expiracion: Mapped[Time] = mapped_column(Time)
    tipo_documento: Mapped[str] = mapped_column(String(50))
    subtipo_documento: Mapped[str] = mapped_column(String(50))
    ruta_archivo: Mapped[str] = mapped_column(String(50))



