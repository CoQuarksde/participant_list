# setup.py
# Diese Datei macht das Projekt als Python-Paket installierbar

from setuptools import setup, find_packages

# Liest die Abhängigkeiten aus der requirements.txt-Datei
with open("requirements.txt") as f:
    required = f.read().splitlines()

# Setup-Informationen für das Paket
setup(
    name='garagentreff_teilnehmer',  # Name des Pakets
    version='0.1',  # Versionsnummer
    packages=find_packages(),  # Findet und listet alle Pakete auf
    include_package_data=True,  # Stellt sicher, dass die JSON- und YAML-Dateien enthalten sind
    install_requires=required,  # Installiert die in requirements.txt aufgeführten Abhängigkeiten
    python_requires='>=3.8',  # Stellt sicher, dass Python 3.8 oder höher verwendet wird
    entry_points={
        'console_scripts': [
            'garagentreff=garagentreff.garagentreff:main',  # Definiert den Konsolenbefehl "garagentreff"
        ],
    },
)
