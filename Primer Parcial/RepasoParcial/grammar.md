PROG
	PROG	->	PROG ID ; V P B .

V
	V	->	VAR to_id : TIPO ; to_id
	to_id	->	ID , to_id | ID

P
	P	->	PROC ID ; V B ; P | #

B
	B	->	BEGIN to_s
	to_s	->	S ; to_s | END

S
	S	->	B | A
