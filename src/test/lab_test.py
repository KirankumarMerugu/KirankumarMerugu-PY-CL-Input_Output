import unittest
from unittest.mock import patch
from io import StringIO
import time
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.main.lab import get_user_input_float, get_user_input_integer, get_user_input_string


class TestUserInputFunctions(unittest.TestCase):

    def test_get_user_input_string(self):
        with patch('builtins.input', return_value='John'):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_user_input_string("Enter your name: ")
                time.sleep(0.1)
                self.assertEqual(result, 'John')
                self.assertEqual(fake_out.getvalue().strip(), "")

    def test_get_user_input_integer(self):
        with patch('builtins.input', side_effect=['abc', '25']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_user_input_integer("Enter your age: ")
                time.sleep(0.1)
                self.assertEqual(result, 25)
                self.assertIn("Invalid input. Please enter an integer.", fake_out.getvalue())

    def test_get_user_input_float(self):
        with patch('builtins.input', side_effect=['abc', '25.5']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_user_input_float("Enter your height in meters: ")
                time.sleep(0.1)
                self.assertEqual(result, 25.5)
                self.assertIn("Invalid input. Please enter a float.", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
