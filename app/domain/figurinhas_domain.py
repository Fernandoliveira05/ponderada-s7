# infra/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FigurinhaModel(db.Model):
    __tablename__ = 'figurinhas'
    
    id = db.Column(db.BigInteger, primary_key=True)  # uuid.int gera números grandes
    numero = db.Column(db.String(50), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)