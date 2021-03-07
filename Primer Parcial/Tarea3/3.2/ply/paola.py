import ply.lex as lex
import ply.yacc as yacc
import os
import codecs
import re
import sys

#LEXER
tokens = [
    'INT',  #ya
    'FLOAT', #ya
    'IF', #ya
    'VAR',
    'ELSE', #ya
    'PRINT',
    'CTEI', #ya
    'CTEF', #ya
    'ID', #ya
    'PLUS', #ya
    'MINUS', #ya
    'DIVIDE', #ya
    'MULTIPLY', #ya
    'EQUALS', #ya
    'LPAREN', #ya
    'RPAREN', #ya
    'LBRACKET', #ya
    'RBRACKET', #ya
    'LT', #ya
    'GT', #ya
    'NE', #ya
    'COMMA', #ya
    'SEMI', #ya
    'COLON', #ya
    'STRING', #ya
    #'CHARACTER',
    'PROGRAM'
]

#REGULAR EXPRESSIONS
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LT = r'<'
t_GT = r'>'
t_NE = r'<>'
t_COMMA = r','
t_SEMI = r';'
t_COLON = r':'
t_STRING = r'([^\\\n]|(\\.))*?\"'
#t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''
t_ignore  = r' '

def t_PROGRAM(t):
    r'PROGRAM'
    t.value = 'PROGRAM'
    return t  
  
def t_PRINT(t):
    r'PRINT'
    t.value = 'PRINT'
    return t  

def t_INT(t):
    r'INT'
    t.value = 'INT'
    return t

def t_FLOAT(t):
    r'FLOAT'
    t.value = 'FLOAT'
    return t

def t_IF(t):
    r'IF'
    t.value = 'IF'
    return t

def t_ELSE(t):
    r'ELSE'
    t.value = 'ELSE'
    return t

def t_VAR(t):
    r'VAR'
    t.value = 'VAR'
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_]*'
    t.value = 'ID'
    return t

def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)

#build lexer
lexer = lex.lex()

lexer.input("PRINT")

# =================================================== PARSER  ===================================================
precedence = (
    # ('right', 'PROGRAM'),
    # ('right', 'PRINT'),
    # ('right', 'VAR'),
    # ('right', 'EQUALS'),
    # ('left', 'NE'),
    # ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY','DIVIDE'),
    # ('left', 'LPAREN', 'RPAREN'),
    # ('left', 'LBRACKET', 'RBRACKET')

)
#PROGRAMA===================================================
def p_programa(p):
    '''
    programa : PROGRAM ID SEMI varsp bloque
    '''
    p[0] = None
    
def p_varsp(p):
    '''
    varsp : vars
          | empty
    '''
    p[0] = None
#BLOQUE===================================================
def p_bloque(p):
    '''
    bloque : LBRACKET est RBRACKET
    '''

def p_est(p):
    '''
    est : estatuto est
        | empty
    '''
    p[0] = None
#EXPRESION===================================================
def p_expresion(p):
    '''
    expresion : exp expp
    '''
    p[0] = None
def p_expp(p):
    '''
    expp : LT exp
         | GT exp
         | NE exp
         | empty
    '''
    p[0] = None

#EXP===================================================
def p_exp(p):
    '''
    exp : termino te
    '''
    p[0] = None
    
def p_te(p):
    '''
    te : as termino
       | empty
    '''
    p[0] = None

def p_as(p):
    '''
    as : PLUS 
       | MINUS
    '''
    p[0] = None   
#TERMINO===================================================
def p_termino(p):
    '''
    termino : factor fa
    '''
    p[0] = None

def p_fa(p):
    '''
    fa : MULTIPLY factor
       | DIVIDE factor
       | empty
    '''
    p[0] = None

#CONDICION===================================================
def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN bloque condel SEMI
    '''
    p[0] = None

def p_condel(p):
    '''
    condel : ELSE bloque
          | empty
    '''
    p[0] = None

#FACTOR===================================================
def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | fafa
    '''
    p[0] = None

def p_fafa(p):
    '''
    fafa : as varcte
       | varcte
    '''
    p[0] = None

#ESTATUTO===================================================
def p_estatuto(p):
    '''
    estatuto : asignacion
             | condicion
             | escritura
    '''
    #p[0] = p[1]
    p[0] = None
#VARS===================================================
def p_vars(p):
    '''
    vars : VAR va
    '''
    p[0] = None

def p_va(p):
    '''
    va : ID COLON tipo SEMI vb
       | ID COMMA va 
    '''
    p[0] = None

def p_vb(p):
    '''
    vb : vars 
       | empty
    '''
    p[0] = None

#TIPO========================================================
def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''
    p[0] = None

#ASIGNACION===================================================
def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion SEMI
    '''
    p[0] = None

#ESCRITURA===================================================
def p_escritura(p):
    '''
    escritura : PRINT LPAREN op rest RPAREN
    '''
    p[0] = None

def p_op(p):
    '''
    op : expresion 
       | STRING
    '''
    p[0] = None

def p_rest(p):
    '''
    rest : COMMA
         | empty
    '''
    p[0] = None

#VARCTE===================================================
def p_VARCTE(p):
    '''
    varcte : ID
           | CTEI
           | CTEF
    '''
    p[0] = None

#OTHERS===================================================
def p_empty(p):
    '''
    empty :'''
    pass

# def p_error(p):
#     print("Syntax error")

parser = yacc.yacc()
env = {}

# def run(p):
# 	global env
# 	if type(p) == tuple:
# 		if p[0] == '+':
# 			return run(p[1]) + run(p[2])
# 		elif p[0] == '-':
# 			return run(p[1]) - run(p[2])
# 		elif p[0] == '*':
# 			return run(p[1]) * run(p[2])
# 		elif p[0] == '/':
# 			return run(p[1]) / run(p[2])
# 		elif p[0] == '=':
# 			env[p[1]] = run(p[2])
# 		elif p[0] == 'var':
# 			if p[1] not in env:
# 				return 'Undeclared viariable found!'
# 			else:
# 				return env[p[1]]
# 	else:
# 		return p

while True:
	try:
		s = input('>> ')
	
	except EOFError:
		break

	parser.parse(s)

