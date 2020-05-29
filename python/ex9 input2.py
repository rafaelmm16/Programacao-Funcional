import random
def crescente():
    a=random.randrange(1,10)
    b=random.randrange(1,10)
    c=random.randrange(1,10)
    if a<b and b<c:
        print (a,b,c)
    elif a<c and c<b:
        print(a,c,b)
    elif b<c and c<a:
        print(b,c,a)
    elif b<a and a<c:
        print(b,a,c)
    elif c<a and a<b:
        print(c,a,b)
    elif c<b and b<a:
        print(c,b,a)
    else:
        print("Deu ruim!!")
