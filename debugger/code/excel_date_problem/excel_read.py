import csv

COLUMN_NAMES = [
    "GeVIR %",
    "LOEUF %",
    "VIRLoF %",
    "GeVIR AD",
    "LOEUF AD",
    "VIRLoF AD",
    "GeVIR AR",
    "LOEUF AR",
    "VIRLoF AR",
]


def main():
    sum_dict = {x: 0 for x in COLUMN_NAMES}
    count = 0
    with open("table.csv") as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        for row in spamreader:
            count += 1
            for name in COLUMN_NAMES:
                sum_dict[name] += float(row[name])
            assert row["Gene Name"][0].isupper() or row["Gene Name"][0].isdigit()
    for name, val in sum_dict.items():
        print(name, val / count)


if __name__ == "__main__":
    main()
