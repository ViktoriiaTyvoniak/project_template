def write_to_console(text):
    """
    Outputs the given text to the console.
    Args:
        text (str): The text to display in the console.
    """
    print(text)


def write_to_file_builtin(text, filename="output.txt"):
    """
    Writes the given text to a file using Python's built-in file handling.
    Args:
        text (str): The text to be written to the file.
        filename (str): The name of the file to write to. Defaults to 'output.txt'.
       """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")
