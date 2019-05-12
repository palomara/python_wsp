Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> peso1 = float(input('Digite o peso da primeira prova'))
Digite o peso da primeira prova:
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    peso1 = float(input('Digite o peso da primeira prova'))
ValueError: could not convert string to float: ':'
>>> peso2 = float (input('Digite o peso da segunda prova'))
Digite o peso da segunda prova 6
>>> nota1 = float(input('Digite a nota da primeira prova: '))
Digite a nota da primeira prova: 5
>>> nota2= float(input('Digite a nota da segunda prova: '))
Digite a nota da segunda prova: 5
>>> peso1 = float(input('Digite o peso da primeira prova'))
Digite o peso da primeira prova
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    peso1 = float(input('Digite o peso da primeira prova'))
ValueError: could not convert string to float: 
>>> peso1 = float(input('Digite o peso da primeira prova: '))
Digite o peso da primeira prova: 5
>>> media = ((peso1*nota1) + (peso2*nota2)) / (peso1+peso2)
>>> print('A média do aluno é: , media)
      
SyntaxError: EOL while scanning string literal
>>> print ('A média do aluno é:',media)
A média do aluno é: 5.0
>>> input ('Aperte Enter para sair')
Aperte Enter para sair
''
>>> txt = (input ('Bom Dia'))

Bom Dia
>>> nome = (input('Digite o nome',txt))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    nome = (input('Digite o nome',txt))
TypeError: input expected at most 1 arguments, got 2
>>> nome = (input('Digite o nome'))
Digite o nome Guilherme
>>> txt = (input('Bom dia',nome))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    txt = (input('Bom dia',nome))
TypeError: input expected at most 1 arguments, got 2
>>> txt = (input('Bom dia'))
Bom dia
>>> print ('Bom dia',nome))
SyntaxError: invalid syntax
>>> 
>>> nome = str (input('Digite seu nome: '))
Digite seu nome: guilherme
>>> print ('Bom dia',nome)
Bom dia guilherme
>>> nome = str (input('Digite seu nome: '))
Digite seu nome: Guilherme
>>> nome = str (input('Digite seu nome: '))
Digite seu nome: João
>>> nome = str (input('Digite seu nome: '))

Digite seu nome: Maria
>>> 
KeyboardInterrupt
>>> nome = str (input('Digite seu nome: '))
nome = str (input('Digite seu nome: '))
nome = str (input('Digite seu nome: '))

SyntaxError: multiple statements found while compiling a single statement
>>> 
===================== RESTART: D:/Python/Bom-Dia+Nome.py =====================
Digite seu nome: Guilherme
Bom dia Guilherme
>>> 
==================== RESTART: D:/Python/nome-3-pessoas.py ====================
Digite seu nome: 
==================== RESTART: D:/Python/nome-3-pessoas.py ====================
Digite seu nome: 
