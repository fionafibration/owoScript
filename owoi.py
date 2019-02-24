from OwOScriptGrammar.OwOScriptVisitor import OwOScriptVisitor
from OwOScriptGrammar.OwOScriptParser import OwOScriptParser
from OwOScriptGrammar.OwOScriptLexer import OwOScriptLexer
from antlr4 import *

import sys
import string

class OwOScriptExecutor(OwOScriptVisitor):
    def __init__(self, token_stream, debug=False):
        self.functions = {}
        self.debug = debug
        self.token_stream = token_stream
        self.out = ''
        self.code = ''
        self.stack = []
        self.output = sys.stdout
        self.input = sys.stdin
        self.vars = {}

    def pop(self):
        try:
            return self.stack.pop()
        except:
            return 0

    def push(self, var):
        return self.stack.append(var)

    def indent(self, code):
        indented_string = ''
        indent = 1

        for line in code.split('\n'):
            if '}' in line:
                indent -= 1
            indented_string += '\t' * indent + line + '\n'
            if '{' in line:
                indent += 1

        return indented_string

    def visitBignumber(self, ctx:OwOScriptParser.BignumberContext):
        try:
            self.push(int(float(ctx.getChild(1).getText())))
        except:
            pass

    def visitDefinition(self, ctx:OwOScriptParser.DefinitionContext):
        func_name = ctx.getChild(1).getText()
        func_body = ctx.getChild(3)
        if func_name not in self.functions:
            self.functions[func_name] = func_body

    def visitFunctioncall(self, ctx:OwOScriptParser.FunctioncallContext):
        func_name = ctx.getChild(0).getText()
        if func_name in self.functions:
            self.visitChildren(self.functions[func_name])
        else:
            sys.stderr.write('Unknown function %s' % func_name)
            sys.exit()

    def visitScript(self, ctx: OwOScriptParser.ScriptContext):
        self.code = self.indent(
            ctx.getText()
                .replace(';', ';\n')
                .replace('{', ' {\n')
                .replace('}', '}\n')
        )
        return self.visitChildren(ctx)

    def visitNumber(self, ctx: OwOScriptParser.NumberContext):
        try:
            self.push(int(ctx.getChild(1).getText(), 16))
        except:
            pass
        self.print_info(ctx)
        return self.visitChildren(ctx)

    def visitWhileloop(self, ctx: OwOScriptParser.WhileloopContext):
        while self.stack[-1]:
            self.visitChildren(ctx.getChild(2))
        self.print_info(ctx)

    def visitTernary(self, ctx: OwOScriptParser.TernaryContext):
        if self.pop():
            self.visitChildren(ctx.getChild(2))
        else:
            self.visitChildren(ctx.getChild(6))
        self.print_info(ctx)

    def visitCommand(self, ctx: OwOScriptParser.CommandContext):
        self.exec(ctx.getText().lower())
        self.print_info(ctx)

    def exec(self, command):
        if command == 'add':
            b = self.pop()
            a = self.pop()
            self.push(a + b)

        elif command == 'sub':
            b = self.pop()
            a = self.pop()
            self.push(a - b)

        elif command == 'mult':
            b = self.pop()
            a = self.pop()
            self.push(a * b)

        elif command == 'div':
            b = self.pop()
            a = self.pop()
            if b != 0:
                self.push(a // b)

        elif command == 'mod':
            b = self.pop()
            a = self.pop()
            self.push(a % b)

        elif command == 'exp':
            b = self.pop()
            a = self.pop()
            if a < 30 and b < 30:
                self.push(a ** b)
            else:
                raise ValueError('Too high of an exponent!')

        elif command == 'print':
            a = self.pop()
            if self.debug:
                self.out += chr(a)
            else:
                self.output.write(chr(a))

        elif command == 'printnum':
            a = self.pop()
            if self.debug:
                self.out += str(a)
            else:
                self.output.write(str(a))

        elif command == 'printstack':
            self.output.write(str(self.stack))

        elif command == 'input':
            self.push(ord(self.input.read(1)))

        elif command == 'inputnum':
            num = 0
            data = self.input.read(1)
            while data in '0123456789':
                num *= 10
                num += int(data)
                data = self.input.read(1)
            self.push(num)

        elif command == 'lt':
            b = self.pop()
            a = self.pop()
            self.push(1 if a < b else 0)

        elif command == 'gt':
            b = self.pop()
            a = self.pop()
            self.push(1 if a > b else 0)

        elif command == 'eq':
            b = self.pop()
            a = self.pop()
            self.push(1 if a == b else 0)

        elif command == 'neq':
            b = self.pop()
            a = self.pop()
            self.push(1 if a != b else 0)

        elif command == 'cmp':
            b = self.pop()
            a = self.pop()
            if a == b:
                self.push(0)
            if a > b:
                self.push(1)
            else:
                self.push(-1)

        elif command == 'dupe':
            a = self.pop()
            self.push(a)
            self.push(a)

        elif command == 'dupedeep':
            a = self.pop()
            if a >= 0:
                self.stack.extend(self.stack[-a:])

        elif command == 'stacklength':
            self.push(len(self.stack))

        elif command == 'discard':
            self.pop()

        elif command == 'swap':
            b = self.pop()
            a = self.pop()
            self.push(b)
            self.push(a)

        elif command == 'push':
            b = self.pop()
            a = self.pop()
            if 0 < b < len(self.stack):
                self.stack.insert(len(self.stack) - b, a)
            elif b > len(self.stack):
                self.stack.insert(0, a)
            else:
                self.push(a)

        elif command == 'fetch':
            a = self.pop()
            if 0 < a < len(self.stack):
                val = self.stack.pop(len(self.stack) - a - 1)
                self.push(val)
            elif a >= len(self.stack):
                val = self.stack.pop(0)
                self.push(val)
        
        elif command == 'store':
            b = self.pop()
            a = self.pop()
            self.vars[a] = b

        elif command == 'get':
            a = self.pop()
            self.push(self.vars.get(a, 0))

        elif command == 'stop':
            sys.exit(self.pop())

        elif command == 'fetchdupe':
            a = self.pop()
            if 0 < a < len(self.stack):
                self.push(self.stack[len(self.stack) - a - 1])
            elif a >= len(self.stack):
                self.push(self.stack[0])

        elif command == 'pushdupe':
            b = self.pop()
            a = self.pop()
            if 0 < b < len(self.stack):
                self.stack.insert(len(self.stack) - b, a)
            elif b > len(self.stack):
                self.stack.insert(0, a)
            self.push(a)

        elif command == 'hexmult':
            b = self.pop()
            a = self.pop()
            self.push(a * 16 + b)

        elif command == 'printhash':
            self.output.write('%s' % self.vars)

        elif command == 'nop':
            pass

        else:
            raise ValueError('Unknown command %s' % command)

    def print_info(self, ctx):
        if not self.debug:
            return
        print('\n' * 50)
        if len(self.code) < 8000:
            print('Code:')
            print(self.code)
        print('\n\nStack:')
        print(' | '.join([str(item) for item in self.stack]))
        print(' | '.join([chr(item) if 32 <= item <= 127 else ' ' for item in self.stack]))
        print('\nHashmap:')
        print(', '.join(['%s: %s' % (key, value) for key, value in self.vars.items()]))

        print('Output:')
        print(self.out)
        input()

def run_owo_pseudocode(code, debug):
    lexer = OwOScriptLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = OwOScriptParser(stream)

    parser.removeErrorListeners()

    tree = parser.script()

    visitor = OwOScriptExecutor(stream, debug)
    try:
        visitor.visit(tree)
        if debug:
            print('Completed')
    except Exception as e:
        raise e