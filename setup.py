# setup.py 内容应如下
from setuptools import setup, find_packages

setup(
    name="web_test",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0",
        "pytest>=7.0"
    ]
)