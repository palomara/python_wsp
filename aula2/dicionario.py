joao = {'nome': 'joao', 'sobrenome': 'pereira', 'profissao': 'programador python', 'filhos': ['pedro', 'maria']}
type(joao)
joao['sobrenome']
len(joao)
del joao['filhos']
joao
joao['profissao'] = 'aposentado'
'sobrenome' in joao
for x in joao:
    print(x)
for x in joao:
    print(x+': '+joao[x])
joao.get('nome', 'Esta informação nao consta no cadastro')
joao.get('idade', 'Esta informação nao consta no cadastro')
joao['filhos'] = ['pedro', 'maria']
joao
joao['filhos'].append ('jorge')
joao
joao.clear()
joao
