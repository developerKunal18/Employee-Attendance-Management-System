from storage import initialize_storage

from employee_manager import (
    add_employee,
    show_employees,
    search_employees,
    change_employee_status,
)

from attendance_manager import (
    mark_attendance,
    edit_attendance,
    show_daily_attendance,
)

from report_manager import (
    monthly_report,
    employee_attendance_report,
)

from utils import pause


def display_menu():
    print("\n" + "=" * 48)
    print("    EMPLOYEE ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 48)
    print("1.  Register Employee")
    print("2.  View All Employees")
    print("3.  Search Employees")
    print("4.  Activate or Deactivate Employee")
    print("5.  Mark Attendance")
    print("6.  Edit Attendance")
    print("7.  View Daily Attendance")
    print("8.  Monthly Attendance Report")
    print("9.  Individual Employee Attendance")
    print("0.  Exit")
    print("=" * 48)


def main():
    initialize_storage()

    actions = {
        "1": add_employee,
        "2": show_employees,
        "3": search_employees,
        "4": change_employee_status,
        "5": mark_attendance,
        "6": edit_attendance,
        "7": show_daily_attendance,
        "8": monthly_report,
        "9": employee_attendance_report,
    }

    print("Welcome to the Employee Attendance Management System!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using the application.")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid choice. Please select a valid menu option.")
            pause()
            continue

        try:
            action()
        except (ValueError, OSError, KeyError) as error:
            print(f"\nUnable to complete the operation: {error}")
            print("Check your input and data files, then try again.")

        pause()


if __name__ == "__main__":
    main()
