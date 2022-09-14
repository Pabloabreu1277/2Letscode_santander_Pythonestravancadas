#1.Faça um programa que olhe todos os itens
#  de uma lista e diga quantos deles são pares.

lista = []
i = 0
resultz = []
y = int(input("digite quantos numeros seram cadastrados:"))
for i in range(y):
    i = (float(input("digite um numero")))
    lista.append(i)
    i = i % 2
    if i == 0 :
        resultz.append('numero par')
    else:
        resultz.append('numero impar')
print(lista)
print(resultz)
