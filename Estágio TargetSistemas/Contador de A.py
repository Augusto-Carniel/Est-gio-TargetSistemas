# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula 
# ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

string = input("Digite uma string : ")
cont_a = string.lower().count("a")
print(f"A palavra contem {cont_a} letras A")