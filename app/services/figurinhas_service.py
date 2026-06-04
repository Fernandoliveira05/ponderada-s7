import uuid
from datetime import datetime
from app.domain.figurinhas_domain import Figurinha, TipoFigurinha, PosicaoFigurinha
from app.repositories.figurinhas_interface import IFigurinhaRepository
from enum import Enum

class CreateFigurinhaService:
    def __init__(self, repository: IFigurinhaRepository):
        self.repository = repository

    def execute(self, numero: str, posicao: str, tipo: str) -> Figurinha:
        self._validate(numero, posicao, tipo)
    
        nova_figurinha = Figurinha(
            numero=numero,
            tipo=tipo,
            posicao=posicao,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
    
        self.repository.create(nova_figurinha)
        return nova_figurinha

    def _validate(self, numero: str, posicao: str, tipo: str) -> None:
        self._not_null(numero, "numero")
        self._not_null(posicao, "posicao")
        self._not_null(tipo, "tipo")

        tipos_validos = [t.value for t in TipoFigurinha]
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo inválido. Valores aceitos: {tipos_validos}")
        
        posicoes_validas = [p.value for p in PosicaoFigurinha]
        if posicao not in posicoes_validas:
            raise ValueError(f"Essa posição não existe! Nossas posições são: {posicoes_validas}")

        if numero.isdigit() and int(numero) < 0:
            raise ValueError("O número da figurinha não pode ser negativo.")

    def _not_null(self, value: str, field_name: str) -> None:
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError(f"O campo '{field_name}' é obrigatório e não pode ser vazio.")
        
class ListFigurinhasService:
    def __init__(self, repository: FigurinhaRepository):
        self.repository = repository

    def execute(self, tipo: str = None, posicao: str = None) -> list[Figurinha]:
        if tipo is not None:
            tipos_validos = [t.value for t in TipoFigurinha]
            if tipo not in tipos_validos:
                raise ValueError(f"Tipo inválido. Valores aceitos: {tipos_validos}")
        
        if posicao is not None:
            posicoes_validas = [p.value for p in PosicaoFigurinha]
            if posicao not in posicoes_validas:
                raise ValueError(f"Posição inválida. Valores aceitos: {posicoes_validas}")
        
        return self.repository.get_all(tipo=tipo, posicao=posicao)

class GetFigurinhaByIdService:
    def __init__(self, repository: IFigurinhaRepository):
        self.repository = repository

    def execute(self, figurinha_id: int) -> Figurinha | None:
    
        if self.repository.get_by_id(figurinha_id) is None:
            raise ValueError("Figurinha não encontrada.")
        
        return self.repository.get_by_id(figurinha_id)
    
class DeleteFigurinhaService:
    def __init__(self, repository: IFigurinhaRepository):
        self.repository = repository

    def execute(self, figurinha_id: int) -> None:
        self.repository.delete(figurinha_id)
        

class AtualizaFigurinhaService:
    def __init__(self, repository: IFigurinhaRepository):
        self.repository = repository 
        
    def execute(self, figurinha_id: int, numero: str, posicao: str, tipo: str) -> Figurinha:
        figurinha = self.repository.get_by_id(figurinha_id)
        if figurinha is None:
            raise ValueError("Figurinha não encontrada.")

        self._validate(numero, posicao, tipo)

        figurinha.numero = numero
        figurinha.posicao = posicao
        figurinha.tipo = tipo
        figurinha.updated_at = datetime.utcnow()
        
        self.repository.update(figurinha)
        return figurinha
        
    def _validate(self, numero: str, posicao: str, tipo: str) -> None:
        if numero is None or not str(numero).strip():
            raise ValueError("O campo 'numero' é obrigatório e não pode ser vazio.")
        if posicao is None or not str(posicao).strip():
            raise ValueError("O campo 'posicao' é obrigatório e não pode ser vazio.")
        if tipo is None or not str(tipo).strip():
            raise ValueError("O campo 'tipo' é obrigatório e não pode ser vazio.")

        tipos_validos = [t.value for t in TipoFigurinha]
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo inválido. Valores aceitos: {tipos_validos}")
        
        posicoes_validas = [p.value for p in PosicaoFigurinha]
        if posicao not in posicoes_validas:
            raise ValueError(f"Essa posição não existe! Nossas posições são: {posicoes_validas}")

        if numero.isdigit() and int(numero) < 0:
            raise ValueError("O número da figurinha não pode ser negativo.")