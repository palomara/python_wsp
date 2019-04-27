cores = {'verde': 'green', 'vermelho': 'red', 'preto': 'black', 'branco': 'white'}
cor = input('Escolha a cor que deseja traduzir: ').lower()
traducao = cores.get(cor, 'Esta cor não consta no meu dicionário')
print(traducao)
