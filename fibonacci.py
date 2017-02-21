def fibonacci(fibo):
    if (fibo==0):
        return (fibo)
    if (fibo==1):
        return (fibo)
    if (fibo>1):
        resultado=fibonacci(fibo-1)+fibonacci(fibo-2)
        return resultado
    else:
        return "error"
print (fibonacci(12))
