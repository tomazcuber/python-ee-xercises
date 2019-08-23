def euler_6(n=100):
        """Uma breve explicação do que a função faz"""
        soma_quadrados = soma_dos_quadrados(n)
        quadrado_soma = soma_dos_naturais(n) ** 2

        return soma_quadrados, quadrado_soma, quadrado_soma - soma_quadrados

def soma_dos_quadrados(n):
    return ((n+1)*n*(2*n+1)) // 6

def soma_dos_naturais(n):
    if n % 2 == 0:
        return (n//2)*(1 + n)
    else:
        return ((n//2) + 1) * n

print("A soma dos quadrados dos primeiros {} números naturais é: {}".format(100, euler_6()[0]))
print("O quadrado da soma dos {} primeiros números naturais é {}".format(100,euler_6()[1]))
#print("A soma dos {} primeiros números naturais é {}".format(99,soma_dos_naturais(99)))
print("{} - {} = {}".format(euler_6()[1],euler_6()[0],euler_6()[2]))
