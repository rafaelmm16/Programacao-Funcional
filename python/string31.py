def cal(a,b):
    q=(b-1)
    w=(a*q)
    if q==a:
        return w
    else:
        print(w)
        return cal (a,q)
