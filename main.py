import argparse
from compute import myadd


def main():
    parser = argparse.ArgumentParser(description='add or multiply two numbers')
    parser.add_argument('arg1', type=int,
                        help='first argment')
    parser.add_argument('arg2', type=int,
                        help='second argment')
    parser.add_argument('arg3', choices=['add', 'mult'],
                        help='add or mult (default: add)')
    args = parser.parse_args()
    a = args.arg1
    b = args.arg2
    c = args.arg3

    print(a, b, c)

if __name__ == '__main__':
    main()
