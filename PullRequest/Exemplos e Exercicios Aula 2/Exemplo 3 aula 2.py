cores ={'vermelho' : 'red' , 'azul' : 'blue' , 'verde' : 'green' , 'branco' : 'white' }
cor = input('Escolha a cor que deseja traduzir: ' ).lower()
traducao = cores.get (cor, 'Esta cor nao consta no dicionario' )
print (traducao )
