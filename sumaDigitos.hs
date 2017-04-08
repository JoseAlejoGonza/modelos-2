def SumaDigitos(n):
   if(n==0):
        
        return (0)
   else:
        if(n%2==0):
            return n%10+SumaDigitos(n/10) 
        else:
            return SumaDigitos(n/10)