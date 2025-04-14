from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import write_to_console, write_to_file_builtin


def main():
    """
    Main function that:
    - Reads text from the console.
    - Reads text from a .txt file using built-in methods.
    - Reads data from a .csv file using pandas.
    - Displays each of the results in the console.
    - Writes each of the results to an output file.
    """

    text_from_console = read_from_console()
    text_from_txt_file = read_from_file_builtin()
    text_from_csv_file = read_from_file_pandas()

    write_to_console("\n--- Text entered by user ---")
    write_to_console(text_from_console)

    write_to_console("\n--- Text read from 'input.txt' ---")
    write_to_console(text_from_txt_file)

    write_to_console("\n--- Data read from 'input.csv' using pandas ---")
    write_to_console(text_from_csv_file)

    write_to_file_builtin("--- Text entered by user ---")
    write_to_file_builtin(text_from_console)

    write_to_file_builtin("--- Text read from 'input.txt' ---")
    write_to_file_builtin(text_from_txt_file)

    write_to_file_builtin("--- Data read from 'input.csv' using pandas ---")
    write_to_file_builtin(text_from_csv_file)


if __name__ == "__main__":
    main()
