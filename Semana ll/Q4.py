'''Faça um programa que recebe um código de um programa e devolve todas as constante ponto flutuante contidas no seu programa.

Uma constante ponto-flutuante consiste em uma palavra com:

Um sinal de + ou - opcional
Uma string de dígitos
Um ponto decimal
Uma outra string de dígitos. Essa outra string de dígitos ou a primeira string de dígitos (2) podem ser vazias, mas não ambas.'''

import re

code = input()
## Coloque aqui usa expressão regular
pattern = r'[+-]?([0-9]+\.([0-9]*)?|[.][0-9]+)'

for s in code.split():
  if re.fullmatch(pattern, s) :
    print(s) 