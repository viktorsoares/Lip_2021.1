'''Hexadecimal
Faça um programa que lê uma linha formada por várias strings e verifica se cada uma das strings corresponde a constante hexadecimal. 
Um constante hexadecimal começa com 0, seguido de x ou X, seguido dos dígitos de 0 até 9 ou os caracteres de a até f, maiúsculos ou minúsculos.'''

import re


## Coloque aqui usa expressão regular
#regexp = r'[xX][0-9a-fA-F]+'

regexp = r'(?:0[xX])?[0-9a-fA-F]+'

for string in input().split(' '):
  print( re.fullmatch(regexp, string) != None)