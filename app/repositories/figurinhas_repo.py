from domain.figurinhas_domain import Figurinha
from domain.figurinhas_domain import db, FigurinhaModel

class FigurinhaRepository:
    def create(self, figurinha: Figurinha) -> None:
        db_model = FigurinhaModel(
            id=figurinha.id,
            numero=figurinha.numero,
            posicao=figurinha.posicao,
            created_at=figurinha.created_at,
            updated_at=figurinha.updated_at
        )
        
        db.session.add(db_model)
        db.session.commit()
    
    def get_all(self) -> list[Figurinha]:
        db_models = FigurinhaModel.query.all()
        return [
            Figurinha(
                id=db_model.id,
                numero=db_model.numero,
                posicao=db_model.posicao,
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
            db_model.updated_at = figurinha.updated_at
            db.session.commit()