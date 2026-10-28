fila = []
menu = 'SIM'

while menu == 'SIM':
    print("Fila do refeitório")
    print('1- Adicionar alguém no fim da fila')
    nome = input("Digite um nome para ser adicionado à fila:")

    fila.append(nome)

    for nome in fila:
        print(nome)

    menu = input("Deseja adicionar mais um nome? (SIM/NÃO)") .upper()