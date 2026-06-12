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

def calculate_conversion(value, formula):
    allowed_names = {"value": value}
    return eval(formula, {"__builtins__": {}}, allowed_names)

def run_conversion(category_name, conversions):
    category = conversions[category_name]
    options = list(category.values())

    print(f"\n{category_name.title()} Conversions")
    for index, conversion in enumerate(options, start=1):
        print(f"{index}. {conversion['label']}")

    choice = get_choice(len(options))
    selected = options[choice - 1]

    value = get_number("Enter value: ")

    try:
        result = calculate_conversion(value, selected["formula"])
        print(f"Result: {result:.2f} {selected['unit']}")
    except Exception:
        print("Error: Could not convert.")

