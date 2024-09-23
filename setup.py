# setup.py
# This file makes the project installable as a Python package

from setuptools import setup, find_packages

# Reads the dependencies from the requirements.txt file
with open("requirements.txt") as f:
    required = f.read().splitlines()

# Setup information for the package
setup(
    name='garagentreff_participants',  # Name of the package
    version='0.1',  # Version number
    packages=find_packages(),  # Finds and lists all packages
    include_package_data=True,  # Ensures that JSON and YAML files are included
    install_requires=required,  # Installs the dependencies listed in requirements.txt
    python_requires='>=3.8',  # Ensures that Python 3.8 or higher is used
    entry_points={
        'console_scripts': [
            'garagentreff=garagentreff.garagentreff:main',  # Defines the console command "garagentreff"
        ],
    },
)
