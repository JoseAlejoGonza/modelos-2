def mcd(n,m):
    if (m==0):
        return n
    else:
        return mcd(m, n%m)
print (mcd(100,52))
