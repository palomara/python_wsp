print("*************************************")
print("Bem-vindo ao jogo de Adivinhação ! ")
print("*************************************")
numero_secreto = 42
chute = int(input("Digite seu número: " ))
print("Você digitou:" , chute )
acertou = chute ==numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if (acertou ):
    print("Você acertou!")
else :
        if(maior):
            print("Você Errou! O seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você Errou! O seu chute foi menor que o numero secreto")
            print(" Fim do jogo")
            
