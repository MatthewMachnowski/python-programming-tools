from iris_analysis import calculate
from iris_analysis.io.load import load_file
from iris_analysis.io.save import save_file
import sys


if __name__ == '__main__':
    data = load_file(sys.argv[1])
    result = []
    for f in (calculate.mean, calculate.median, calculate.std):
        result.append({key: f(data[key]) for key in data})

    save_file(sys.argv[2], result)
