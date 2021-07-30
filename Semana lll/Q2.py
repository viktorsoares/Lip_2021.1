#4. (Atividade de Programação) Analisador Léxico usando diagrama de estados

import sys
import re

class Token():
  def __init__(self,type, value, line):
    self.type = type
    self.value = value
    self.line = line
    
  def __str__(self):
    return "Token(type='%s', value='%s', line=%d)" % (self.type, self.value,self.line) 

pos = 0
token_atual = ""
proximoCaracter = ' '
line_num = 0

def pegaCaracter():

  global pos  
  global proximoCaracter
  if pos == len(code):
    proximoCaracter = '$'  
  else:
    proximoCaracter = code[pos] 
  pos = pos + 1

  
def acrescentaCaracter():
  global token_atual  
  token_atual = token_atual + proximoCaracter
     

def get_token():  
  global token_atual  
  global pos  
  global line_num
  kind = ''
  value = ''
  pattern = r'\d+(\.\d*)?'
     
  keywords = {'if', 'THEN', 'ENDIF', 'for', 'NEXT', 'GOSUB', 'return'}

  pegaCaracter()
  while proximoCaracter == '' or proximoCaracter == '\n' or proximoCaracter == '\t' or proximoCaracter == ' ' :
    if proximoCaracter == '\n':
      line_num = line_num + 1
    pegaCaracter()  
  
  if proximoCaracter == '=':      
    acrescentaCaracter()      
    kind = 'ASSIGN'
    value = token_atual

  elif proximoCaracter == '(':
    acrescentaCaracter()      
    kind = '('
    value = token_atual
  
  elif proximoCaracter == ')':
    acrescentaCaracter()      
    kind = ')'
    value = token_atual
  
  elif proximoCaracter == '{':
    acrescentaCaracter()      
    kind = '{'
    value = token_atual

  elif proximoCaracter == '}':
    acrescentaCaracter()      
    kind = '}'
    value = token_atual
  
  elif proximoCaracter == '[':
    acrescentaCaracter()      
    kind = '['
    value = token_atual
  
  elif proximoCaracter == ']':
    acrescentaCaracter()      
    kind = ']'
    value = token_atual

  elif proximoCaracter == '+':
    acrescentaCaracter()
    kind = 'OP'
    value = token_atual
  elif proximoCaracter == '*':
    acrescentaCaracter()
    kind = 'OP'
    value = token_atual
  elif proximoCaracter == ';':
    acrescentaCaracter()
    kind = 'END'
    value = token_atual
  elif proximoCaracter == '$':
    kind = 'EOF'
    value = token_atual
  else :
    acrescentaCaracter()
    pegaCaracter()
    while proximoCaracter.isalpha() or proximoCaracter.isdigit():
      acrescentaCaracter()
      pegaCaracter()
    pos = pos - 1    
    if token_atual in keywords:
      kind = token_atual
      value = token_atual
    elif (re.fullmatch(pattern, token_atual)):
      kind = 'INT'
      value = token_atual
    else:
      kind = 'ID'
      value = token_atual  

  token_atual = ""  
  return Token(kind, value, line_num)  


data = sys.stdin.readlines()

code = ''.join(data)

token = get_token()
while  token.type != 'EOF':
  print(token)
  token = get_token()