from fabricaEsportiva import  fabricaEsportiva
from camisaEsportiva import camisaEsportiva
from camisasEsportivasTimes import camisaVasco, camisaBrasil, camisaFluminense, camisaBotafogo, camisaFlamengo


class Nike(fabricaEsportiva):
    def produtoDesportivo(self) -> camisaEsportiva:
        return camisaBrasil()


class Adidas(fabricaEsportiva):
    def produtoDesportivo(self) -> camisaEsportiva:
        return camisaFlamengo()


class Puma(fabricaEsportiva):
    def produtoDesportivo(self) -> camisaEsportiva:
        return camisaBotafogo()


class Umbro(fabricaEsportiva):
    def produtoDesportivo(self) -> camisaEsportiva:
        return camisaFluminense()


class Kappa(fabricaEsportiva):
    def produtoDesportivo(self) -> camisaEsportiva:
        return camisaVasco()
