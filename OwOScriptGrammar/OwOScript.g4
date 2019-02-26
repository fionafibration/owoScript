grammar OwOScript;

/*
    This is the grammar for the OwOScript pseudocode,
    before it is compiled into OwO format.

    Parser rules
*/

script : definitions statements EOF;

statements : statement*;

definitions : definition*;

statement : expression ';'
          | ternary 
          | whileloop
          ;

expression : number
           | bignumber
           | command
           | functioncall
           ;

number : ('literal' | 'lit' | 'l') SINGLE_HEX_DIGIT;

bignumber : 'number' integer;

integer : NUMBER;

command : IDENTIFIER;

functioncall : IDENTIFIER '()';

definition : 'func' IDENTIFIER '{' statements '}';

ternary : 'if' '{' statements '}' 'else' '{' statements '}';

whileloop : 'while' '{' statements '}';

/*
    Lexer rules
 */

COMMENT : '/*' .*? '*/' -> skip;

LINE_COMMENT : '//' ~[\r\n]* -> skip;

HASH_COMMENT : '#' ~[\r\n]* -> skip;

WS : [ \n\t\r]+ -> channel(HIDDEN);

SINGLE_HEX_DIGIT : '0' .. '9'
                 | 'a' .. 'f'
                 | 'A' .. 'F'
                 ;

NUMBER : DECIMAL_INTEGER
       | EXPONENT_INTEGER
       ;

fragment DIGIT : [0-9];

fragment NON_ZERO_DIGIT : [1-9];

DECIMAL_INTEGER : ('+' | '-')? NON_ZERO_DIGIT DIGIT*
                | '0'+
                ;

fragment EXPONENT : [eE] DECIMAL_INTEGER;

fragment EXPONENT_INTEGER : DECIMAL_INTEGER EXPONENT;

fragment LETTER : [a-zA-Z];

IDENTIFIER : LETTER+;