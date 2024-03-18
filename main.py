import fabricaEsportiva
from fabricaEsportivaMarcas import Nike, Adidas, Puma, Umbro, Kappa

def Client(prefabrication: fabricaEsportiva) -> None:
    produto = prefabrication.produtoDesportivo()
    produto.InfoProduto()


if __name__ == '__main__':
    print("\nCATALOGO CAMISAS ESPORTIVAS")
    print("1 - Seleção Brasileira")
    print("2 - Flamengo")
    print("3 - Botafogo")
    print("4 - Fluminense")
    print("5 - Vasco")

    resposta = int(input("\nDigite uma opção valida:\n"))
    if (resposta == 1):
        Client(Nike())
    elif (resposta == 2):
        Client(Adidas())
    elif (resposta == 3):
        Client(Puma())
    elif (resposta == 4):
        Client(Umbro())
    elif (resposta == 5):
        Client(Kappa())
    else:
        print("Insira uma opção válida")
