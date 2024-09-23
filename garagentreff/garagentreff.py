import json
import os
import yaml
import time
import sys

# Path to the YAML configuration file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config.yml")

# Function to load the YAML config file
def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

# Load the config
config = load_config()

# Path to the JSON file with participant data (loaded from YAML config)
JSON_FILE = config['paths']['data_file']

# Function to load participant data from the JSON file
def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Function to save participant data to the JSON file
def save_data(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Function to get non-empty input from the user, with 'x' to exit
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()  # Remove leading/trailing spaces
        if value.lower() == 'x':
            print("\nExiting the program.")
            sys.exit()  # Exit the program when 'x' is entered
        elif value:
            return value
        print("Input cannot be empty. Please enter a valid value.")
        print("Or Exit the program with 'x'\n")


# Function to add a new participant
def add_participant():
    # Prompt for non-empty first name, last name, and email
    first_name = get_non_empty_input("Enter your first name: ")
    last_name = get_non_empty_input("Enter your last name: ")
    email = get_non_empty_input("Enter your email address: ")

    # Load existing participants
    participants = load_data()

    # Immediately check if the email already exists
    for participant in participants:
        if participant["email"] == email:
            print(f"A participant with the email {email} already exists.")
            return  # Exit the function if the email is already registered

    # If the email does not exist, proceed to collect the phone number
    phone = get_non_empty_input("Enter your phone number: ")

    # Create a new participant entry
    new_participant = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }
    participants.append(new_participant)

    # Save the updated participant list to the JSON file
    save_data(participants)
    print(f"{first_name} {last_name} was successfully added!")



    # Save the updated participant list to the JSON file
    save_data(participants)
    print(f"{first_name} {last_name} was successfully added!")

# Function to display all participants
def show_all_participants():
    participants = load_data()
    if not participants:
        print("\n No participants are registered.")
    else:
        for participant in participants:
            print(f"{participant['first_name']} {participant['last_name']}, "
                  f"Email: {participant['email']}, Phone: {participant['phone']}")

# Function to display a specific participant by email
def show_participant():
    email = input("\nEnter the email address of the participant: ")
    participants = load_data()
    for participant in participants:
        if participant["email"] == email:
            print(f"Found participant: {participant['first_name']} {participant['last_name']}, "
                  f"Phone: {participant['phone']}")
            return
    print(f"No participant found with the email address {email}.")

# Main menu of the application
def main():
    while True:
        print("\n--- Garagentreff Participant Management ---")
        print("1. Add a new participant")
        print("2. Show all participants")
        print("3. Show a specific participant")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_participant()
        elif choice == "2":
            show_all_participants()
        elif choice == "3":
            show_participant()
        elif choice == "4":
            print("\nExiting the program.")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid selection, please try again.")
