from setuptools import setup

import toml

with open("data.toml") as f_p:
    data = toml.load(f_p)

setup(
    platforms=data["metadata"]["platforms"],
    version=data["metadata"]["version"]
)