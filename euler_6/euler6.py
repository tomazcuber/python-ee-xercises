def euler_6(n=100):
        """Resolve a diferença entre o quadrado da soma e a soma dos quadrados dos n primeiros números naturais."""
        soma_quadrados = soma_dos_quadrados(n)
        quadrado_soma = soma_dos_naturais(n) ** 2

        return soma_quadrados, quadrado_soma, quadrado_soma - soma_quadrados

def soma_dos_quadrados(n):
    """Retorna a soma dos quadrados dos n primeiros números naturais."""
    return ((n+1)*n*(2*n+1)) // 6

def soma_dos_naturais(n):
    """Retorna soma dos n primeiros números naturais."""
    if n % 2 == 0:
        return (n//2)*(1 + n)
    else:
        return ((n//2) + 1) * n

if __name__ == "__main__":
    print("Digite a quantidade de númeos naturais da entrada: ");
    n = int(input())

    print("a soma dos quadrados dos primeiros {} números naturais é: {}".format(100, euler_6(n)[0]))
    print("o quadrado da soma dos {} primeiros números naturais é {}".format(100,euler_6(n)[1]))
    #print("a soma dos {} primeiros números naturais é {}".format(99,soma_dos_naturais(99)))
    print("{} - {} = {}".format(euler_6(n)[1],euler_6(n)[0],euler_6(n)[2]))
