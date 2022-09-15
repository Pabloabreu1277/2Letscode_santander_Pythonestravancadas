dados = {
    'nome':'sao paulo',
    'estado':'sao paulo',
    'area': 1521,
    'população': 121800
}

print(type(dados))
print(dados)

dados['pais'] = 'brasil'

print(dados)

dados['areakm2']=1500
print(dados)

dados2 = dados
dados2 ['nome'] = 'santos'
print(dados2)
print(dados)

dados3 = dados.copy()

dados3['estado'] = 'rio de janeiro'
print(dados3)

print(dados)


novos_dados = {
    'população': 15,
    'fundação':'25/01/1554'

}

dados.update(novos_dados)
print(dados)


print(dados.get('perfeito'))

print(dados.keys())#retorna alista de chaves de um dicionario
print('___________')
print(dados.values()) #retorna uma lista de valores de um dicionario
print('___________')
print(dados.items())#retorna uma lista de tuplas chave valor de um dicionario

