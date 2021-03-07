# -----------------------------------------------------------------------------
# little_duck programming language scanner and parser using ply
# -----------------------------------------------------------------------------

import ply.lex as lex           # Scanner, reconoce textos
import ply.yacc as yacc         # Parser, verifica que los textos estén correctamente ordenados (syntaxis)
import sys

# =================================================== SCANNER ===================================================

tokens = [
    'PROGRAM',              # program
    'VAR',                  # var
    'FLOAT',                # cte_f
    'INT',                  # cte_i
    'ID',                   # id
    'PLUS',                 # suma
    'MINUS',                # resta
    'DIVIDE',               # division
    'MULTIPLY',             # multiplicacion
    'EQUALS',               # igualacion
    'LESS_THAN',            # menor que
    'BIGGER_THAN',          # mayor que
    'EQUAL_THAN',           # igual que
    'OTHER_THAN',           # diferente que
    'IF',                   # condicional if
    'ELSE',                 # condicional else
    'STRING',               # cte.string
    'LEFT_PARENTHESIS',     # parentesis izquierdo
    'RIGHT_PARENTHESIS',    # parentesis derecho
    'LEFT_CURLY_BRACKET',   # llave izquierda
    'RIGHT_CURLY_BRACKET',  # llave derecha
    'PRINT',                # print
    'COMA',                 # ,
    'SEMICOLON'             # ;
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\:'
t_OTHER_THAN = r'\<\>'
t_LESS_THAN = r'\<'
t_BIGGER_THAN = r'\>'
t_EQUAL_THAN = r'\=\='
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_CURLY_BRACKET = r'\{'
t_RIGHT_CURLY_BRACKET = r'\}'
t_COMA = r'\,'
t_SEMICOLON = r'\;'

t_ignore  = ' \t'

def t_PROGRAM(t):
    r'program'
    t.type = 'PROGRAM'
    return t

def t_VAR(t):
    r'var'
    t.type = 'VAR'
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

def t_STRING(t):
    r'"[a-zA-Z0-9!@#$%^&*()]*"'
    t.type = 'STRING'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# This function is only for coding, call it at the end of the file for testing if you want
def test_lexer():
    lexer.input('program var b, a : 5; if (2<>3) { print ("program") } else { print (1.2) }')

    while True:
        tok = lexer.token()
        if not tok:
            break;

        print(tok)

test_lexer()

# =================================================== SCANNER ===================================================

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)

# PROGRAMA ------------------------------------------------------------------------------------------------------
def p_little_duck(p):
    '''
    little_duck : program
                | empty
    '''
    print(p[1])

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON program bloque
    '''
    p[0] = ()

def p_program_variable(p):
    '''
    program : vars
            | empty
    '''

# VARS ----------------------------------------------------------------------------------------------------------
def p_vars(p):
    '''
    vars : VAR vars
    '''

def p_vars_definicion(p):
    '''

    '''

# BLOQUE --------------------------------------------------------------------------------------------------------
def p_bloque(p):
    '''
    bloque : LEFT_CURLY_BRACKET bloque RIGHT_CURLY_BRACKET
    '''

def p_bloque_estatuto(p):
    '''
    bloque : estatuto
           | empty
    '''

# TIPO ----------------------------------------------------------------------------------------------------------

# ESTATUTO ------------------------------------------------------------------------------------------------------
def estatuto(p):
    '''
    estatuto : asignacion
             | condicion
             | escritura 
    '''

def p_expresion():
    pass

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# parser = yacc.yacc()
# env = {}

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared viariable found!'
            else:
                return env[p[1]]

    else:
        return p

# while True:
#     try:
#         s = input('>> ')
    
#     except EOFError:
#         break

#     parser.parse(s)
