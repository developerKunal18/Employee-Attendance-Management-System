from config import (
    ATTENDANCE_FILE,
    ATTENDANCE_STATUSES,
)
from storage import read_data, write_data, get_next_id
from employee_manager import list_employees
from utils import (
    input_integer,
    input_date,
    current_timestamp,
)


def list_attendance():
    return read_data(ATTENDANCE_FILE)


def get_attendance_record(employee_id, attendance_date):
    for record in list_attendance():
        if (
            record["employee_id"] == employee_id
            and record["date"] == attendance_date
        ):
            return record

    return None


def mark_attendance():
    employees = [
        employee
        for employee in list_employees()
        if employee["active"]
    ]

    if not employees:
        print("No active employees available.")
        return

    print("\n--- Mark Employee Attendance ---")

    attendance_date = input_date()

    print("\nActive employees:")

    for employee in employees:
        print(
            f"ID: {employee['id']} | "
            f"Code: {employee['employee_code']} | "
            f"{employee['name']}"
        )

    employee_id = input_integer("Enter employee ID: ")

    employee = next(
        (item for item in employees if item["id"] == employee_id),
        None,
    )

    if not employee:
        print("Active employee not found.")
        return

    records = list_attendance()

    existing = next(
        (
            record for record in records
            if record["employee_id"] == employee_id
            and record["date"] == attendance_date
        ),
        None,
    )

    if existing:
        print(
            f"Attendance is already marked as "
            f"{existing['status']} for {attendance_date}."
        )
        print("Use Edit Attendance to change this record.")
        return

    print("\nAttendance statuses:")

    for index, status in enumerate(ATTENDANCE_STATUSES, start=1):
        print(f"{index}. {status}")

    choice = input_integer("Choose status number: ")

    if choice > len(ATTENDANCE_STATUSES):
        print("Invalid status selection.")
        return

    status = ATTENDANCE_STATUSES[choice - 1]

    record = {
        "id": get_next_id(records),
        "employee_id": employee["id"],
        "employee_code": employee["employee_code"],
        "employee_name": employee["name"],
        "department": employee["department"],
        "date": attendance_date,
        "status": status,
        "created_at": current_timestamp(),
        "updated_at": current_timestamp(),
    }

    records.append(record)
    write_data(ATTENDANCE_FILE, records)

    print("\nAttendance marked successfully.")
    print(f"Employee : {employee['name']}")
    print(f"Date     : {attendance_date}")
    print(f"Status   : {status}")


def edit_attendance():
    records = list_attendance()

    print("\n--- Edit Attendance ---")

    attendance_date = input_date("Date to edit (YYYY-MM-DD): ")
    employee_id = input_integer("Enter employee ID: ")

    record = next(
        (
            item for item in records
            if item["employee_id"] == employee_id
            and item["date"] == attendance_date
        ),
        None,
    )

    if not record:
        print("No attendance record found for that employee and date.")
        return

    print(f"Employee: {record['employee_name']}")
    print(f"Current status: {record['status']}")

    for index, status in enumerate(ATTENDANCE_STATUSES, start=1):
        print(f"{index}. {status}")

    choice = input_integer("Choose new status: ")

    if choice > len(ATTENDANCE_STATUSES):
        print("Invalid status selection.")
        return

    record["status"] = ATTENDANCE_STATUSES[choice - 1]
    record["updated_at"] = current_timestamp()

    write_data(ATTENDANCE_FILE, records)

    print("Attendance updated successfully.")


def show_daily_attendance():
    attendance_date = input_date(
        "Enter date to view (YYYY-MM-DD), or Enter for today: "
    )

    records = [
        record for record in list_attendance()
        if record["date"] == attendance_date
    ]

    print(f"\n--- Daily Attendance: {attendance_date} ---")

    if not records:
        print("No attendance records found for this date.")
        return

    for record in sorted(records, key=lambda item: item["employee_id"]):
        print(
            f"ID: {record['employee_id']} | "
            f"{record['employee_name']} | "
            f"{record['department']} | "
            f"{record['status']}"
        )

    print(f"\nEmployees with recorded attendance: {len(records)}")
