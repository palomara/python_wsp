meses = ('janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

alunos =['Joao','Maria','Pedro','Helena']
alunos2 =['Jose','Jailson']
nasc = input('Digite a sua data de nascimento no formato dd-mm-aa:')
indice = int(nasc[3:5])-1
mes = meses [indice]
print('voce nasceu no mes de',mes)

