cores = {'vermelho' : 'red', 'azul' : 'blue', 'verde' : 'green', 'branco' : 'white'}
cor = input('Escolha a cor que desja traduzir: ').lower()
traducao = cores.get(cor, 'Esta cor nao consta no dicionario')
print (traducao)
