from setuptools import *

setup(
    # Metadata
    name="babel-cli",
    version="0.3.5",
    author="Calder Coalson",
    author_email="caldercoalson@gmail.com",
    url="https://github.com/Calder/babel-cli",
    description = "A command line interface for sending anything anywhere.",
    long_description="See https://github.com/calder/babel-cli/ for documentation.",
    license="LICENSE.txt",

    # Contents
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "babel=babel:main",
        ],
    },

    # Dependencies
    install_requires=[
        "PySocks", # Required but not declared by twilio
        "requests-futures",
        "toml",
        "twilio",
    ],

    # Settings
    zip_safe=True,
)