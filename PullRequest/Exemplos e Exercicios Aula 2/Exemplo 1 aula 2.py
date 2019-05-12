meses = ('Janeiro', 'Fevereiro', 'Março' ,'Abril', 'Maio', 'Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro' )
alunos = ['Joao' , 'Maria' , 'Pedro' , 'Helena' ]
nasc = input('Digite a sua data de nascimento no formato DD-MM-AAA'  )
indice = int(nasc[3:5] )-1
mes = meses[indice]
print('\nVocê nasceu no mês de:' , mes )


