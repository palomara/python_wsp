cores = {"vermelho":"red","azul": "blue","verde":"green","White":"branco"}
cor= input("escolha a cor que deseja traduzir: ").lower()
traducao = cores.get(cor, "esta cor nao consta no dicionario")
print (traducao)
