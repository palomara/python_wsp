peso1 = float(input('Digite o peso da primeira prova: '))
peso2 = float(input('Digite o peso da segunda prova: '))
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

media = ((peso1*nota1) + (peso2*nota2)) / (peso1+peso2)

print('A média do aluno é:',media)

input('Aperte enter para sair')
