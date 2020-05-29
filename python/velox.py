velox=int(input("Qual e a velocidade do seu carro?"))
if velox > 80:
    multa= velox - 80
    a= multa*5
    print ("Você foi multado no valor de:", a)
if velox <= 80:
    print ("Você não foi multado.")
    
