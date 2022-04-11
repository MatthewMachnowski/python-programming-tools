from collections import defaultdict
from random import randint, random


def create_que():
    return defaultdict(list)


def put_in_priority_que(que, priority, value):
    que[priority].append(value)


def get_from_queue(que):
    if not que:
        return None
    key = list(sorted(que))[0]
    value = que[key].pop(0)
    if not que[key]:
        del que[key]
    return value


def generate_data():
    base = [(randint(0, 1000), randint(0, 1000), 0.0) for _ in range(10**5)]
    extend = [(randint(100, 200), randint(0, 1000), random()) for _ in range(10**5)]
    return base + extend


def perform(que, data):
    for priority, value, prop in data:
        if prop > 0.7:
            get_from_queue(que)
        put_in_priority_que(que, priority, value)
