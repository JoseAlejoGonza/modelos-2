def bin_dec(n):
    if (n<10):
        return n
    else:
        return (int)((n%2)+ (bin_dec(n/10))*2)
print (bin_dec(111))
