import csv


def save_file(filename, lst):
    with open(filename, 'w', newline='') as f:
        fieldnames = []
        for key in lst[0]:
            fieldnames.append(key)

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in lst:
            writer.writerow(row)
