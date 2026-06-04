from app import db
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TipoFigurinha(str, Enum):
    LEGEND_OURO = "legends_ouro"
    LEGEND_BRONZE = "legends_bronze"
    BRILHANTE = "brilhante"
    COMUM = "comum"
    
class PosicaoFigurinha(str, Enum):
    GOLEIRO = "goleiro"
    ZAGUEIRO = "zagueiro"
    MEIOCAMPO = "meio-campista"
    ATACANTE = "atacante"

@dataclass
class Figurinha:
    numero: str
    tipo: str
    posicao: str
    created_at: datetime
    updated_at: datetime
    id: int = None

class FigurinhaModel(db.Model):
    __tablename__ = 'figurinhas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)