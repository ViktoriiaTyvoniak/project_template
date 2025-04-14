import pandas as pd


def read_from_console():
    """
    Prompts the user to enter text via the console and returns it
    Returns:
        str: The text entered by the user.
    """
    return input("Please enter some text: ")


def read_from_file_builtin():
    """
    Reads the content of a file named 'input.txt' using Python's built-in file handling.
    Returns:
        str: The contents of 'input.txt'. If the file does not exist, returns an error message.
    """
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: 'input.txt' was not found."


def read_from_file_pandas():
    """
    Reads the content of a file named 'input.csv' using the pandas library and returns it as a string.
    Returns:
        str: The contents of 'input.csv' formatted as a table. If the file does not exist, returns an error message.
    """
    try:
        df = pd.read_csv("input.csv")
        return df.to_string(index=False)
    except FileNotFoundError:
        return "Error: 'input.csv' was not found."
