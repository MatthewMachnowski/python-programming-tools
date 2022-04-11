import argparse
import glob
import gzip
import json
import os
import re


def calc_statistic(data: dict):
    return {"change": data["high"] - data["low"]}


def analyze(data_dir: str):
    pattern = re.compile("data(\d+).json.gz")

    data_list = glob.glob(os.path.join(data_dir, "*.json.gz"))
    max_change = 0
    probe_num = -1
    for file_path in data_list:
        with gzip.GzipFile(file_path, "r") as gzip_file:
            json_str = gzip_file.read().decode("utf-8")
            data = json.loads(json_str)
            stat = calc_statistic(data)
            if stat["change"] > max_change:
                max_change = stat["change"]
                file_name = os.path.basename(file_path)
                probe_num = pattern.match(file_name).group(1)

    return probe_num, max_change


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("data_dir")

    args = parse.parse_args()
    probe_num, max_change = analyze(args.data_dir)
    print(f"Maximum change of temperature is for probe {probe_num} is {max_change}")


if __name__ == "__main__":
    main()
