a=[7,9,10,12]
p=int(input("Digite um numero a pesquisa:"))
for e in a:
    if e>=p:
        print("Elemento encontrado")
        break
    else:
        print("Elemento nao encontrado")
