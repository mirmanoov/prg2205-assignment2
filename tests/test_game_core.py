import unittest
from game_logic import game_core
from utils.data_structures import UserData

class TestGameCore(unittest.TestCase):
    def setUp(self):
        self.user_data = UserData(name="TestUser")

    def test_start_and_end_game(self):
        # Mock user data and question type
        question_type = "basic_arithmetic"
        game_core.start_game(question_type, self.user_data.__dict__)

        # Check if the game modifies the user_data correctly
        self.assertIsInstance(self.user_data.score, int, "Score should be an integer.")
        self.assertGreaterEqual(self.user_data.score, 0, "Score should be non-negative.")

        # Test end_game function
        game_core.end_game(self.user_data.__dict__)
        self.assertGreaterEqual(self.user_data.level, 1, "Level should be at least 1 after ending the game.")

if __name__ == '__main__':
    unittest.main()
