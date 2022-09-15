from statistics import median


def calcula_media(*args):
    print(args, type(args))
    soma = sum(args)
    media = soma / len(args)
    print(media)
    return media

calcula_media(10,8,9)



def print_inf(**kwargs):
    print(kwargs,type(kwargs))
print_inf(nome='pablo',sobrenome='abreu')