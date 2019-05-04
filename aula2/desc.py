primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

print(primeiro,'-',segundo,'-',terceiro)

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if(segundo > primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro,'-',segundo,'-',terceiro)
