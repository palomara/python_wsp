print('************************************************')
print('BEM-VINDO AO JOGO DE ADVINHAÇÃO!')
print('************************************************')

numero_secreto=42
chute =int(input('Digite seu numero:'))
print ('voce digitou:',chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print('voce acertou')

else:

    if (maior):
        print('voce errou! oseu chute foi menor que o numero secreto.')
    elif (menor):
        print('voce errou! o seu chute foi menor que o numero secreto.')
        print('fim do jogo')
