from lab import *


def main():
    # String input
    name = get_user_input_string("Enter your name: ")
    print("Hello, {}!".format(name))

    # Integer input
    age = get_user_input_integer("Enter your age: ")
    print("You are {} years old.".format(age))

    # Float input
    height = get_user_input_float("Enter your height in meters: ")
    print("Your height is {} meters.".format(height))


if __name__ == "__main__":
    main()
