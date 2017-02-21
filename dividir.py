def dividir (n,m):
    if (m>n):
        return 0
    return dividir (n-m, m)+1
print (dividir(5,2))
