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
    'COLON',                # asignacion de variables
    'EQUALS',               # asignacion de ids
    'LESS_THAN',            # menor que
    'BIGGER_THAN',          # mayor que
    'SAME_AS',              # igual que
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
t_COLON = r'\:'
t_EQUALS = r'\='
t_OTHER_THAN = r'\<\>'
t_LESS_THAN = r'\<'
t_BIGGER_THAN = r'\>'
t_SAME_AS = r'\=\='
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
    lexer.input('program var b, a : 5; if (2<>3) { print ("program") } else { A = 1.2 }')

    while True:
        tok = lexer.token()
        if not tok:
            break;

        print(tok)

# test_lexer()

# =================================================== SCANNER ===================================================

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)

# PROGRAMA ------------------------------------------------------------------------------------------------------
# def p_little_duck(p):
#     '''
#     little_duck : program
#                 | empty
#     '''
#     print("start")
#     print(run(p[1]))

def p_program(p):
    '''
    program : PROGRAM ID COLON program bloque
            | empty
    '''
    print("program")

def p_program_block_var(p):
    '''
    program : vars
            | bloque
    '''

# VARS ----------------------------------------------------------------------------------------------------------
def p_vars(p):
    '''
    vars : VAR vars
    '''

def p_vars_for_id(p):
    '''
    vars : ID vars
    '''

def p_vars_coma(p):
    '''
    vars : COMA vars
    '''

def p_vars_colon(p):
    '''
    vars : COLON tipo SEMICOLON vars
    '''

def p_vars_var_end(p):
    '''
    vars : vars
         | bloque
    '''

# BLOQUE --------------------------------------------------------------------------------------------------------
def p_bloque(p):
    '''
    bloque : LEFT_CURLY_BRACKET bloque
    '''

def p_bloque_info(p):
    '''
    bloque : RIGHT_CURLY_BRACKET
           | estatuto bloque
    '''

# TIPO ----------------------------------------------------------------------------------------------------------
def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''

# ESTATUTO ------------------------------------------------------------------------------------------------------
def p_estatuto(p):
    '''
    estatuto : asignacion
             | condicion
             | escritura 
    '''

# ASIGNACION ------------------------------------------------------------------------------------------------------
def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion SEMICOLON
    '''

# CONDICION ------------------------------------------------------------------------------------------------------
def p_condicion(p):
    '''
    condicion : IF LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS bloque condicion
    '''

def p_condicion_cond_else(p):
    '''
    condicion : SEMICOLON
              | ELSE bloque SEMICOLON
    '''

# ESCRITURA ------------------------------------------------------------------------------------------------------
def p_escritura(p):
    '''
    escritura : PRINT LEFT_PARENTHESIS escritura RIGHT_PARENTHESIS SEMICOLON 
    '''

def p_escritura_exp_str(p):
    '''
    escritura : expresion
              | STRING
    '''

# EXPRESION ------------------------------------------------------------------------------------------------------
def p_expresion(p):
    '''
    expresion : exp expresion exp
    '''

def p_expresion_comparador(p):
    '''
    expresion : BIGGER_THAN
              | LESS_THAN
              | OTHER_THAN
    '''

# EXP ------------------------------------------------------------------------------------------------------
def p_exp(p):
    '''
    exp : termino exp
    '''

def p_exp_sum_sub(p):
    '''
    exp : PLUS
        | MINUS
    '''

# TERMINO ------------------------------------------------------------------------------------------------------
def p_termino(p):
    '''
    termino : factor termino
    '''

def p_termino_mult_div(p):
    '''
    termino : MULTIPLY
            | DIVIDE
    '''

# FACTOR ------------------------------------------------------------------------------------------------------
def p_factor(p):
    '''
    factor : factor
           | varcte
    '''

def p_factor_for_expr(p):
    '''
    factor : LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS
    '''

def p_factor_for_op(p):
    '''
    factor : PLUS varcte
           | MINUS varcte
    '''

# VARCTE ------------------------------------------------------------------------------------------------------
def p_varcte(p):
    '''
    varcte : ID
           | INT
           | FLOAT
    '''

def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

parser = yacc.yacc()
env = {}

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
        print(p)
        return p

while True:
    try:
        s = input('>> ')
    
    except EOFError:
        break

    parser.parse(s)
