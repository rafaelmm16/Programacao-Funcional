def o():
   di=int(input("Digite 1 para Juros:" "\n" "Digite 2 para Conversao de moedas:" "\n" "Digite 3 para Financiamento Residencial:"))
   if (di==1):
      aa=float(input("Digite o juros:"))
      bc=int(input("Digite o tempo:"))
      cc=int(input("Digite o capital:"))
      z=(aa/100)*bc*cc
      print (z+cc)
   elif (di==2):
       ac=float(input("Digite o valor:"))
       xz=(ac*0.30)
       zx=ac*(320/100)
       print("O valor em dolar e", xz, "\n", "O valor em real e",zx)
   
   elif (di==3):
        print ("O banco so financiara 80% do valor")
        j=0.0034
        ca=float(input("Digite o valor:"))
        print(j*0.8*ca+ca)
