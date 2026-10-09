"""Unit tests for Treasure Island. Run with: python -m unittest -v"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from treasure_island import get_choice, main, treasure_game


class TreasureIslandTests(unittest.TestCase):
    def run_round(self, choices):
        output = io.StringIO()
        with patch("builtins.input", side_effect=choices), redirect_stdout(output):
            result = treasure_game()
        return result, output.getvalue()

    def test_yellow_door_wins(self):
        won, output = self.run_round(["left", "wait", "yellow"])
        self.assertTrue(won)
        self.assertIn("YOU WIN!", output)

    def test_right_direction_is_trap(self):
        won, output = self.run_round(["right"])
        self.assertFalse(won)
        self.assertIn("fell into a trap", output)

    def test_swimming_leads_to_shark(self):
        won, output = self.run_round(["left", "swim"])
        self.assertFalse(won)
        self.assertIn("attacked by a shark", output)

    def test_red_door_leads_to_fire(self):
        won, output = self.run_round(["left", "wait", "red"])
        self.assertFalse(won)
        self.assertIn("fire room", output)

    def test_blue_door_leads_to_beast(self):
        won, output = self.run_round(["left", "wait", "blue"])
        self.assertFalse(won)
        self.assertIn("beast room", output)

    def test_uppercase_and_spaces_are_accepted(self):
        won, _ = self.run_round([" LEFT ", " Wait ", "YELLOW "])
        self.assertTrue(won)

    def test_invalid_direction_prompts_again(self):
        won, output = self.run_round(["forward", "left", "wait", "yellow"])
        self.assertTrue(won)
        self.assertIn("Invalid choice!", output)

    def test_invalid_river_choice_prompts_again(self):
        won, output = self.run_round(["left", "jump", "wait", "yellow"])
        self.assertTrue(won)
        self.assertIn("Invalid choice!", output)

    def test_invalid_door_prompts_again(self):
        won, output = self.run_round(["left", "wait", "green", "yellow"])
        self.assertTrue(won)
        self.assertIn("Invalid choice!", output)

    def test_get_choice_returns_normalized_input(self):
        with patch("builtins.input", side_effect=["  no  "]):
            self.assertEqual(get_choice("Continue? ", ("yes", "no")), "no")

    def test_replay_starts_a_new_round(self):
        output = io.StringIO()
        answers = ["right", "YES", "left", "wait", "yellow", "n"]
        with patch("builtins.input", side_effect=answers), redirect_stdout(output):
            main()
        text = output.getvalue()
        self.assertEqual(text.count("WELCOME TO TREASURE ISLAND"), 2)
        self.assertIn("YOU WIN!", text)
        self.assertIn("Goodbye!", text)

    def test_invalid_replay_answer_prompts_again(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=["right", "maybe", "no"]), redirect_stdout(output):
            main()
        self.assertIn("Invalid choice!", output.getvalue())
        self.assertIn("Goodbye!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
