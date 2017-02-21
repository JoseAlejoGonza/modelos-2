def palindromo(palabra):
    if len(palabra) < 2:
        return "si es palindromo"
    if palabra[0] != palabra[-1]:
        return "no es palindromo"
    return palindromo(palabra[1:-1])
print(palindromo('amigo n ogima'))
