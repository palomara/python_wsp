##x = 0
##pessoas = []
##
##while x < 4:
##    nome = input('Qual o seu nome? ')
##    ##evitar que o nome joão seja adicionado a lista
##    if nome == 'joao':
##        break
##    pessoas.append(nome)
##    x += 1
##print(pessoas)

compras = ['arroz', 'feijao', 'macarrão', 'carne']

for i in compras:
    print(i)

nome = 'joaquim'

for i in nome:
    print(i)

vendas = [1000, 450, 300, 820, 600]

total = 0

for i in vendas:
    total += i
    print(total)

for i in vendas:
    total += i
print(total)

cores = ['verde':'green', 'preto': 'black', 'azul': 'blue']

for i in cores:
    print(i)
    print(i, ':', cores[i])

compras = [['arroz', 'feijão', 'macarrão'], ['carne', 'frango', 'peixe'], ['leite', 'iogurte']]
for i in compras:
    for item in i:
        print(item)

for i in range(0,10):
    print(i)



    
