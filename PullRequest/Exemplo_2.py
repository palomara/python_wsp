print("**************************************")
print("Bem-vindo Ao jogo de Avidinhação!")
print("***************************************")

numero_secreto = 42

chute = int(input("Digite seu número: ") )
print("Voce digitou :", chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if  (acertou) :
    print("Voce acertou!")

else :
    if (maior) :
        print ("Voce Errou! O seu chute foi maior que o número secreto.")
    elif (menor) :
        print("Voce Errou! O seu chute foi menor que  o número secreto.")
    print("Fim do jogo")
