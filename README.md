# owoScript

owoScript is a stack based, imperative, and Turing complete programming language. 
owoScript works with a simple and descriptive language 
that is then compiled to the best bytecode to ever exist on this planet.

Why is owoScript bytecode the best on the planet? Because it's entirely made out of 
OwO faces! Why have the speed and portability of the JVM when you can have the most *adorable* 
code out of almost any language you can write in? And never fear, your owoScript bytecode can easily be turned
back into the higher level form at any time.

Additionally, owoScript leaves its syntax and parsing files easily accessible to be inspected and verified by 
anyone. owoScript's grammar is written in ANTLR4, a parsing tool so out of this world reliable and efficient that 
you'll wonder why your favorite programming language isn't using it yet.

### Examples
See the `/examples` directory for a hello world, truth machine, and a proof of turing completeness via 
brainfuck equivalents (does your fancy OOP language prove that it is capable of universal computation? 
Can you trust it if it doesn't?)

### Usage

##### Stack

owoScript is written in a descriptive language consisting of stack operations, number literals, 
`while` loops, and `if {} else {}` statements.
Whitespace is ignored. 

owoScript is stack-based, with only integer types. For example, 
the following literal will push `6` onto the stack:
```
literal 6;
```
and the following command will take that number off the stack and print it:
```
printnum;
```
operations take their values off the stack in the order they came onto it:
```
literal 8;
literal 2;
div;
```
corresponds to 8 / 2, not 2 / 8. However, in addition to the stack, an optional "hashmap", 
mapping integer keys to integer values, is available through the `store` and `get` commands

##### Arithmetic 

Because owoScript is stack-based, arithmetic is performed in postfix notation.
This means that writing something like (2+3)*(5/7)
is written by taking the operator out of the middle of the expression and adding it on to the end.
So 2+3 is written as `literal 2; literal 3; add;` and 5/7 is written as `literal 5; literal 7; div;`

The final expression would thus be written as:

```
literal 2;
literal 3;
add;
literal 5;
literal 7;
div;
mult;
```

##### Flow control

Flow control is provided in `while` loops, functions, and `if {} else {}` statements

While loops simply repeat the operation inside them until the top of the stack is 0, or falsy.
They do not pop values, and instead simply inspect the stack without changing it. While loops are skipped
if the top of the stack is 0 when they are made.

Example: 
```
// Truth machine
// When a truthy number is inputted, continue printing it forever
// Otherwise print once and stop
inputnum;
dupe;
printnum;
while {
    dupe;
    printnum;
}
```

Functions are defined at the top of the file and called like so, 
and can call other functions. Putting a function anywhere other than 
at the top of the file will result in very undefined behavior.
Functions do not take argument, and simply operate off of the stack.
```
func square {
    dupe;
    mult;
}
literal 3;
square();
```

If statements have the syntax 
```
if {
    // statements or nop;
}
else {
    // statements or nop;
}
```
and pop the top value of the stack. If it is truthy, the first block is executed. Otherwise,
the second one is.


##### Commands

Commands are single word operations (except for number literals and bignumber literals, see below)

| Keyword    | Pops | Pushes                                                     |
|------------|------|------------------------------------------------------------|
| literal x  | None | hex value of x, x must be single hex digit (0-9, a-f)      |
| number x   | None | int value of x, x is signed number [*]                     |
| add        | a, b | a + b                                                      |
| sub        | a, b | a - b                                                      |
| mult       | a, b | a * b                                                      |
| div        | a, b | a // b (floor division)                                    |
| mod        | a, b | a % b (modulus)                                            |
| exp        | a, b | a ^ b (exponent)                                           |
| print      | a    | prints the character with code *a*                         |
| printnum   | a    | prints the number literally                                |
| printstack | None | prints entire stack                                        |
| input      | None | number of character read from stdin                        |
| inputnum   | None | decimal number read from stdin                             |
| lt         | a, b | 1 if a < b else 0                                          |
| gt         | a, b | 1 if a > b else 0                                          |
| eq         | a, b | 1 if a == b else 0                                         |
| neq        | a, b | 1 if a != b else 0                                         |
| cmp        | a, b | if a == b: 0, if a > b: 1, if a < b: -1                    |
| dupe       | a    | a, a (a repeated)                                          |
| dupedeep   | a    | extend stack with last a values on stack                   |
| swap       | a, b | b, a (top two values swapped)                              |
| push       | a, b | puts a *b* layers deep in the stack                        |
| fetch      | a    | pulls the number *a* deep in the stack to the top          |
| stacklength| None | length of stack                                            |
| store      | a, b | stores b in the *a* slot in the hashmap                    |
| get        | a    | pushes the value stored in *a* slot in the hashmap         |
| stop       | a    | exits with return code a                                   |
| fetchdupe  | a, b | same as fetch but doesn't remove number from inside stack  |
| pushdupe   | a    | same as push but doesn't remove number from top of stack   |
| nop        | None | no operation, used for code clarity in if/else statements  |
| hexmult    | a, b | a * 16 + b (hexadecimal digit appending)                   |
| printhash  | None | prints entire hashmap                                      |

\* these number literals will be less space efficient in OwO form, so if your 
number is representable by a single hex digit, that form is recommended.

##### CLI Usage

The python script `owo.py` is used for running owoScript bytecode or psuedocode, while the python
script `owoc.py` is the compiler/decompiler used to transform code from pseudocode or bytecode.

The script `bfowo.py` is used to convert brainfuck programs into owoscript. This conversion is moderately optimized, 
but is still less efficient than really writing in owoscript would be. 

A command line option can be used to specify whether you'd like the transpiler to "wrap" the brainfuck cells 
(like an 8-bit unsigned int) or whether you'd like python-style ints.

See `sierpinski_bf.owop` and `mandelbrot_bf.owop` for examples of these conversions.

### Turing completeness
owoScript is provably Turing complete, via a simple reduction to brainfuck

```/*

Brainfuck equivalents for OwOScript

Stack is used to hold current pointer while hashmap is used for cells

*/


// > Move pointer right
literal 1;
add;

// < Move pointer left
literal 1;
sub;

// + Increment cell
dupe;
dupe;
get;
literal 1;
add;

/*
Mod 256 wrapping if desired
literal 1;
literal 0;
hexmult;
literal 0;
hexmult;
mod;
*/

store;

// - Decrement cell
dupe;
dupe;
get;
literal 1;
sub;

/*
Mod 256 wrapping if desired
literal 1;
literal 0;
hexmult;
literal 0;
hexmult;
mod;
*/

store;

// . Output char
dupe;
get;
print;

// , Input char
dupe;
input;
store;

// [ ] Begin and end while loop
dupe;
get;
while {
    discard;
    //statements
    dupe;
    get;
}
discard;
```

### Why

"The only reason someone would do something like this if they could, which they can't, would be because they could, which they can't." - Rick Sanchez

I'm sure the question everyone is thinking is "why." Why make a programming language entirely in OwO faces? 
Why go out of my way to implement a formal grammar with a parser for a meme? 

The simple answer, of course, is because 
I hate myself. The more accurate answer is because I wanted to try out writing a basic interpreter and grammar in
ANTLR, in preparation for possibly writing an LLVM compiler for a few esoteric programming languages in the near future

### Credits
I dedicate this project to all of my friends who answer the phone with "hewwo" so often I want to bash my head in.

### Final Note
This project is mostly a joke I embarked on as a fun way of learning parsing and the basics of imperative language design. Any ridiculous statements inside this project are purely satire.
