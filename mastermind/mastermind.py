# -*- coding: utf-8 -*-
import sys

def play():
    print("Hello World")

def main() -> int:
    """Echo the input arguments to standard output"""
    print("Main file")
    play()

if __name__ == '__main__':
    sys.exit(main())
