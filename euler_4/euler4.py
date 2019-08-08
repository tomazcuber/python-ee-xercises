def euler_4(ndigits=3):
    """Encontra o maior número palindrômico que é produto de dois números inteiros A e B cujo número de dígitos (ndigits) é passado como parâmetro. Seu valor padrão é 3., logo quando chamada apenas euler_4() sem parâmetros, o valo de ndigits será automaticamente 3."""
    min_num = 10 ** (ndigits-1)
    max_num = 10 ** ndigits - 1
    print("Fator mínimo: {}".format(min_num))
    print("Fator máximo: {}".format(max_num))
    
    palindrome = 0
    max_palindrome = 0 
    num_A = 0
    num_B = 0
    for i in range(min_num, max_num + 1):
        for j in range(min_num, max_num + 1):
            current = i * j
            if(str(current) == str(current)[::-1]):
                    palindrome = current
                    if(palindrome > max_palindrome):
                        max_palindrome = palindrome
                        num_A = i
                        num_B = j
    print("O maior produto palindrômico de dois inteiros de {} dígitos é: {}, que é produto de {} e {}.".format(ndigits,max_palindrome,num_A, num_B))                    

if __name__ == "__main__":
    euler_4() #Chama euler_4() sem parâmetro algum, levando ndigits ao seu valor padrão 3.
