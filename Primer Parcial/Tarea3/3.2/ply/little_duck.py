
# -----------------------------------------------------------------------------
# little_duck.py
#
# A home work for compilers... I have no idea what does this program do 
# -----------------------------------------------------------------------------

import ply.lex as lex           # Scanner, reconoce textos
import ply.yacc as yacc         # Parser, verifica que los textos estén correctamente ordenados (syntaxis)
import sys

# =================================================== SCANNER ===================================================

tokens = [
    'PROGRAM'               # program
    'INT',                  # cte_i
    'FLOAT',                # cte_f
    'NAME',                 # id
    'PLUS',                 # suma
    'MINUS',                # resta
    'DIVIDE',               # division
    'MULTIPLY',             # multiplicacion
    'EQUALS',               # igualacion
    'LESS_THAN',            # menor que
    'BIGGER_THAN',          # mayor que
    'EQUAL_THAN',           # igual que
    'OTHER_THAN'            # diferente que
    'IF',                   # condicional if
    'ELSE',                 # condicional else
    'STRING',               # cte.string
    'LEFT_PARENTHESIS',     # parentesis izquierdo
    'RIGHT_PARENTHESIS',    # parentesis derecho
    'LEFT_CURLY_BRACKET',   # llave izquierda
    'RIGHT_CURLY_BRACKET',  # llave derecha
    'PRINT'                # print
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_LESS_THAN = r'\<'
t_BIGGER_THAN = r'\>'
t_EQUAL_THAN = r'\=='
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_CURLY_BRACKET = r'\{'
t_RIGHT_CURLY_BRACKET = r'\}'

t_ignore = r' '

def t_PROGRAM(t):
    r'program'
    t.type = 'PROGRAM'
    return t

def t_FLOAT(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PRINT(t):
    r'print'
    t.type = 'PRINT'
    return t

def t_IF(t):
    r'if'
    t.type = 'IF'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t

def t_OTHER_THAN(t):
    r'<>'
    t.type = 'OTHER_THAN'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_STRING(t):
    r'"[a-zA-Z0-9_ ]*"'
    t.type = 'STRING'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("abc = 123.23")

while True:
    tok = lexer.token()
    if not tok:
        break;

    print(tok)
