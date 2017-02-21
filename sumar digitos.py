def digitos(n):
    if (n<10):
        return n
    else:
        return (int)((n%10)+(digitos(n/10)))
print (digitos(18))
