from context import mastermind
from mastermind import mastermind
import copy, sys, unittest

class TestCodeMethods(unittest.TestCase):

    def test_instantiate_empty(self):
        code = mastermind.Code([])
        self.assertIsInstance(code, mastermind.Code)

    def test_instantiate_with_colors(self):
        GREEN = mastermind.Color.GREEN
        code = mastermind.Code([GREEN])
        self.assertIsInstance(code.code.pop(), mastermind.Color)

    def test_deepcopy(self):
        GREEN = mastermind.Color.GREEN
        code = mastermind.Code([GREEN])
        code_copy = copy.deepcopy(code)
        
        self.assertIsInstance(code_copy, mastermind.Code)
        self.assertIs(GREEN, code_copy.code[0])
        self.assertEqual(GREEN, code_copy.code[0])

    def test_assert_one_red_feedback(self):
        GREEN = mastermind.Color.GREEN
        RED = mastermind.Color.RED
        BLUE = mastermind.Color.BLUE

        answer_code = mastermind.Code([GREEN, GREEN])
        guess = mastermind.Code([GREEN, BLUE])

        self.assertIsNone(guess.feedback)
        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertEqual([mastermind.Feedback.RED], guess.feedback)

    def test_assert_empty_feedback(self):
        GREEN = mastermind.Color.GREEN
        RED = mastermind.Color.RED
        BLUE = mastermind.Color.BLUE

        answer_code = mastermind.Code([GREEN, RED])
        guess = mastermind.Code([BLUE, BLUE])

        self.assertIsNone(guess.feedback)
        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertEqual([], guess.feedback)

    def test_assert_two_white_feedback(self):
        GREEN = mastermind.Color.GREEN
        RED = mastermind.Color.RED

        answer_code = mastermind.Code([RED, GREEN])
        guess = mastermind.Code([GREEN, RED])

        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertListEqual([mastermind.Feedback.WHITE, mastermind.Feedback.WHITE], guess.feedback)

    def test_assert_two_white_one_red_feedback(self):
        GREEN = mastermind.Color.GREEN
        RED = mastermind.Color.RED
        BLUE = mastermind.Color.BLUE
        YELLOW = mastermind.Color.YELLOW

        answer_code = mastermind.Code([RED, GREEN, YELLOW, BLUE])
        guess = mastermind.Code([GREEN, RED, YELLOW, RED])

        guess.generate_feedback(answer_code)
        self.assertIsNotNone(guess.feedback)
        self.assertIsInstance(guess.feedback, list)
        self.assertEqual(guess.feedback.count(mastermind.Feedback.WHITE), 2)
        self.assertEqual(guess.feedback.count(mastermind.Feedback.RED), 1)
        self.assertEqual(len(guess.feedback), 3)

    def test_feedback_is_symmetrical(self):
        GREEN = mastermind.Color.GREEN
        RED = mastermind.Color.RED
        BLUE = mastermind.Color.BLUE
        YELLOW = mastermind.Color.YELLOW
        WHITE = mastermind.Color.WHITE

        answer_code = mastermind.Code([RED, GREEN, YELLOW, BLUE])
        guess = mastermind.Code([GREEN, WHITE, YELLOW, GREEN])

        guess.generate_feedback(answer_code)
        answer_code.generate_feedback(guess)
        self.assertEqual(guess.feedback.count(mastermind.Feedback.WHITE), 1)
        self.assertEqual(guess.feedback.count(mastermind.Feedback.RED), 1)
        self.assertEqual(len(guess.feedback), 2)
        self.assertEqual(answer_code.feedback.count(mastermind.Feedback.WHITE), 1)
        self.assertEqual(answer_code.feedback.count(mastermind.Feedback.RED), 1)
        self.assertEqual(len(answer_code.feedback), 2)


def main() -> int:
    """Echo the input arguments to standard output"""
    unittest.main()

if __name__ == '__main__':
    sys.exit(main())
