import csv


def load_file(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)

        result = {}
        for row in reader:
            del row['variety']
            for column, value in row.items():
                result.setdefault(column, []).append(float(value))

    return result
