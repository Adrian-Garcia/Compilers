# ---------------------------------------------------------------------------------------------------------------
# little_duck programming language scanner and parser using ply
# ---------------------------------------------------------------------------------------------------------------

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

t_ignore  = ' \t\n'

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
  lexer.input('program primero : { print("hola") }')

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
def p_program(p) :
  '''
  program : PROGRAM ID SEMICOLON
          | PROGRAM ID COLON var bloque
  '''
  run(p[1])

def p_var(p):
  '''
  var : VAR var1
  '''
  p[0] = None

def p_var1(p):
  '''
  var1 : ID COMA var1
       | ID COLON INT SEMICOLON var1
       | ID COLON FLOAT SEMICOLON var1
       | empty
  '''
  p[0] = None

def p_bloque(p):
  '''
  bloque : LEFT_CURLY_BRACKET bloque1
  '''
  p[0] = None

def p_bloque1(p):
  '''
  bloque1 : estatuto bloque1
          | RIGHT_CURLY_BRACKET
  '''
  p[0] = None

def p_expresion(p):
  '''
  expresion : exp 
            | exp BIGGER_THAN exp
            | exp LESS_THAN exp
            | exp OTHER_THAN exp
            | exp SAME_AS exp
  '''
  p[0] = None

def p_exp(p):
  '''
  exp : termino
      | exp PLUS exp
      | exp MINUS exp
  '''
  p[0] = None

def p_termino(p):
  '''
  termino : factor
          | factor MULTIPLY factor
          | factor DIVIDE factor
  '''
  p[0] = None

def p_factor(p):
  '''
  factor : LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS
         | PLUS varcte
         | MINUS varcte
         | varcte
  '''
  p[0] = None

def p_estatuto(p):
  '''
  estatuto : asignatura
           | condicion
           | escritura
  '''
  p[0] = None

def p_condicion(p):
  '''
  condicion : IF LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS bloque SEMICOLON
            | IF LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS bloque ELSE bloque SEMICOLON
  '''
  p[0] = None

def p_asignatura(p):
  '''
  asignatura : ID EQUALS expresion SEMICOLON
  '''
  p[0] = None

def p_varcte(p):
  '''
  varcte : ID
         | INT
         | FLOAT
  '''
  p[0] = None

def p_escritura(p):
  '''
  escritura : PRINT RIGHT_PARENTHESIS escritura1
  '''
  p[0] = None

def p_escritura1(p):
  '''
  escritura1 : expresion escritura2
             | STRING escritura2
  '''
  p[0] = None

def p_escritura2(p):
  '''
  escritura2 : COMA escritura1
             | LEFT_PARENTHESIS SEMICOLON
  '''
  p[0] = None

def p_empty(p):
  '''
  empty :
  '''
  p[0] = None

parser = yacc.yacc()

def run(p):
    return p

def read(file_name):
  file = open(file_name)

  print("\nErrors on {}:".format(file_name))

  while True:

    line = file.readline()

    if (line):
      parser.parse(line)
    else: 
      break

read("test_that_works.txt")
read("test_that_does_not_work.txt")

