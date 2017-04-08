def ListaDigitos(n):
    if(n==0):
        return []
    else:
        return [n%10]+ListaDigitos(n/10)