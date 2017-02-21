def Factorial(fac):
    if (fac>0):
        resultado=fac*Factorial(fac-1)
        return resultado
    if (fac<0):
        return "error"
    else:
        return 1
print (Factorial(3))
