cores = {'vermelho':'red','verde' : 'green', 'azul' : 'blue', 'branco' : 'white'}
cor = input('Escolha a cor que deseja traduzir: ').lower()
tradução = cores.get(cor, 'Esta cor não consta no dicionário')
print (tradução)
