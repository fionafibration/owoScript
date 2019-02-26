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

bignumber :  'number' integer;

integer : ('+' | '-')? NUMBER;

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

fragment SEMICOLON : ';';

SINGLE_HEX_DIGIT : '0' .. '9'
                 | 'a' .. 'f'
                 | 'A' .. 'F'
                 ;

NUMBER : ('0' .. '9') + (('e' | 'E') NUMBER)*;

LETTER : 'a' .. 'z'
       | 'A' .. 'Z'
       ;

IDENTIFIER : LETTER+;