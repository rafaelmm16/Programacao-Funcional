def rec(x):
    if x<=20 and x%2==0:
        print (x)
        return rec (x+2)
    elif x<=20 and x%2!=0:
        print (x)
        return rec (x+3)
