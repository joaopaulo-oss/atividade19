# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
n = 1
n = int(input("Digite um numero inteiro: "))
while n >= 0:
    fatorial = 1
while n <= 1:
        fatorial = fatorial * n
n = n - 1
    print(fatorial)  
 
  