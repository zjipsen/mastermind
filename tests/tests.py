from context import mastermind
from mastermind import mastermind
import sys, unittest

class TestCodeMethods(unittest.TestCase):

    def test_instantiate(self):
        self.assertIsInstance(mastermind.Code([]), mastermind.Code)

def main() -> int:
    """Echo the input arguments to standard output"""
    unittest.main()

if __name__ == '__main__':
    sys.exit(main())
