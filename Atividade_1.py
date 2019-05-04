meses = ("Janeiro", "Feveiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
alunos = ["Joao", "Maria", "Pedro", "Helena"]

data_nasc = input("Digite a sua data de nascimento no formado DD-MM-AAAA:  " )
indice = int(data_nasc[3:5] ) - 1
mes = meses [indice]

print("\nVocê nasceu no mes de: ", mes)
