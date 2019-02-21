from owoi import run_owo_pseudocode
from owoc import owos_to_code
import sys
import argparse


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Run OwO code in OwO form.')

    argparser.add_argument('file', type=argparse.FileType('r'), help='File with OwO code')
    argparser.add_argument('--pseudo', '-p', action='store_true', default=False,
                           help='Whether to run OwO bytecode or pseudocode. Use this for testing without having to compile')

    args = argparser.parse_args()

    code = args.file.read()
    if not args.pseudo:
        decompiled_code = owos_to_code(code)
    else:
        decompiled_code = code

    run_owo_pseudocode(decompiled_code)