meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
nasc = input('Digite a sua data de nascimento no formato DD-MM-AAAA: ')

indice = int(nasc[3:5])-1
mes = meses[indice]

print('Você nasceu no mês de',mes)
