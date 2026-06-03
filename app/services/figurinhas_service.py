from domain.figurinhas_domain import Figurinha
from repositories.figurinhas_repo import FigurinhaRepository

class CreateFigurinhaService:
    def __init__(self, repository: FigurinhaRepository):
        self.repository = repository

    def execute(self, numero: str, posicao: str) -> Figurinha:
        self._validate(numero, posicao)
        
        nova_figurinha = Figurinha(numero=numero, posicao=posicao)
        
        self.repository.create(nova_figurinha)
        
        return nova_figurinha

    def _validate(self, numero: str, posicao: str) -> None:
        self._not_null(numero, "numero")
        self._not_null(posicao, "posicao")
        
        if numero.isdigit() and int(numero) < 0:
            raise ValueError("O número da figurinha não pode ser negativo.")

    def _not_null(self, value: str, field_name: str) -> None:
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError(f"O campo '{field_name}' é obrigatório e não pode ser vazio.")
        
class ListFigurinhasService:
    def __init__(self, repository: FigurinhaRepository):
        self.repository = repository

    def execute(self) -> list[Figurinha]:
        return self.repository.get_all()
    

class GetFigurinhaByIdService:
    def __init__(self, repository: FigurinhaRepository):
        self.repository = repository

    def execute(self, figurinha_id: int) -> Figurinha | None:
    
        if self.repository.get_by_id(figurinha_id) is None:
            raise ValueError("Figurinha não encontrada.")
        
        return self.repository.get_by_id(figurinha_id)
    
class DeleteFigurinhaService:
    def __init__(self, repository: FigurinhaRepository):
        self.repository = repository

    def execute(self, figurinha_id: int) -> None:
        self.repository.delete(figurinha_id)
