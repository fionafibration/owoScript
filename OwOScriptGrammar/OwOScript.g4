grammar OwOScript;

/*
    This is the grammar for the OwOScript pseudocode,
    before it is compiled into OwO format. 
 */

/* 
    Parser rules
*/

script : statements EOF;

statements : statement*;

statement : expression ';' 
          | ternary 
          | whileloop
          ;

expression : number
           | command
           | '(' expression ')'
           ;

number : ('literal' | 'lit' | 'l') SINGLE_DIGIT;

command : IDENTIFIER;

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

SINGLE_DIGIT : '0' .. '9' 
             | 'a' .. 'f' 
             | 'A' .. 'F'
             ;

fragment LETTER : 'a' .. 'z' 
                | 'A' .. 'Z'
                ;

IDENTIFIER : LETTER+;