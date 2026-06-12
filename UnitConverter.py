import json
import os

script_dir = os.path.dirname(__file__)
config_file = os.path.join(script_dir, "conversions.json")

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

def calculate_conversion(value, conversion):
   factor = conversion["factor"]
   offset = conversion["offset"]
   return (value * factor) + offset

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
        result = calculate_conversion(value, selected)
        print(f"Result: {result} {selected['unit']}")
    except KeyError:
        print("Error: Missing factor, offset or unit")
    except TypeError:
        print("Error: Factor and offset must be numbers")

def main():
    conversions = load_conversions()

    if conversions is None:
        return

    categories = list(conversions.keys())

    while True:
        print("\nUnit Converter")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category.title()}")
        print(f"{len(categories) + 1}. Quit")

        choice = get_choice(len(categories) + 1)

        if choice == len(categories) + 1:
            print("Goodbye!")
            break

        selected_category = categories[choice - 1]
        run_conversion(selected_category, conversions)

if __name__ == "__main__":
    main()