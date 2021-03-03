# Tarea 3.1
A continuación se describe un pequeño lenguaje de programación. Se te pide que implementes 2 versiones de los analizadores de léxico y sintaxis (scanner y parser) necesarios para reconocerlo. Debes utilizar la herramienta que planeas usar para tu proyecto. El programa a ejecutar leerá los elementos de un archivo fuente (texto), revisará el léxico y la sintaxis y, en caso de existir error, desplegará en pantalla el mensaje “apropiado”.

##### LENGUAJE: LittleDuck 2020

A continuación se describen las reglas sintácticas del lenguaje LittleDuck 2020. Considerando los tokens que se usan dentro de estas reglas, diseña las reglas de los elementos de léxico (tokens) que sean necesarias (a tu criterio). Considera que esta tarea te dará la pauta para desarrollar las etapas de léxico y sintaxis de tu proyecto.

*Entregar las expresiones regulares y la gramática en un documento.*

## LittleDuck 2020
![LittleDuck](./LittleDuck.png)

----------------------------------------------------------------

## Expresiones regulares

|         Token          |     Expresion     |
|------------------------|:-----------------:|
| inicio de programa     | program           |
| letras                 | [a-z], [A-Z]      |
| numero                 | [0-9]             |
| id                     | letra* numero*    |
| var                    | letra* numero*    |
| parentsis izquierdo    | (                 |
| parentsis derecho      | )                 |
| llave curva izquierda  | {                 |
| llave curva derecha    | }                 |
| igual a                | =                 |
| mayor a                | >                 |
| menor a                | <                 |
| diferente a            | <>                |
| suma                   | +                 |
| resta                  | -                 |
| multiplicacion         | *                 |
| division               | /                 |
| print                  | print             |
| condicional if         | if                |
| condicional else       | else              |
| cte string             | "letra*"          |
| cte entera             | numero*           |
| cte flotante           | numero* .numero*  |

## Gramatica

#### PROGRAMA
    programa    ->      id 
    id          ->      ;
    ;           ->      Vars | Bloque | ε
    Vars        ->      Bloque
    Bloque      ->      ε

#### VARS
    Var         ->      id
    id          ->      . | ;
    .           ->      id
    ;           ->      Tipo
    Tipo        ->      ;
    ;           ->      id | ε

#### BLOQUE
    Bloque      ->      {
    {           ->      Estatuto | }
    Estatuto    ->      } | {
    }           ->      }

### TIPO
    int         ->      ε
    float       ->      ε

#### ESTATUTO
    Estatuto    ->      Asignacion | Condicion | Estritura
    Asignacion  ->      ε
    Condicion   ->      ε
    Estritura   ->      ε

#### ASIGNACION
    Asignacion  ->      id
    id          ->      =
    =           ->      Expresion
    Expresion   ->      ;
    ;           ->      ε

#### CONDICION
    if          ->      (
    (           ->      Expresion
    Expresion   ->      )
    )           ->      Bloque
    Bloque      ->      else | ;
    else        ->      Bloque'
    Bloque'     ->      ;

#### ESCRITURA
    print       ->      (
    (           ->      cte.string | Expresion
    cte.string  ->      ) | .
    Expresion   ->      . | )
    .           ->      Expresion | cte.string
    )           ->      ;
    ;           ->      ε

#### EXPRESION
    Exp         ->      > | < | <> | ε
    >           ->      Exp
    <           ->      Exp
    <>          ->      Exp

#### EXP
    Termino     ->      + | - | ε
    +           ->      Termino
    -           ->      Termino

#### TERMINO
    Factor      ->      / | * | ε
    /           ->      Factor
    *           ->      Factor

#### FACTOR
    (           ->      Expresion
    +           ->      Var Cte
    -           ->      Var Cte
    Var Cte     ->      ε
    Expresion   ->      )
    )           ->      ε

### VAR CTE
    id          ->      ε
    cte i       ->      ε
    cte f       ->      ε
