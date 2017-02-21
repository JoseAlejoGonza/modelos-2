def multi (n,m):
    if(n==0):
        return 0
    if(m==0):
        return 0
    if(n==1):
        return m
    if(m==1):
        return n
    if (m>1):
        return n+multi(n, m-1)
    else:
        return -n+multi(n, m+1)
print (multi(5,5))
