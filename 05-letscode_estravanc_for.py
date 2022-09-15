#for

nomes = ['são paulo','londre','toquio','paris']
for nome in nomes:
    print(nome)


#comparando com while
cont = 0
nomes = ['são paulo','londre','toquio','paris']
while cont < len(nomes):
    print(nomes[cont])
    cont =cont + 1

nomes = ['são paulo','londre','toquio','paris']
for names in nomes:
    print(names)


dados = {
    'nome':'sao paulo',
    'estado':'sao paulo',
    'area': 1521,
    'população': 121800
}

for chave in dados:
    print(f"{chave}: {dados[chave]}")


nomes = ['são paulo','londre','toquio','paris']
for names in nomes:
    names = 'rio de janeiro'
print(nomes)



for posicao in range(len(nomes)):
    nomes[posicao] = 'rio de janeiro'
print(nomes)

print(list(range(10)))




