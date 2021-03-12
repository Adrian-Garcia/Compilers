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
program: PROGRAM ID SEMICOLON | PROGRAM ID SEMICOLON var bloque;

var: VAR var1;

var1: ID COMA var1 | ID COLON INT SEMICOLON var1 | ID COLON FLOAT SEMICOLON var1 |;

bloque: LEFT_CURLY_BRACKET bloque1;

bloque1: estatuto bloque1 | RIGHT_CURLY_BRACKET;

expresion: exp | exp BIGGER_THAN exp | exp LESS_THAN exp | exp OTHER_THAN exp;

exp: termino | termino PLUS exp | termino MINUS exp;

termino: factor | factor MULTIPLY termino | factor DIVIDE termino;

factor: LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS | PLUS varcte | MINUS varcte | varcte;

estatuto: asignatura | condicion | escritura;

condicion: IF LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS bloque SEMICOLON | IF LEFT_PARENTHESIS expresion RIGHT_PARENTHESIS bloque ELSE bloque SEMICOLON;

asignatura: ID EQUALS expresion SEMICOLON;

varcte: ID | INT | FLOAT;
 
escritura: PRINT LEFT_PARENTHESIS escritura1;

escritura1: expresion escritura2 | STRING escritura2;

escritura2: COMA escritura1 | RIGHT_PARENTHESIS SEMICOLON;

%%

int main (int argc, char **argv){
    yyparse();
}

int yyerror(char *s){
    fprintf(stderr, "error: %s\n", s);
    return 0;
}