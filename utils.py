from datetime import date, datetime


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_integer(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt).strip())

            if value < minimum:
                print(f"Enter a whole number of at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Enter a valid whole number.")


def input_date(prompt="Enter date (YYYY-MM-DD), or press Enter for today: "):
    while True:
        value = input(prompt).strip()

        if not value:
            return date.today().isoformat()

        try:
            parsed_date = date.fromisoformat(value)

            if parsed_date.isoformat() != value:
                raise ValueError

            return value

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, for example 2026-10-24.")


def current_timestamp():
    return datetime.now().isoformat(timespec="seconds")


def pause():
    input("\nPress Enter to continue...")
