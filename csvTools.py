from config import SEPARATOR
from Dataset import Dataset


def parse_csv_file(filename: str):
    """
    Parse a csv file and return the corresponding dataset
    """
    data = []
    with open(filename, 'r') as csvFile:
        fields = parse_csv_line(csvFile.readline())

        for row in csvFile:
            data.append(parse_csv_line(row))
        return Dataset(fields, data)


def parse_csv_line(line: str):
    """
    Parse a csv line and return a list of string
    """
    return line.rstrip().split(SEPARATOR)