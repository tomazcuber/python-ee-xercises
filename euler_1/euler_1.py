def euler_1(a,b,N):
    #Calcula a soma de todos os multiplos de a ou b menores que N.
    sum = 0
    for i in range(N):
        if i % a == 0 or i % b == 0:
            sum += i
    return sum

if __name__ == "__main__":
    result_10 = euler_1(3,5,10)
    result_1000 = euler_1(3,5,1000)
    print("A soma dos multiplos de 3 e 5 menores que 10 e: {}".format(result_10)) 
    print("A soma dos multiplos de 3 e 5 menores que 1000 e: {}".format(result_1000))

