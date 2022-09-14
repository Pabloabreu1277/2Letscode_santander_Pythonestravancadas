#Listas e tuplas
#LISTAS

nomes_paises = ['brasil','argentina','china','canada','japão']
print("tamanho da lista = ",len(nomes_paises))

print('pais', nomes_paises[4])
print('pais', nomes_paises[-1])
print(nomes_paises)
#nomes_paises[5] ='chile' assim da erro

print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[2:])
print(nomes_paises[:3])
print(nomes_paises[:])
print(nomes_paises[::2])
print(nomes_paises[::-1])

print('brasil' in nomes_paises)
print('chile' in nomes_paises)
#lista vazia
lista_capitais = []
#incluindo dados com o append
lista_capitais.append('brasilia')
lista_capitais.append('buenos aires')
lista_capitais.append('pequim')
lista_capitais.append('bogota')

print(lista_capitais)
#inserir um valor em uma posição
lista_capitais.insert(2,'paris')
print(lista_capitais)

lista_capitais.remove('buenos aires')
print(lista_capitais)

removido=lista_capitais.pop(2)
print(lista_capitais, removido)

#TUPLAS

nomes = ('brasil','argentina','china','canada','japão')
print(nomes)

estado = 'sao paulo',
print(estado,type(estado))


print(len(nomes))
print(nomes[0])

c, f,t,y,o = nomes

print(c,f,t)

print(*nomes)


