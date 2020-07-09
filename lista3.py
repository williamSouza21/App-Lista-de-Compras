class Lista:
    def __init__(self, quantidade, tipo_unid, comida):
        self.quantidade = quantidade
        self.tipo_unid = tipo_unid
        self.comida = comida

    def exibirListaPronta(self):
        print("[ ] {} {} de {}.".format(self.quantidade, self.tipo_unid, self.comida))

linha = []
contador = 0
while(True):
    letra = input("Digite a 1° Letra do alimento/objeto desejado: ")
    with open("alimentos.txt", "r", encoding="UTF-8") as arquivo:
        lista_de_frutas = []
        for frutas in arquivo:
            if(frutas[0] == "á" and letra == "a"):
                frutas = frutas.strip()
                lista_de_frutas.append(frutas)
            if(frutas[0] == letra):
                frutas = frutas.strip()
                lista_de_frutas.append(frutas)
        arquivo.close()

    rep = 0
    while(rep < len(lista_de_frutas)):
        print(rep, lista_de_frutas[rep])
        rep = rep + 1

    comida = int(input("Digite o número do alimento/objeto: "))
    while(comida<0 or comida >= len(lista_de_frutas)):
        if(comida<0 or comida >= len(lista_de_frutas)):
            comida = int(input("Digite o número do alimento/objeto: "))

    quantidade = input("Digite quantas unidades de {} você quer: ".format(lista_de_frutas[comida].upper()))
    quantidade1 = int(quantidade)


    with open("tipo_unidade.txt", "r", encoding="UTF-8") as arquivo:
        lista_de_unidades = []
        for tipo_unid in arquivo:
            tipo_unid = tipo_unid.strip()
            lista_de_unidades.append(tipo_unid)
        arquivo.close()

    rep = 0
    while(rep < len(lista_de_unidades)):
        print(rep, lista_de_unidades[rep])
        rep = rep + 1

    tipo_unidade = int(input("Escolha o tipo de unidade: "))
    while(tipo_unidade < 0 or tipo_unidade >= len(lista_de_unidades)):
        if(tipo_unidade < 0 or tipo_unidade >= len(lista_de_unidades)):
            tipo_unidade = int(input("Escolha o tipo de unidade: "))
            if(quantidade1 == 1 and tipo_unidade == 3):
                lista_de_unidades[tipo_unidade] = "copo"
            elif(quantidade1 == 1 and tipo_unidade == 4):
                lista_de_unidades[tipo_unidade] = "garrafa"
            elif(quantidade1 == 1 and tipo_unidade == 5):
                lista_de_unidades[tipo_unidade] = "pote"
            elif(quantidade1 == 1 and tipo_unidade == 6):
                lista_de_unidades[tipo_unidade] = "sachê"
            elif(quantidade1 == 1 and tipo_unidade == 7):
                lista_de_unidades[tipo_unidade] = "refil"
            elif(quantidade1 == 1 and tipo_unidade == 8):
                lista_de_unidades[tipo_unidade] = "lata"

    print(quantidade1, lista_de_unidades[tipo_unidade], "de", lista_de_frutas[comida])

    lista1 = Lista(quantidade1, lista_de_unidades[tipo_unidade], lista_de_frutas[comida])
    linha.append(lista1)

    continuar = input("Deseja continuar fazendo a lista? (s/n): ")
    if(continuar != "s"):
        inicio = 0
        print("\nSUA LISTA ESTÁ PRONTA!")
        while(inicio <= contador):
            linha[inicio].exibirListaPronta()
            inicio = inicio + 1
        break
    else:
        contador = contador + 1
