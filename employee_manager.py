from config import EMPLOYEES_FILE
from storage import read_data, write_data, get_next_id
from utils import input_non_empty, current_timestamp


def list_employees():
    return read_data(EMPLOYEES_FILE)


def find_employee(employee_id):
    for employee in list_employees():
        if employee["id"] == employee_id:
            return employee

    return None


def find_employee_by_code(employee_code):
    for employee in list_employees():
        if employee["employee_code"].lower() == employee_code.lower():
            return employee

    return None


def add_employee():
    employees = list_employees()

    print("\n--- Register Employee ---")

    employee_code = input_non_empty("Employee code: ").upper()

    if find_employee_by_code(employee_code):
        print("This employee code already exists.")
        return

    name = input_non_empty("Full name: ")
    department = input_non_empty("Department: ")
    phone = input("Phone number (optional): ").strip()
    email = input("Email address (optional): ").strip()

    employee = {
        "id": get_next_id(employees),
        "employee_code": employee_code,
        "name": name,
        "department": department,
        "phone": phone,
        "email": email,
        "active": True,
        "created_at": current_timestamp(),
    }

    employees.append(employee)
    write_data(EMPLOYEES_FILE, employees)

    print(
        f"Employee registered successfully. "
        f"Employee ID: {employee['id']}"
    )


def display_employee(employee):
    print("-" * 45)
    print(f"Employee ID   : {employee['id']}")
    print(f"Employee Code : {employee['employee_code']}")
    print(f"Name          : {employee['name']}")
    print(f"Department    : {employee['department']}")
    print(f"Phone         : {employee.get('phone') or '-'}")
    print(f"Email         : {employee.get('email') or '-'}")
    print(f"Status        : {'Active' if employee['active'] else 'Inactive'}")


def show_employees():
    employees = list_employees()

    print("\n--- Employee List ---")

    if not employees:
        print("No employees registered.")
        return

    for employee in sorted(employees, key=lambda item: item["id"]):
        display_employee(employee)


def search_employees():
    query = input_non_empty(
        "Search by employee name, code, department, or ID: "
    ).lower()

    matches = [
        employee
        for employee in list_employees()
        if query in employee["name"].lower()
        or query in employee["employee_code"].lower()
        or query in employee["department"].lower()
        or query == str(employee["id"])
    ]

    if not matches:
        print("No matching employees found.")
        return

    for employee in matches:
        display_employee(employee)


def change_employee_status():
    employees = list_employees()

    print("\n--- Activate or Deactivate Employee ---")
    employee_id = int(input_non_empty("Enter employee ID: "))

    employee = next(
        (item for item in employees if item["id"] == employee_id),
        None,
    )

    if not employee:
        print("Employee not found.")
        return

    print(f"Employee: {employee['name']}")
    print(f"Current status: {'Active' if employee['active'] else 'Inactive'}")
    print("1. Activate")
    print("2. Deactivate")

    choice = input("Choose an option: ").strip()

    if choice not in ("1", "2"):
        print("Invalid option.")
        return

    employee["active"] = choice == "1"
    employee["updated_at"] = current_timestamp()

    write_data(EMPLOYEES_FILE, employees)

    print("Employee status updated successfully.")
