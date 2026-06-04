from app import db
from app.domain.figurinhas_domain import Figurinha, FigurinhaModel
from app.repositories.figurinhas_interface import IFigurinhaRepository

class FigurinhaRepository(IFigurinhaRepository):
    def create(self, figurinha: Figurinha) -> Figurinha:
        db_model = FigurinhaModel(
            numero=figurinha.numero,
            tipo=figurinha.tipo,
            posicao=figurinha.posicao,
            created_at=figurinha.created_at,
            updated_at=figurinha.updated_at
        )
        
        db.session.add(db_model)
        db.session.commit()
        
        figurinha.id = db_model.id
        return figurinha
    
    def get_all(self, tipo: str = None, posicao: str = None) -> list[Figurinha]:
        query = FigurinhaModel.query
    
        if tipo:
            query = query.filter(FigurinhaModel.tipo == tipo)
        if posicao:
            query = query.filter(FigurinhaModel.posicao == posicao)
    
        db_models = query.all()
        return [
            Figurinha(
                id=db_model.id,
                numero=db_model.numero,
                posicao=db_model.posicao,
                tipo=db_model.tipo,
                created_at=db_model.created_at,
                updated_at=db_model.updated_at
            )
            for db_model in db_models
        ]

    def get_by_id(self, figurinha_id: int) -> Figurinha | None:
        db_model = FigurinhaModel.query.get(figurinha_id)
        if not db_model:
            return None
            
        return Figurinha(
            id=db_model.id,
            numero=db_model.numero,
            posicao=db_model.posicao,
            tipo=db_model.tipo,
            created_at=db_model.created_at,
            updated_at=db_model.updated_at
        )
    
    def delete(self, figurinha_id: int) -> None:
        db_model = FigurinhaModel.query.get(figurinha_id)
        if db_model:
            db.session.delete(db_model)
            db.session.commit()
            
    def update(self, figurinha: Figurinha) -> None:
        db_model = FigurinhaModel.query.get(figurinha.id)
        if db_model:
            db_model.numero = figurinha.numero
            db_model.posicao = figurinha.posicao
            db_model.tipo = figurinha.tipo
            db_model.updated_at = figurinha.updated_at
            db.session.commit()