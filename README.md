# TV Series Manager

## Overview
TV Series Manager is a command-line application that allows users to manage their TV series by creating and updating a `.csv` file. Users can add series, rate them, and optionally include additional information. The program ensures the `.csv` file has the correct headers and provides options to view the list or quit the application.

## Features
- Create a new `.csv` file or use an existing one.
- Add TV series with ratings (1 to 5) and optional additional information.
- View the list of TV series in a tabular format.

## Requirements
- Python 3.x
- Libraries: `pyfiglet`, `csv`, `sys`, `tabulate`, `pandas`, `pathlib`

## Installation
Install the required libraries using pip:
```bash
pip install pyfiglet tabulate pandas
```

## Usage
Run the program from the command line:
```bash
python project.py <filename.csv>
```
Where `<filename.csv>` is the name of the `.csv` file you want to create or use.

### Example Workflow
1. Start the program:
   ```bash
   python project.py series.csv
   ```
2. If the file does not exist, it will be created automatically.
3. Follow the prompts to:
   - Add new series.
   - View the list of series.
   - Quit the program.

## Notes
- The program validates the `.csv` file format and ensures proper headers.
- Ratings must be numeric and between 1 to 5.
- The tabular view of the series uses the `tabulate` library for formatting.

## Testing

To ensure the functionality of the program, unit tests have been written using `pytest`. Follow these steps to run the tests:

### Prerequisites
- Ensure `pytest` is installed:
  ```bash
  pip install pytest
  ```

### Running Tests
Run all tests by executing the following command in the terminal:
```bash
pytest test_project.py
```

### Test Coverage
The tests cover the following functionalities:
- Validation of command-line arguments (`check_file` function).
- Creation of a new `.csv` file (`create_file` function).
- Adding and validating user input (`get_information` function).
- Ensuring proper headers in the `.csv` file.

## License
This project is licensed under the MIT License.