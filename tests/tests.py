from context import mastermind
from mastermind import mastermind
import sys, unittest

def test_code():
    c1 = mastermind.Code([])
    print(f'{c1}')
    print("hi")


def main() -> int:
    """Echo the input arguments to standard output"""
    test_code()

if __name__ == '__main__':
    sys.exit(main())
