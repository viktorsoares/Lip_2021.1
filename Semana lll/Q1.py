#2.(Atividade de Programação) Análise Léxica usando Expressão Regular

from typing import NamedTuple
import sys
import re

"""
class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int
"""
Token = NamedTuple('Token', [('type', str), ('value', str), ('line', int), ('column', int)])
    
     
def tokenize(code):
    # palavras-chaves da linguagem analisada
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    # lista com o identificador do token e a expressão regular que descreve o token    
    token_specification = [
        # Observe que a especificação do token NUMBER aceita números inteiros e decimais
        # Os números decimais descritos a parte inteira é obrigatória 
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r'='),           # Assignment operator
        ('AP', r'[(]'),
        ('AC', r'[{]'),
        ('COMMA', r'[,]'),
        ('LEFTBRACKET', r'[[]'),
        ('RIGHTBRACKET', r'[]]'),
        ('for', r'for'),
        ('LT', r'[<]'),
        ('FP', r'[)]'),
        ('FC', r'[}]'),
        ('if', r'if'),
        ('return', r'return'),
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        #('MISMATCH', r'.'),            # Any other character
    ]
    
    # Com esse comando construímos uma expressão regular com todos os tokens da linguagem
    # Por exemplo,
    # tok_regex = (?P<NUMBER>\d+(\.\d*)|(?P<ID>[A-Za-z]+))
    # É uma expressão regular que descreve os tokens NUMBER e ID


    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    # A função finditer(tok_regex, code) devolve um iterador de match objects
    # Os atributos e métodos de match object mo utilizados são: 
    # * mo.lastgroup devolve o nome do último match capturado
    # * mo.group() devolve o último match encontrado
    # * mo.start() devolve o indice do inicio da substring casada pelo group
    

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = str(value) if '.' in value else str(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            # Cada vez que o caractere \n é encontrado o numero de linhas é incrementado            
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        #elif kind == 'MISMATCH':
           # raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

data = sys.stdin.readlines(200)

code = ''.join(data)

for token in tokenize(code):
    print(token)