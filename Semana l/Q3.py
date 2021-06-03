#5. (Atividade de Programação) Encontrando lexemas"
#Use a função find(sub, [ start [, end]]) que retorna o índice mais baixo na string onde a substring sub é encontrado dentro da fatia s[start:end]. Argumentos opcionais como start e end são interpretados como na notação de fatiamento. Retorna -1 se sub não for localizado.

def counting_lexemes(code, lexeme):
    res = 0
    codeList = code.split()
    for lex in codeList:
        if(lex.find(lexeme) != -1):
            res += 1
    return res

code = input()
lexeme = input()
print ( counting_lexemes(code, lexeme))
