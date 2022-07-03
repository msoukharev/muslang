import argparse as ap
from muslang.compiler import compile


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('--src', required=True, dest='src')
    parser.add_argument('--target', required=True, dest='target')
    args = parser.parse_args()
    compile(args.src, args.target)


main()
