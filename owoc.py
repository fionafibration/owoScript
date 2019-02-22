from OwOScriptGrammar.OwOScriptVisitor import OwOScriptVisitor
from OwOScriptGrammar.OwOScriptParser import OwOScriptParser
from OwOScriptGrammar.OwOScriptLexer import OwOScriptLexer
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


import random
import itertools
import owoi
import sys


class OwOErrorListener(ErrorListener):
    def syntaxError(self, recognizer, symbol, line, col, msg, e):
        print('Syntax error at line %s char %s:\n%s\n' % (line, col, msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


OWO_CHARSET = 'oOuUnNxXcC~^*-<>'

COMMAND_LIST = [
        'literal 0;',
        'literal 1;',
        'literal 2;',
        'literal 3;',
        'literal 4;',
        'literal 5;',
        'literal 6;',
        'literal 7;',
        'literal 8;',
        'literal 9;',
        'literal a;',
        'literal b;',
        'literal c;',
        'literal d;',
        'literal e;',
        'literal f;',
        'if {',
        '} else {',
        'while {',
        '}',
        'add;',
        'sub;',
        'mult;',
        'div;',
        'mod;',
        'exp;',
        'print;',
        'printnum;',
        'printstack;',
        'input;',
        'inputnum;',
        'lt;',
        'gt;',
        'eq;',
        'neq;',
        'cmp;',
        'dupe;',
        'discard;',
        'swap;',
        'push;',
        'fetch;',
        'store;',
        'get;',
        'stop;',
        'pushdupe;',
        'fetchdupe;',
        'nop;'
    ]

COMMAND_LIST_INVERTED = dict({command: number for number, command in enumerate(COMMAND_LIST)})


def num_to_owo(number):
    if number < 0 or number > 255:
        raise ValueError('Invalid OwO number!')
    a, b = number // 16, number % 16
    first_eye, second_eye = OWO_CHARSET[a], OWO_CHARSET[b]

    return '%sw%s %sw%s' % (first_eye, first_eye, second_eye, second_eye)


def owo_pair_to_num(first_owo, second_owo):
    first_eye, second_eye = first_owo[0], second_owo[0]
    a, b = OWO_CHARSET.find(first_eye), OWO_CHARSET.find(second_eye)
    return a * 16 + b


# List of commands
def num_to_command(num):
    return COMMAND_LIST[num]


def owos_to_code(owos):
    owos.replace('\n\t', '')
    owos = owos.split(' ')
    if len(owos) % 2 != 0:
        raise ValueError('An even number of OwOs are required!')

    iters = [iter(owos)] * 2
    owos = list(itertools.zip_longest(*iters))

    pseudocode = ''

    for pair in owos:
        pseudocode += num_to_command(owo_pair_to_num(*pair))

    return pseudocode


class OwOScriptConverter(OwOScriptVisitor):
    def __init__(self):
        self.owos = []

    def out(self, number):
        self.owos.append(num_to_owo(number))

    def dump(self):
        return ' '.join(self.owos)

    def visitNumber(self, ctx:OwOScriptParser.NumberContext):
        try:
            number = int(ctx.getChild(1).getText(), 16)
            self.out(number)
        except:
            sys.stderr.write('Not a valid number literal!')
            sys.exit(0)
        return self.visitChildren(ctx)

    def visitWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        self.out(COMMAND_LIST_INVERTED['while {'])
        self.visitChildren(ctx)
        self.out(COMMAND_LIST_INVERTED['}'])

    def visitTernary(self, ctx:OwOScriptParser.TernaryContext):
        self.out(COMMAND_LIST_INVERTED['if {'])
        self.visitChildren(ctx.getChild(2))
        self.out(COMMAND_LIST_INVERTED['} else {'])
        self.visitChildren(ctx.getChild(6))
        self.out(COMMAND_LIST_INVERTED['}'])

    def visitCommand(self, ctx:OwOScriptParser.CommandContext):
        try:
            self.out(COMMAND_LIST_INVERTED[ctx.getText().lower() + ';'])
        except:
            print('%s is not a valid command!' % ctx.getText())
            sys.exit(0)


def code_to_owos(code):
    lexer = OwOScriptLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = OwOScriptParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(OwOErrorListener())

    tree = parser.script()

    visitor = OwOScriptConverter()
    visitor.visit(tree)
    return visitor.dump()

if __name__ == '__main__':
    import argparse

    argparser = argparse.ArgumentParser(description='Convert pseudocode of owoScript to OwO form, or the other way around'
                                                    ' or the other way around. Defaults to converting pseudocode to OwO form')

    argparser.add_argument('file', type=argparse.FileType('r'), help='Filename of file to convert')
    argparser.add_argument('--reverse', '-r', action='store_true', default=False, help='Convert OwO form to pseudocode instead')

    args = argparser.parse_args()

    if args.reverse:
        try:
            sys.stdout.write(owos_to_code(args.file.read()))
        except:
            sys.stderr.write('Invalid owoScript OwO code!')
    else:
        try:
            sys.stdout.write(code_to_owos(args.file.read()))
        except Exception as e:
            raise e
            sys.stderr.write('Invalid owoScript pseudocode!')


