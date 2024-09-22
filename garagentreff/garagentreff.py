# Module docstring (for the whole file):
"""
This module contains functions for managing participants in the Garagentreff application.
"""

import json
import os
import yaml
import time
import sys


# Pfad zur YAML-Konfigurationsdatei
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config.yml")

# Funktion, um die Konfiguration aus der config.yml zu laden
def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

# Konfiguration wird geladen
config = load_config()

# Pfad zur JSON-Datei mit den Teilnehmerdaten, aus der YAML-Konfiguration geladen
JSON_FILE = config['paths']['data_file']

# Funktion, um die Teilnehmerdaten aus der JSON-Datei zu laden
def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_participant():
    first_name = input("Gib deinen Vornamen ein: ")
    last_name = input("Gib deinen Nachnamen ein: ")
    email = input("Gib deine E-Mail-Adresse ein: ")
    phone = input("Gib deine Telefonnummer ein: ")

    participants = load_data()

    for participant in participants:
        if participant["email"] == email:
            print(f"Ein Teilnehmer mit der E-Mail-Adresse {email} ist bereits registriert.")
            return

    new_participant = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }
    participants.append(new_participant)
    save_data(participants)
    print(f"{first_name} {last_name} wurde erfolgreich hinzugefügt!")

def show_all_participants():
    participants = load_data()
    if not participants:
        print("Es sind keine Teilnehmer registriert.")
    else:
        for participant in participants:
            print(f"{participant['first_name']} {participant['last_name']}, 
            E-Mail: {participant['email']}, Telefon: {participant['phone']}")

def show_participant():
    email = input("Gib die E-Mail-Adresse des Teilnehmers ein: ")
    participants = load_data()
    for participant in participants:
        if participant["email"] == email:
            print(f"Gefundener Teilnehmer: {participant['first_name']}
                            {participant['last_name']}, Telefon: {participant['phone']}")
            return
    print(f"Es wurde kein Teilnehmer mit der E-Mail-Adresse {email} gefunden.")

# Hauptmenü des Programms
def main():
    while True:
        print("\n--- Garagentreff Teilnehmer Verwaltung ---")
        print("1. Neuen Teilnehmer hinzufügen")
        print("2. Alle Teilnehmer anzeigen")
        print("3. Spezifischen Teilnehmer anzeigen")
        print("4. Beenden")
        choice = input("Wähle eine Option (1-4): ")

        if choice == "1":
            add_participant()
        elif choice == "2":
            show_all_participants()
        elif choice == "3":
            show_participant()
        elif choice == "4":
            print("Programm wird beendet.")
            time.sleep(1)
            sys.exit()
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")
