def ValAbs(n):
    if (n<0):
        resultado=ValAbs(n*-1)
        return resultado
    else:
        return (n*1)
print (ValAbs(0))
