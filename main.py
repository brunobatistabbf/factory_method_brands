import fabricaEsportiva
from fabricaEsportivaMarcas import Nike, Adidas, Puma, Umbro, Kappa


def Cliente(fabricaesportiva: fabricaEsportiva) -> None:
    fabricaesportiva.InfoProduto()
    print("Teste")


if __name__ == '__main__':
    print("CATALOGO PRODUTOS DESPORTIVOS")
    print("\n1 - Seleção Brasileira")
    print("\n2 - Flamengo")
    print("\n3 - Botafogo")
    print("\n4 - Fluminense")
    print("\n5 - Vasco")

    resposta = int(input("\nDigite uma opção valida:"))
    if (resposta == 1):
        Cliente(Nike())
    elif (resposta == 2):
        Cliente(Adidas())
    elif (resposta == 3):
        Cliente(Puma())
    elif (resposta == 4):
        Cliente(Umbro())
    elif (resposta == 5):
        Cliente(Kappa())
    else:
        print("Insira uma opção válida")
