import unittest
from game_logic import question_generator

class TestQuestionGenerator(unittest.TestCase):
    def test_basic_arithmetic_question_generation(self):
        question, answer = question_generator.generate_basic_arithmetic_question()
        self.assertIsNotNone(question, "Question should not be None.")
        self.assertIsNotNone(answer, "Answer should not be None.")
        self.assertIsInstance(question, str, "Question should be a string.")
        self.assertIsInstance(answer, (int, float), "Answer should be a number.")

    def test_generate_question(self):
        question_types = ['basic_arithmetic', 'intermediate_arithmetic', 'advanced_arithmetic']
        for q_type in question_types:
            with self.subTest(q_type=q_type):
                question, answer = question_generator.generate_question(q_type)
                self.assertIsNotNone(question, "Question should not be None.")
                self.assertIsNotNone(answer, "Answer should be not None.")

if __name__ == '__main__':
    unittest.main()
