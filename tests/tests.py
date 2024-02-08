from context import mastermind
from mastermind import mastermind
import copy, sys, unittest

class TestCodeMethods(unittest.TestCase):

    def test_instantiate_empty(self):
        code = mastermind.Code([])
        self.assertIsInstance(code, mastermind.Code)

    def test_instantiate_with_colors(self):
        green = mastermind.Color("green")
        code = mastermind.Code([green])
        self.assertIsInstance(code.code.pop(), mastermind.Color)

    def test_deepcopy(self):
        green = mastermind.Color("green")
        code = mastermind.Code([green])
        code_copy = copy.deepcopy(code)
        
        self.assertIsInstance(code_copy, mastermind.Code)
        self.assertIsNot(green, code_copy.code[0])
        self.assertEqual(green, code_copy.code[0])

    def test_assert_one_red_feedback(self):
        green = mastermind.Color("green")
        red = mastermind.Color("red")
        blue = mastermind.Color("blue")

        answer_code = mastermind.Code([green, green])
        guess = mastermind.Code([green, blue])

        self.assertIsNone(guess.feedback)
        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertEqual([mastermind.Feedback.RED], guess.feedback)

    def test_assert_empty_feedback(self):
        green = mastermind.Color("green")
        red = mastermind.Color("red")
        blue = mastermind.Color("blue")

        answer_code = mastermind.Code([green, red])
        guess = mastermind.Code([blue, blue])

        self.assertIsNone(guess.feedback)
        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertEqual([], guess.feedback)

    def test_assert_two_white_feedback(self):
        green = mastermind.Color("green")
        red = mastermind.Color("red")

        answer_code = mastermind.Code([red, green])
        guess = mastermind.Code([green, red])

        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertListEqual([mastermind.Feedback.WHITE, mastermind.Feedback.WHITE], guess.feedback)

    def test_assert_two_white_one_red_feedback(self):
        green = mastermind.Color("green")
        red = mastermind.Color("red")
        blue = mastermind.Color("blue")
        yellow = mastermind.Color("yellow")

        answer_code = mastermind.Code([red, green, yellow, blue])
        guess = mastermind.Code([green, red, yellow, red])

        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertEqual(guess.feedback.count(mastermind.Feedback.WHITE), 2)
        self.assertEqual(guess.feedback.count(mastermind.Feedback.RED), 1)
        self.assertEqual(len(guess.feedback), 3)


def main() -> int:
    """Echo the input arguments to standard output"""
    unittest.main()

if __name__ == '__main__':
    sys.exit(main())
