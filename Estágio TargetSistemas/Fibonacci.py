# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 
# 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem 
# que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
# avisando se o número informado pertence ou não a sequência.

primeiro_num = 0
segundo_num = 1

numero = int(input("Digite o numero que deseja avaliar na sequencia de Fibonacci : "))

if numero == 0 or numero == 1 :
    print("O numero faz parte da sequencia de Fibonacci")
else :
    aux = primeiro_num + segundo_num
    while aux<=numero :
        if aux==numero :
            print("O numero faz parte da sequencia de Fibonacci")
            exit(0)
        else :
            primeiro_num=segundo_num
            segundo_num=aux
            aux = primeiro_num + segundo_num

    print("O numero nao faz parte da sequencia de Fibonacci")