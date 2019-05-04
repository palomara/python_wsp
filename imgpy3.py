cores = {'vermelho':'red','blue':'azul','verde':'green','branco':'white'}
cor = input('Escolha a cor que deseja traduzir:').lower()
traducao =cores.get(cor,'Esta cor não consta no dicionario')
print(traducao)

