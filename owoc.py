from OwOScriptGrammar.OwOScriptVisitor import OwOScriptVisitor
from OwOScriptGrammar.OwOScriptParser import OwOScriptParser
from OwOScriptGrammar.OwOScriptLexer import OwOScriptLexer
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


import random
import itertools
import owoi
import sys
import zigzag

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
        'nop;',
        'hexmult;',
        'printhash;',
        'dupedeep;',
        'stacklength;'
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


def commands_to_pseudocode(nums):
    # Nums is the list of commands, and functions is the function
    # dictionary
    pseudocode = []

    i = 0
    while i < len(nums):
        command = nums[i]

        # If it isn't a function call or definition, simply add the command
        if command not in [253, 254, 255]:
            try:
                pseudocode.append(COMMAND_LIST[command])
            except Exception as e:
                print(command)
                raise e

        # If it's a function call, pull the varint function name out
        if command == 254:
            i += 1
            func_name = ''
            while True:
                command = nums[i]
                func_name += chr(command & 0x7f)
                if command & 0x80:
                    break
                i += 1

            pseudocode.append('%s();' % func_name)

        # If it's a definition, pull the function name out and then recursively convert the body numbers to commands
        # This should never go over depth 2, the AST parsing doesn't allow definitions inside definitions
        elif command == 255:
            i += 1
            func_name = ''
            while True:
                command = nums[i]
                func_name += chr(command & 0x7f)
                i += 1
                if command & 0x80:
                    break
            #
            start = i

            # Find the end of the body
            while nums[i] != 255:
                i += 1

            pseudocode.append('func %s {' % func_name)
            pseudocode.extend(commands_to_pseudocode(nums[start:i]))
            pseudocode.append('}')


        elif command == 253:
            i += 1
            num = 0
            shift = 0
            while True:
                command = nums[i]
                num |= (command & 0x7f) << shift
                shift += 7
                if command & 0x80:
                    break
                i += 1
                    
            pseudocode.append('number %s;' % zigzag.zigzag_decode(num))

        i += 1

    return pseudocode


def owos_to_code(owos):
    # Take extraneous whitespace out of the owos
    owos.replace('\n\t', '')
    owos = owos.split(' ')

    if len(owos) % 2 != 0:
        raise ValueError('An even number of OwOs are required!')

    # Make the owos into pairs
    iters = [iter(owos)] * 2
    owos = list(itertools.zip_longest(*iters))

    pseudocode = []
    commands = []

    # Convert those pairs into command numbers
    for pair in owos:
        commands.append(owo_pair_to_num(*pair))

    # Convert to commands
    pseudocode.extend(commands_to_pseudocode(commands))

    # Format pseudocode
    formatted_pseudocode = ''
    indent = 0
    for line in pseudocode:
        if '}' in line:
            indent -= 1
        formatted_pseudocode += '\t' * indent + line + '\n'
        if '{' in line:
            indent += 1

    return formatted_pseudocode


class OwOScriptConverter(OwOScriptVisitor):
    def __init__(self):
        self.owos = []

    def _out(self, number):
        self.owos.append(num_to_owo(number))

    def dump(self):
        return ' '.join(self.owos)

    def visitDefinition(self, ctx:OwOScriptParser.DefinitionContext):
        # Output 255 then the function name in "varint" format.
        # The msb will be set on the last char in the function name
        # Then output the function body
        # Then output 255 to finish

        func_name = ctx.getChild(1).getText()
        func_body = ctx.getChild(3)

        self._out(255)

        for char in func_name[:-1]:
            self._out(ord(char))
        self._out(ord(func_name[-1]) | 0x80)

        self.visitChildren(func_body)

        self._out(255)

    def visitFunctioncall(self, ctx:OwOScriptParser.FunctioncallContext):
        # Output 254 then the function name in "varint" format.
        # The msb will be set on the last char in the function name

        func_name = ctx.getChild(0).getText()
        self._out(254)
        for char in func_name[:-1]:
            self._out(ord(char))
        self._out(ord(func_name[-1]) | 0x80)

    def visitNumber(self, ctx:OwOScriptParser.NumberContext):
        try:
            number = int(ctx.getChild(1).getText(), 16)
            self._out(number)
        except:
            sys.stderr.write('Not a valid number literal!')
            sys.exit(0)
        return self.visitChildren(ctx)

    def visitBignumber(self, ctx:OwOScriptParser.BignumberContext):
        number = zigzag.zigzag_encode(int(float(ctx.getChild(1).getText())))
        self._out(253)
        while True:
            out = number & 0x7f
            number >>= 7
            if number:
                self._out(out)
            else:
                self._out(out | 0x80)
                break


    def visitWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        self._out(COMMAND_LIST_INVERTED['while {'])
        self.visitChildren(ctx)
        self._out(COMMAND_LIST_INVERTED['}'])

    def visitTernary(self, ctx:OwOScriptParser.TernaryContext):
        self._out(COMMAND_LIST_INVERTED['if {'])
        self.visitChildren(ctx.getChild(2))
        self._out(COMMAND_LIST_INVERTED['} else {'])
        self.visitChildren(ctx.getChild(6))
        self._out(COMMAND_LIST_INVERTED['}'])

    def visitCommand(self, ctx:OwOScriptParser.CommandContext):
        try:
            self._out(COMMAND_LIST_INVERTED[ctx.getText().lower() + ';'])
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
        except Exception as e:
            sys.stderr.write('Invalid owoScript OwO code!')
            raise e
    else:
        try:
            sys.stdout.write(code_to_owos(args.file.read()))
        except Exception as e:
            sys.stderr.write('Invalid owoScript pseudocode!')
            raise e


