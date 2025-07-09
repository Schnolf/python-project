import csv
import sys
import pytest
from project import create_file
from project import get_information
from project import add_information
from project import write_to_csv


def test_create_file_with_headers(tmp_path):
    # Simulate creating a new .csv file
    test_file = tmp_path / "series.csv"
    create_file(test_file)
    assert test_file.exists()
    with open(test_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert headers == ["Series", "Rating", "Info"]


def test_add_information_add_header(monkeypatch, tmp_path):
    test_file = tmp_path / "series.csv"
    with open(test_file, "w") as f:
        f.write("wrong_series,2,wrong_info")
    inputs = iter(["Better Call Saul", "4", "Great attorney!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    add_information(test_file)
    with open(test_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert headers == ["Series", "Rating", "Info"]

        rows = list(reader)
        assert rows == [
            ["wrong_series", "2", "wrong_info"],
            ["Better Call Saul", "4", "Great attorney!"]
        ]


def test_get_information_valid_input(monkeypatch):
    # Simulate valid user input
    inputs = iter(["Breaking Bad", "5", "Great show!"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    series, rating, info = get_information()

    assert series == "Breaking Bad"
    assert rating == "5"
    assert info == "Great show!"
