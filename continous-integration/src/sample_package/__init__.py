import json
import os
from functools import lru_cache

DATA = None


@lru_cache
def fibonacci(num: int) -> int:
    """
    This function caluculate n-th number of fibbonaci. Ist use cache to achive linear times of caluculation.

    :param int num: position in sequece
    :return: fibbonaci num
    """
    if num < 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def good_data(val: float) -> bool:
    """
    Check if
    :param val:
    :return:
    """
    global DATA
    if DATA is None:
        with open(os.path.join(os.path.dirname(__file__), "data.json")) as f_p:
            DATA = json.load(f_p)
    return DATA["lower"] < val < DATA["upper"]
