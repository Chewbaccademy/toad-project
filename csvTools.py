from config import SEPARATOR
from Dataset import Dataset
from Datum import Datum

# -o 
def parse_csv_file(filename, optimized_indexes=[]):
    """
    Parse a csv file and return the corresponding dataset
    """
    data = []
    with open(filename, 'r') as csvFile:
        fields = csvFile.readline().rstrip().split(SEPARATOR)
        if len(optimized_indexes) != 0:
            fields = [fields[i] for i in range(len(fields)) if i in optimized_indexes]

        for row in csvFile:
            data.append(parse_csv_line(row, optimized_indexes))
        return Dataset(fields, data)


def parse_csv_line(line, optimized_indexes=[]):
    """
    Parse a csv line and return a list of string
    """
    parsed_line = line.rstrip().split(SEPARATOR)

    if len(optimized_indexes) == 0:
        return Datum(parsed_line)

    result = [parsed_line[i] for i in range(len(parsed_line)) if i in optimized_indexes]
    return Datum(result)