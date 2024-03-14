from abc import ABC, abstractmethod
class camisaEsportiva(ABC):
    @abstractmethod
    def InfoProduto(self) -> str:
        pass