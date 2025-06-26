from pyfiglet import Figlet
import csv
import sys
from tabulate import tabulate
import pandas as pd


def main():
    check_file()
    welcome = Figlet(font="slant")
    print(welcome.renderText("Welcome to your TV series manager!"))
    create_add()


def check_file():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        elif len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")

        elif (sys.argv[1]).lower().split(".")[1] != "csv":
            try:
                with open(sys.argv[1]) as file:
                    sys.exit(
                        "Not a .csv file")
            except FileNotFoundError:
                sys.exit(
                    "Either input an existing .csv file or create a new .csv file")
        else:
            return True
    except IndexError:
        sys.exit("Either input an existing .csv file or create a new .csv file")


def get_information():
    series = input("What is the name of the TV series? ")
    rating = input("What is your Rating (from 1 to 5)? ")
    info = input("(optional) Add additional information: ")
    return series, rating, info


def create_add():
    print(f"Your information will be added to file: {sys.argv[1]}.")
    open_file()


def open_file():
    while True:
        add_information = input(
            "Do you want to add a new series? (yes/no) ")

        if add_information == "yes":
            try:
                with open(sys.argv[1], newline='') as f:
                    reader = csv.reader(f)
                    row_1 = next(reader)
                    if row_1 != ["Series", "Rating", "Info"]:
                        df = pd.read_csv(sys.argv[1], header=None)
                        df.to_csv(sys.argv[1], header=[
                            "Series", "Rating", "Info"], index=False)
            except:
                with open(sys.argv[1], "w") as file:
                    fieldnames = ["Series", "Rating", "Info"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()

            series, rating, info = get_information()
            with open(sys.argv[1], "a") as file:
                fieldnames = ["Series", "Rating", "Info"]
                writer = csv.DictWriter(
                    file, fieldnames=fieldnames)
                writer.writerow(
                    {"Series": series, "Rating": rating, "Info": info})
        elif add_information == "no":
            show_quit = input(
                "Do you want to see your list or quit the program? (see/quit) ")
            if show_quit == "see":
                show_file()
                break
            elif show_quit == "quit":
                quit_file()
                break
            else:
                print("Please answer with 'see' or 'quit'.")
        else:
            print("Please answer with 'yes' or 'no'.")


def quit_file():
    goodbye = Figlet(font="slant")
    print(goodbye.renderText("Thanks for using the TV series manager!"))


def show_file():
    series = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            series.append(row)
        series = tabulate(series, headers="keys", tablefmt="grid")
        print(series)
        quit_file()


if __name__ == "__main__":
    main()
