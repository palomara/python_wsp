x = 0
while x < 1:
    nome = input('Qual o seu nome?')

while x < 4:
    nome = input('Qual o seu nome?')
    x = x + 1

while x < 4:
    nome = input('Qual o seu nome?')
    x += 1

while x < 4:
    nome = input('Qual o seu nome?')
    print('Olá', nome)
    x = x + 1

pessoas = []

while x < 4:
    nome = input('Qual o seu nome?')
    pessoas.append(nome)
    x = x + 1
    print(pessoas)

while x < 4:
    nome = input('Qual o seu nome?')
    pessoas.append(nome)
    x = x + 1
print(pessoas)

while True:
    nome = input('Qual o seu nome?')
    pessoas.append(nome)
    x = x + 1
    print(pessoas)

while 'joao' not in pessoas:
    nome = input('Qual o seu nome?')
    pessoas.append(nome)
    x = x + 1
    print(pessoas)

while True:
    nome = input('Qual o seu nome?')
    if nome == 'joao':
        continue
    pessoas.append(nome)
    x = x + 1
    print(pessoas)

while x < 4:
    nome = input('Qual o seu nome?')
    if nome == 'joao':
        continue
    pessoas.append(nome)
    x = x + 1
    print(pessoas)

while x < 4:
    nome = input('Qual o seu nome?')
    if nome == 'joao':
        break
    pessoas.append(nome)
    x = x + 1
    print(pessoas)
