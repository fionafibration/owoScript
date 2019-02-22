from OwOScriptGrammar.OwOScriptVisitor import OwOScriptVisitor
from OwOScriptGrammar.OwOScriptParser import OwOScriptParser
from OwOScriptGrammar.OwOScriptLexer import OwOScriptLexer
from antlr4 import *


import sys


class OwOScriptExecutor(OwOScriptVisitor):
    def __init__(self):
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

    def visitNumber(self, ctx: OwOScriptParser.NumberContext):
        try:
            self.push(int(ctx.getChild(1).getText(), 16))
        except:
            pass
        return self.visitChildren(ctx)

    def visitWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        while self.stack[-1]:
            self.visitChildren(ctx.getChild(2))

    def visitTernary(self, ctx:OwOScriptParser.TernaryContext):
        if self.pop():
            self.visitChildren(ctx.getChild(2))
        else:
            self.visitChildren(ctx.getChild(6))

    def visitCommand(self, ctx:OwOScriptParser.CommandContext):
        return self.exec(ctx.getText().lower())

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
            self.output.write(chr(a))

        elif command == 'printnum':
            a = self.pop()
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


def run_owo_pseudocode(code):
    lexer = OwOScriptLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = OwOScriptParser(stream)

    parser.removeErrorListeners()

    tree = parser.script()

    visitor = OwOScriptExecutor()
    try:
        visitor.visit(tree)
    except Exception as e:
        return str(e)