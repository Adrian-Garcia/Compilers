%{
#include <stdio.h>

int yylex();
int yyerror();

%}
%token PROGRAM VAR INT FLOAT IF ELSE PRINT 
%token LEFT_CURLY_BRACKET RIGHT_CURLY_BRACKET LEFT_PARENTHESIS RIGHT_PARENTHESIS
%token PLUS MINUS MULTIPLY DIVIDE EQUALS OTHER_THAN LESS_THAN BIGGER_THAN
%token COMA SEMICOLON COLON 
%token STRING 
%token ID

%%
little_duck: program;

program: PROGRAM ID COLON block_var;

block_var: vars | bloque;

vars: VAR for_id;

for_id: ID coma | ID colon;

coma: COMA for_id;

colon: COLON tipo SEMICOLON var_end;

var_end: for_id | bloque;

bloque: LEFT_CURLY_BRACKET info RIGHT_CURLY_BRACKET;

info: estatuto info |;

tipo: INT | FLOAT;

estatuto: asignacion | condicion | escritura;

asignacion: ID EQUALS expresion SEMICOLON;

condicion: IF LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS bloque cond_else SEMICOLON;

cond_else: ELSE bloque | ;

escritura: PRINT LEFT_PARENTHESIS expr_str RIGHT_PARENTHESIS SEMICOLON;

expr_str: expresion COMA | STRING COMA | expresion | STRING;

expresion: exp comparador;

comparador: BIGGER_THAN exp | LESS_THAN exp | OTHER_THAN exp | SAME_AS exp |;

exp: termino sum_sub;

sum_sub: PLUS | MINUS;

termino: factor mult_div;

mult_div: MULTIPLY | DIVIDE;

factor: for_expr | for_op | varcte;

for_expr: LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS;

for_op: PLUS varcte | MINUS varcte;

varcte : ID | INT | FLOAT;

%%

int main (int argc, char **argv){
    yyparse();
}

int yyerror(char *s){
    fprintf(stderr, "error: %s\n", s);
    return 0;
}