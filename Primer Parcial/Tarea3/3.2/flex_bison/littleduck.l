%{
#include "littleduck.tab.h" 
#undef yywrap

%}
INT [0-9]*
FLOAT [0-9]*'.'[0-9]*
STRING \"([^\\"|^\\'])*\"
ID [A-Za-z]*|([A-Za-z0-9]*)
%%
program                             { printf("PROGRAM\n"); return PROGRAM; }
var                                 { printf("VAR\n"); return VAR; }
{INT}           	                { printf("INT\n"); return INT; }
{FLOAT}             	            { printf("FLOAT\n"); return FLOAT; }
{ID}                                { printf("ID\n"); return ID; }
if                                  { printf("IF\n"); return IF; }
else                                { printf("ELSE\n"); return ELSE; }
print                               { printf("PRINT\n"); return PRINT; }
"+"                                 { printf("PLUS\n"); return PLUS; }
"-"                                 { printf("MINUS\n"); return MINUS; }
"/"                                 { printf("DIVIDE\n"); return DIVIDE; }
"*"                                 { printf("MULTIPLY\n"); return MULTIPLY; }
"{"                                 { printf("LEFT_CURLY_BRACKET\n"); return LEFT_CURLY_BRACKET; }
"}"                                 { printf("RIGHT_CURLY_BRACKET\n"); return RIGHT_CURLY_BRACKET; }
"("                                 { printf("LEFT_PARENTHESIS\n"); return LEFT_PARENTHESIS; }
")"                                 { printf("RIGHT_PARENTHESIS\n"); return RIGHT_PARENTHESIS; }
"="                                 { printf("EQUALS\n"); return EQUALS; }
"<>"                                { printf("OTHER_THAN\n"); return OTHER_THAN; }
"<"                                 { printf("LESS_THAN\n"); return LESS_THAN; }
">"                                 { printf("BIGGER_THAN\n"); return BIGGER_THAN; }
","                                 { printf("COMA\n"); return COMA; }
";"                                 { printf("SEMICOLON\n"); return SEMICOLON; }
":"                                 { printf("COLON\n"); return COLON; }
{STRING}                            { printf("STRING\n"); return STRING; }
[ \n\t]                             { }
.                                   { printf("Mystery character %s\n", yytext);}
%%
