def ex():
    op=int(input("Tecle 1 para realizar o cálculo de juros:\nTecle 2 para realizar a conversão de moeda:\nTecle 3 para financiar o residencial CEUNES Village Dell Porto:\n"))
    if op==1:
        um=float(input("Insira o seu capital:"))
        ds=float(input("Insira a taxa de juros:"))
        tres=int(input("Insira o tempo em que deseja financiar:"))
        valor=um*ds*tres/tres+um
        print ("O valor final do financiamento ao mes e:", valor)

    elif op==2:
        opa1=int(input("Tecle 1 para converter em dolar:\n" "Tecle 2 para converter em real:"))
        if opa1==1:     
            moeda=float(input("Insira o valor da moeda:"))
            cambio=float(input("Insira o valor do cambio:"))
            v=moeda*cambio
            print ("O valor em dolar e de:", v)
        elif opa1==2:
            m=float(input("Insira o valor da moeda:"))
            c=float(input("Insira o valor do cambio:"))
            vlr=m/c
            print ("O valor em real e de:", vlr)

    elif op==3:
        x=int(input("Insira o valor do financiamento:"))
        y=int(input("Insira o tempo em que deseja financiar:"))
        valor=x*0.34/y
        total=valor*80/100+x
        print ("O valor do seu financiamento e de:", total)
