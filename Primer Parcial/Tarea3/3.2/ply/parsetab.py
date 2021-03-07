
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEDIVIDE EQUALS FLOAT INT MINUS MULTIPLY NAME PLUS\n\tlittle_duck : expression\n\t\t \t\t| var_assign\n\t\t \t\t| empty\n\t\n\tvar_assign : NAME EQUALS expression\n\t\n\texpression : expression MULTIPLY expression\n\t\t\t   | expression DIVIDE expression\n\t\t\t   | expression PLUS expression\n\t\t\t   | expression MINUS expression\n\t\n\texpression : INT\n\t\t\t   | FLOAT\n\t\n\texpression : NAME\n\t\n\tempty :\n\t'
    
_lr_action_items = {'INT':([0,8,9,10,11,12,],[5,5,5,5,5,5,]),'FLOAT':([0,8,9,10,11,12,],[6,6,6,6,6,6,]),'NAME':([0,8,9,10,11,12,],[7,14,14,14,14,14,]),'$end':([0,1,2,3,4,5,6,7,13,14,15,16,17,18,],[-12,0,-1,-2,-3,-9,-10,-11,-5,-11,-6,-7,-8,-4,]),'MULTIPLY':([2,5,6,7,13,14,15,16,17,18,],[8,-9,-10,-11,-5,-11,-6,8,8,8,]),'DIVIDE':([2,5,6,7,13,14,15,16,17,18,],[9,-9,-10,-11,-5,-11,-6,9,9,9,]),'PLUS':([2,5,6,7,13,14,15,16,17,18,],[10,-9,-10,-11,-5,-11,-6,-7,-8,10,]),'MINUS':([2,5,6,7,13,14,15,16,17,18,],[11,-9,-10,-11,-5,-11,-6,-7,-8,11,]),'EQUALS':([7,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'little_duck':([0,],[1,]),'expression':([0,8,9,10,11,12,],[2,13,15,16,17,18,]),'var_assign':([0,],[3,]),'empty':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> little_duck","S'",1,None,None,None),
  ('little_duck -> expression','little_duck',1,'p_little_duck','calc.py',57),
  ('little_duck -> var_assign','little_duck',1,'p_little_duck','calc.py',58),
  ('little_duck -> empty','little_duck',1,'p_little_duck','calc.py',59),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','calc.py',65),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','calc.py',72),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','calc.py',73),
  ('expression -> expression PLUS expression','expression',3,'p_expression','calc.py',74),
  ('expression -> expression MINUS expression','expression',3,'p_expression','calc.py',75),
  ('expression -> INT','expression',1,'p_expression_int_float','calc.py',81),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','calc.py',82),
  ('expression -> NAME','expression',1,'p_expression_var','calc.py',88),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',97),
]
