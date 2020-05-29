def multi(x,y):
    if y==0:
        return 0
    else:
        a=x*y
        print(x,"*", y , "=", a)
        return multi(x,y-1)
