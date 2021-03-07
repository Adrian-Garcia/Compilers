# LittleDuck 2020
## Expresiones
- id: [A-Za-z]+([A-Za-z] | [0-9])*

## Gramática
-   PROGRAMA  
```
PROGRAMA -> program id ; VARIABLE' BLOQUE  
VARIABLE' -> VARS | vacío  
```
-   BLOQUE  
```
BLOQUE -> { BLOQUE' }  
BLOQUE' -> ESTATUTO | vacío  
```
-   EXPRESION  
```
EXPRESION -> EXP EXPRESION'  
EXPRESION' -> SIGNOS EXP | vacío  
SIGNOS -> > | < | <>  
```
-   EXP  
```
EXP -> TERMINO EXP'  
EXP' -> + | - | vacío  
```
-   VARS
```
VARS -> var DEF  
DEF -> DEFINICION DEF'  
DEF' -> DEF | vacío  
DEFINICION -> DEFID : TIPO ;  
DEFID -> id DEFID'  
DEFID' -> , DEFID | vacío  
```
-   ESTATUTO  
```
ESTATUTO -> ASIGNACION | CONDICION |   ESCRITURA  
```
-   TIPO
```
TIPO -> int | float  
```  
-   ASIGNACION  
```
ASIGNACIÓN -> id = EXPRESION ;  
```
-   ESCRITURA  
```
ESCRITURA -> print ( TEXTO ) ;  
TEXTO -> POSTEXTOS TEXTO'  
TEXTO' -> TEXTO | vacío  
POSTEXTOS -> cte.string | EXPRESION   
```
-   CONDICION  
```
CONDICION -> if ( EXPRESION ) BLOQUE CONDICION' ;  
CONDICION' -> else BLOQUE | vacío  
```
-   TERMINO  
```
TERMINO -> FACTOR TERMINO'  
TERMINO' -> * | / | vacío  
```
-   FACTOR  
```
FACTOR -> FACTOREXP | FACTORVAR  
FACTOREXP -> ( EXPRESION )  
FACTORVAR -> FACTORVAR' VAR CTE  
FACTORVAR' -> + | -  
```
-   VAR CTE
```
VAR CTE -> id | cte l | cte f  
```  