import argparse
import sys
import itertools
from bfi import parse, Opcode

OPCODE_MOVE   = 0
OPCODE_LEFT   = 1
OPCODE_RIGHT  = 2
OPCODE_ADD    = 3
OPCODE_SUB    = 4
OPCODE_OPEN   = 5
OPCODE_CLOSE  = 6
OPCODE_INPUT  = 7
OPCODE_OUTPUT = 8
OPCODE_CLEAR  = 9
OPCODE_COPY   = 10
OPCODE_SCANL  = 11
OPCODE_SCANR = 12

class BFIToOwO:
    def __init__(self, opcodes, wrapping):
        self.wrapping = wrapping
        self.indent = 0
        self.out = ''
        self.opcodes = opcodes
        for opcode in self.opcodes:
            self._convert(opcode)

    def dump(self):
        return self.__str__()

    def __str__(self):
        return self.out

    def _out(self, output):
        if '}' in output:
            self.indent -= 1
        self.out += '\t' * self.indent + output + '\n'
        if '{' in output:
            self.indent += 1

    def _convert(self, opcode):
        if self.out != '':
            self._out('')
        self._out('// %s' % opcode)
        if opcode.code == OPCODE_MOVE:
            self._move(opcode.value)
        elif opcode.code == OPCODE_OPEN:
            self._move(opcode.move)
            self._out('dupe;')
            self._out('get;')
            self._out('while {')
            self._out('discard;')
        elif opcode.code == OPCODE_CLOSE:
            self._move(opcode.move)
            self._out('dupe;')
            self._out('get;')
            self._out('}')
            self._out('discard;')
        elif opcode.code == OPCODE_ADD:
            self._move(opcode.move)
            self._out('dupe;')
            self._out('dupe;')
            self._out('get;')
            self._number(opcode.value)
            self._out('add;')
            self._wrap()
            self._out('store;')
        elif opcode.code == OPCODE_SUB:
            self._move(opcode.move)
            self._out('dupe;')
            self._out('dupe;')
            self._out('get;')
            self._number(opcode.value)
            self._out('sub;')
            self._wrap()
            self._out('store;')
        elif opcode.code == OPCODE_INPUT:
            self._move(opcode.move)
            self._out('dupe;')
            self._out('input;')
            self._wrap()
            self._out('store;')
        elif opcode.code == OPCODE_OUTPUT:
            self._move(opcode.move)
            self._out('dupe;')
            self._out('get;')
            self._out('print;')
        elif opcode.code == OPCODE_CLEAR:
            self._move(opcode.move)
            self._out('dupe;')
            self._number(0)
            self._out('store;')
        elif opcode.code == OPCODE_COPY:
            self._move(opcode.move)
            # Get positions
            positions = sorted(list(opcode.value.keys()))

            # Moves are the differences between positions
            moves = [j - i for i, j in zip(positions[:-1], positions[1:])]

            # Values are the values we should output, in order of position
            values = [opcode.value[position] for position in positions]

            # Keys are moves, values are things to put in
            moves_to_values = itertools.zip_longest([0] + moves, values, fillvalue=None)

            self._out('dupe;')
            self._out('get;')
            self._out('dupe;')
            self._out('if {')

            self._out('swap;')
            self._move(positions[0])

            for move, value in moves_to_values:
                self._move(move)
                self._out('dupe;')
                self._out('dupe;')
                self._number(value)
                self._number(4)
                self._out('fetchdupe;')
                self._out('mult;')
                self._out('swap;')
                self._out('get;')
                self._out('add;')
                self._wrap()
                self._out('store;')

            self._out('swap;')
            self._out('discard;')

            self._move(-positions[-1])

            self._convert(Opcode(OPCODE_CLEAR, 0))
            self._out('}')
            self._out('else {')
            self._out('discard;')
            self._out('}')

        elif opcode.code == OPCODE_SCANL:
            self._move(opcode.move)
            self._convert(Opcode(OPCODE_OPEN))
            self._convert(Opcode(OPCODE_MOVE, 0, -1))
            self._convert(Opcode(OPCODE_CLOSE))

        elif opcode.code == OPCODE_SCANR:
            self._move(opcode.move)
            self._convert(Opcode(OPCODE_OPEN))
            self._convert(Opcode(OPCODE_MOVE, 0, 1))
            self._convert(Opcode(OPCODE_CLOSE))

        else:
            raise ValueError('Invalid opcode %s' % opcode.code)

    def _move(self, num_to_move):
        if num_to_move > 0:
            self._number(abs(num_to_move))
            self._out('add;')
        elif num_to_move < 0:
            self._number(abs(num_to_move))
            self._out('sub;')

    def _number(self, number):
        if number < 16 and number > 0:
            for line in number_rep(number).split('\n'):
                self._out(line)
        else:
            self._out('number %s;' % number)

    def _wrap(self):
        if self.wrapping:
            self._number(256)
            self._out('mod;')

def number_rep(number):
    def literal(hex_digit):
        return 'literal %s;\nhexmult;' % hex_digit

    hex_string = hex(number)[2:]
    return (f'literal {hex_string[0]};\n' + '\n'.join([literal(digit) for digit in hex_string[1:]])).strip('\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert brainfuck to OwO script pseudocode')

    parser.add_argument('file', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin, help='Brainfuck file to _convert to owoScript')
    parser.add_argument('--no-wrapping', '-w', action='store_false', default=True, dest='wrapping',
                        help='Disable the generation of wrapping code. If not used, wrapping will default'
                             ' to 8 bit unsigned cells')

    args = parser.parse_args()

    program = args.file.read()

    parsed = parse(program)

    owogenerator = BFIToOwO(parsed, args.wrapping)

    sys.stdout.write(owogenerator.dump())

