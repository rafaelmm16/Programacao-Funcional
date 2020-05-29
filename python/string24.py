I=[7,9,10,12]
p=int(input("Digite um numero:"))
for e in I:
    if e==p:
        print("Elemento encontrado!%d"%e,end=("<--"))
        break
    else:
        print("Elemento nao encontrado.%d"%e)
