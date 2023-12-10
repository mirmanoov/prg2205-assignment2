import unittest
from game_logic.scoring import update_score, display_score

class TestScoring(unittest.TestCase):
    def setUp(self):
        self.user_data = {"score": 0}

    def test_update_score_correct_answer(self):
        update_score(self.user_data, True)
        self.assertEqual(self.user_data['score'], 10, "Score should increase by 10 for a correct answer.")

    def test_update_score_incorrect_answer(self):
        update_score(self.user_data, False)
        self.assertEqual(self.user_data['score'], -5, "Score should decrease by 5 for an incorrect answer.")

    def test_display_score(self):
        self.user_data['score'] = 20
        with self.assertRaises(TypeError):
            display_score()  # Testing without passing user_data

        self.assertIsNone(display_score(self.user_data), "display_score should return None.")

if __name__ == '__main__':
    unittest.main()
