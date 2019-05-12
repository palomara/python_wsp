print('******************************')
print('Bem-vindo ao jogo de Advinhação')
print('*******************************')

numero_secreto = 42
chute = int(input('Digite seu número: '))
print('Você digitou: ', chute) 

if (chute == numero_secreto) :
    print ('Você acertou')
else :
    if (chute > numero_secreto) :
        print('Você errou! O seu chute foi MAIOR que o número secreto')
    elif (chute < numero_secreto) :
        print('Você errou! O seu chute foi MENOR que o número secreto')
   
