import csv
import sys
import pytest
from project import check_file
from project import get_information
from project import create_file


def test_check_file_no_argument(monkeypatch):
    # Simulate no command-line argument
    monkeypatch.setattr(sys, "argv", ["project.py"])
    with pytest.raises(SystemExit) as excinfo:
        check_file()
    assert str(excinfo.value) == "Command-line argument must contain one .csv file"


def test_check_file_invalid_extension(monkeypatch):
    # Simulate an invalid file extension
    monkeypatch.setattr(sys, "argv", ["project.py", "series.txt"])
    with pytest.raises(SystemExit) as excinfo:
        check_file()
    assert str(excinfo.value) == "Not a .csv file."


def test_check_file_create_new_file(monkeypatch, tmp_path):
    # Simulate a new file creation
    test_file = tmp_path / "series.csv"
    monkeypatch.setattr(sys, "argv", ["project.py", str(test_file)])
    result = check_file()
    assert result == str(test_file)
    assert test_file.exists()


def test_check_file_existing_file(monkeypatch, tmp_path):
    # Simulate an existing file
    test_file = tmp_path / "series.csv"
    test_file.touch()  # Create the file
    monkeypatch.setattr(sys, "argv", ["project.py", str(test_file)])
    result = check_file()
    assert result == str(test_file)


def test_get_information_valid_input(monkeypatch):
    # Simulate valid user input
    inputs = iter(["Breaking Bad", "5", "Great show!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    series, rating, info = get_information()

    assert series == "Breaking Bad"
    assert rating == "5"
    assert info == "Great show!"


def test_create_file(monkeypatch, tmp_path):
    # Simulate creating a new .csv file
    test_file = tmp_path / "series.csv"
    monkeypatch.setattr(sys, "argv", ["project.py", str(test_file)])
    # Call the function to create the file
    create_file()
    assert test_file.exists()
    with open(test_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert headers == ["Series", "Rating", "Info"]
