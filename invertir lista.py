def invertir (lista):
    if len (lista)== 0:
        return []
    else:
        return [lista[-1]] + invertir(lista[:-1])
    
print (invertir([1,2,3,4]))


