import json

config_file = "conversions.json"

def load_conversions():
    try:
        with open(config_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No conversions file found.")
        return None
    except json.JSONDecodeError:
        print("conversions.json contains invalid JSON")
        return None

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def get_choice(max_choice):
    while True:
        try:
            choice = int(input("Choose an option:"))
            if 0 < choice <= max_choice:
                return choice
            print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

