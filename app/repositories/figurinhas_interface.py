from abc import ABC, abstractmethod


class IFigurinhaRepository(ABC):
    @abstractmethod
    def create(self, figurinha):
        pass

    @abstractmethod
    def get_all(self, tipo: str = None, posicao: str = None):
        pass

    @abstractmethod
    def get_by_id(self, figurinha_id: int):
        pass

    @abstractmethod
    def update(self, figurinha):
        pass

    @abstractmethod
    def delete(self, figurinha_id: int):
        pass