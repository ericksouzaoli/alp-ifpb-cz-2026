estojo = []
add = "SIM"
quant = 0

while add == "S" or add == "SIM":
    add = input("Deseja adicionar um item no estojo?:") .upper()
    if add == 'S' or add == 'SIM':
        item = input("Escreva o item que deseja adicionar:")
        if item == 'carro':
            print ("tente colocar pra ver se cabe")
            continue
        estojo.append(item)
        quant =+ 1
        for item in estojo:
            print (item)
    elif add != "S" or add != "SIM" and  quant == 0:
        print ("fechando estojo vazio")
        break
    elif add != "S" or add != "SIM" and quant >= 1:
         print ("fechando estojo")