import gzip
import json
import os
import random

for i in range(1000):
    low = random.gauss(10, 2)
    high = random.gauss(4, 1) + low
    if i == 732:
        high = str(high)

    if i == 896:
        high = "a"
    with gzip.GzipFile(
        os.path.join(os.path.dirname(__file__), "data", f"data{i}.json.gz"), "w"
    ) as fp:
        json_bytes = json.dumps(
            {"type": "temperature", "low": low, "high": high}
        ).encode("utf-8")
        fp.write(json_bytes)
