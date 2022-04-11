import os

with open(os.path.join(os.path.dirname(__file__), "text.txt")) as f_p:
    text = f_p.read().strip()


def function():
    print(text)