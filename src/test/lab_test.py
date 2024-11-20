import unittest
from unittest.mock import patch
from io import StringIO
import time
from src.main.lab import *


class TestUserInputFunctions(unittest.TestCase):

    def test_get_user_input_string(self):
        # Set up the mock input
        with patch('builtins.input', return_value='John'):
            # Print the prompt message
            print("Enter your name: ")
            # Redirect stdout to capture printed output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_user_input_string("")
                # Add a slight delay to ensure prompt message is fully printed
                time.sleep(0.1)
                # Check the result
                self.assertEqual(result, 'John')
                # Check the printed output
                self.assertEqual(fake_out.getvalue().strip(), "")

    def test_get_user_input_integer(self):
        # Set up the mock input
        with patch('builtins.input', side_effect=['abc', '25']):
            # Redirect stdout to capture printed output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_user_input_integer("Enter your age: ")
                # Add a slight delay to ensure prompt message is fully printed
                time.sleep(0.1)
                # Check the result
                self.assertEqual(result, 25)
                # Check the printed output
                self.assertIn("Invalid input. Please enter an integer.", fake_out.getvalue())

    def test_get_user_input_float(self):
        # Set up the mock input
        with patch('builtins.input', side_effect=['abc', '25.5']):
            # Redirect stdout to capture printed output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_user_input_float("Enter your height in meters: ")
                # Add a slight delay to ensure prompt message is fully printed
                time.sleep(0.1)
                # Check the result
                self.assertEqual(result, 25.5)
                # Check the printed output
                self.assertIn("Invalid input. Please enter a float.", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
