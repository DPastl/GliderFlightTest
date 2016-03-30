import unittest

from ..question_class import QuestionClass


class testQuestion(unittest.TestCase):
    def setUp(self):
        self.qc = QuestionClass()

    def test_randomization(self):
        pass


if __name__ == '__main__':
    unittest.main()
