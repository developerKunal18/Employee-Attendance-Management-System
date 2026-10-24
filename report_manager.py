from datetime import date

from config import ATTENDANCE_CREDIT
from attendance_manager import list_attendance
from employee_manager import list_employees


def attendance_percentage(records):
    """Calculate attendance credit over recorded attendance days."""
    if not records:
        return 0.0

    earned = sum(
        ATTENDANCE_CREDIT[record["status"]]
        for record in records
    )

    return earned / len(records) * 100


def monthly_report():
    print("\n--- Monthly Attendance Report ---")

    month = input(
        "Enter month as YYYY-MM, or press Enter for current month: "
    ).strip()

    if not month:
        month = date.today().strftime("%Y-%m")

    try:
        parsed_month = date.fromisoformat(month + "-01")

        if parsed_month.strftime("%Y-%m") != month:
            raise ValueError

    except ValueError:
        print("Invalid month. Use YYYY-MM, for example 2026-10.")
        return

    employees = list_employees()
    all_records = list_attendance()

    month_records = [
        record for record in all_records
        if record["date"].startswith(month)
    ]

    if not employees:
        print("No employees registered.")
        return

    if not month_records:
        print(f"No attendance records found for {month}.")
        return

    print(f"\nReport month: {month}")
    print("-" * 90)
    print(
        f"{'ID':<5} {'Employee':<24} {'Present':>8} "
        f"{'Absent':>8} {'Leave':>8} {'Half-Day':>9} {'Attendance %':>13}"
    )
    print("-" * 90)

    for employee in sorted(employees, key=lambda item: item["id"]):
        employee_records = [
            record for record in month_records
            if record["employee_id"] == employee["id"]
        ]

        if not employee_records:
            continue

        counts = {
            status: sum(
                1 for record in employee_records
                if record["status"] == status
            )
            for status in ("Present", "Absent", "Leave", "Half-Day")
        }

        percentage = attendance_percentage(employee_records)

        print(
            f"{employee['id']:<5} "
            f"{employee['name'][:23]:<24} "
            f"{counts['Present']:>8} "
            f"{counts['Absent']:>8} "
            f"{counts['Leave']:>8} "
            f"{counts['Half-Day']:>9} "
            f"{percentage:>12.2f}%"
        )

    print("-" * 90)
    print(
        "Attendance % = (Present days + 0.5 × Half-Days) "
        "/ recorded attendance days × 100."
    )
    print("Leave is excluded from attendance credit but included in recorded days.")


def employee_attendance_report():
    employees = list_employees()

    if not employees:
        print("No employees registered.")
        return

    print("\n--- Individual Employee Attendance ---")

    for employee in employees:
        print(
            f"ID: {employee['id']} | "
            f"{employee['employee_code']} | "
            f"{employee['name']}"
        )

    try:
        employee_id = int(input("Enter employee ID: ").strip())
    except ValueError:
        print("Enter a valid employee ID.")
        return

    employee = next(
        (item for item in employees if item["id"] == employee_id),
        None,
    )

    if not employee:
        print("Employee not found.")
        return

    records = [
        record for record in list_attendance()
        if record["employee_id"] == employee_id
    ]

    records.sort(key=lambda item: item["date"])

    print(f"\nAttendance history for {employee['name']}")

    if not records:
        print("No attendance records found.")
        return

    for record in records:
        print(f"{record['date']} | {record['status']}")

    total = len(records)
    present = sum(1 for item in records if item["status"] == "Present")
    absent = sum(1 for item in records if item["status"] == "Absent")
    leave = sum(1 for item in records if item["status"] == "Leave")
    half_day = sum(1 for item in records if item["status"] == "Half-Day")

    print("\nSummary")
    print(f"Recorded days : {total}")
    print(f"Present       : {present}")
    print(f"Absent        : {absent}")
    print(f"Leave         : {leave}")
    print(f"Half-Day      : {half_day}")
    print(f"Attendance %  : {attendance_percentage(records):.2f}%")
