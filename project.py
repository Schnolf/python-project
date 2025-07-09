from pyfiglet import Figlet
import csv
import sys
from tabulate import tabulate
import pandas as pd
from pathlib import Path

""" 
TV Series Manager
This program allows you to manage your TV series by adding, viewing, and quitting the list.
It creates a CSV file to store the series, their ratings, and additional information.
Usage:
    python project.py <filename.csv>

Where <filename.csv> is the name of the CSV file you want to create or use.
It will prompt you to add series and their ratings, and you can view the list or quit the program.
Make sure to have the required libraries installed: pyfiglet, tabulate, pandas and pathlib.
This program is designed to be run from the command line.
It will create a new CSV file if it does not exist, or append to an existing one.
It will also ensure that the CSV file has the correct headers if it is newly created.
"""

# Function to check if the file is not a CSV file and if the file exists and create it if it doesn't


def main():
    if len(sys.argv) != 2:
        sys.exit("Command-line argument must contain one .csv file")
    filename = sys.argv[1]
    if not filename.lower().endswith(".csv"):
        sys.exit("Not a .csv file.")
    if not Path(filename).exists():
        print(f"Cannot find file. File {filename} will be created.")
        create_file(filename)
    else:
        print(f"File {filename} exists.")
    welcome = Figlet(font="smslant")
    print(welcome.renderText("Welcome to your TV series manager!"))
    user_add_quit(filename)


# Function to create a new CSV file with headers.
# This function creates a new CSV file with the specified headers if it does not already exist.


def create_file(filename):
    with open(filename, "w") as file:
        fieldnames = ["Series", "Rating", "Info"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    print(f"File {filename} has been created.")


# Function to create or add information to the CSV file and prompt the user to continue or quit.
# This function allows the user to add new series, view the list, or quit the program.


def user_add_quit(filename):
    print(f"Your information will be added to file: {filename}.")
    while True:
        add_series = input("Do you want to add a new series? (yes/no) ")

        if add_series == "yes":
            add_information(filename)

        elif add_series == "no":
            show_quit = input(
                "Do you want to see your list or quit the program? (see/quit) "
            )
            if show_quit == "see":
                show_file(filename)
                break
            elif show_quit == "quit":
                quit_file()
                break
            else:
                print("Please answer with 'see' or 'quit'.")
        else:
            print("Please answer with 'yes' or 'no'.")


# Function to create or add information to the CSV file.
# This function checks if the CSV file has headers and adds them if they are missing.
# If the file already exists, it appends the new series information to the CSV file.
# If the file does not exist, it creates a new CSV file with the specified headers.


def add_information(filename):
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        row_1 = next(reader)
        if row_1 != ["Series", "Rating", "Info"]:
            df = pd.read_csv(filename, header=None)
            df.to_csv(
                filename,
                header=["Series", "Rating", "Info"],
                index=False,
            )
            print(f"Headers have been added to {filename}.")
            write_to_csv(filename)
        else:
            write_to_csv(filename)


# Function to write the series information to the CSV file.
# This function retrieves the series name, rating, and additional information from the user
# and appends it to the specified CSV file.


def write_to_csv(filename):
    series, rating, info = get_information()
    with open(filename, "a") as file:
        fieldnames = ["Series", "Rating", "Info"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(
            {"Series": series, "Rating": rating, "Info": info})
    print(
        f"Series '{series}' with rating {rating} and info '{info}' has been added to {filename}."
    )


# Function to get information from the user.
# This function prompts the user for the name of the TV series, rating, and optional additional information.
# It validates the rating input to ensure it is a number between 1 and 5.
# It returns the series name, rating, and additional information as a tuple.


def get_information():
    series = input("What is the name of the TV series? ")
    while True:
        rating = input("What is your Rating (from 1 to 5)? ")
        if rating.isdigit() and rating in ["1", "2", "3", "4", "5"]:
            break
        print("Please enter a valid numeric rating from 1 to 5.")

    info = input("(optional) Add additional information: ")
    return series, rating, info


# Function to display the contents of the CSV file in a tabular format.
# This function reads the CSV file and uses the tabulate library to format the data into a grid.


def show_file(filename):
    series = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            series.append(row)
        series = tabulate(series, headers="keys", tablefmt="double_grid")
        print(f"\n\n{series}\n\n")
        quit_file()


# Function to print a goodbye message when quitting the program.
# This function uses the Figlet library to create a stylized text message.


def quit_file():
    goodbye = Figlet(font="smslant")
    print(goodbye.renderText("Thanks for using the TV series manager!"))


if __name__ == "__main__":
    main()
