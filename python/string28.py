def f (m,n):
    x=(m-n)
    if n==0 or n==1:
        return 1
    elif m==0 or m==1:
        return 1
    else:
        return ((m*f(m-1))/((n*f(n-1))*(x*f(x-1))))

f(4,5)
