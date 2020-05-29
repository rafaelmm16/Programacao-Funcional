def inteiros(x,y):
    s=(x/y)
    if s!=0:
        print(s)
        return inteiros(s,y)
    else:
        print("Acabou")
