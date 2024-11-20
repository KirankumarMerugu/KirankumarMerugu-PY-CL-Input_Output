def get_user_input_string(prompt):
    """
    Instead of returning None this method should Get user input as a string.

    Hint : use input()

    :param prompt: The prompt to display to the user.
    :return: The string entered by the user.
    """
    return None # Replace None with your code

def get_user_input_integer(prompt):
    """
    Instead of returning None this method should Get user input as an integer.
    Hint : use input() and  convert it into int data type using int()
    :param prompt: The prompt to display to the user.
    :return: The integer entered by the user.
    """
    while True:
        try:
            return None # Replace None with your code
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_user_input_float(prompt):
    """
    Instead of returning None this method should Get user input as a float.
    Hint : use input() and  convert it into float  data type using float()


    :param prompt: The prompt to display to the user.
    :return: The float entered by the user.
    """
    while True:
        try:
            return None # Replace None with your code
        except ValueError:
            print("Invalid input. Please enter a float.")