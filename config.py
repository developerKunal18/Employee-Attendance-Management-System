from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

EMPLOYEES_FILE = DATA_DIR / "employees.json"
ATTENDANCE_FILE = DATA_DIR / "attendance.json"

ATTENDANCE_STATUSES = [
    "Present",
    "Absent",
    "Leave",
    "Half-Day",
]

# Attendance credit used when calculating attendance percentage.
ATTENDANCE_CREDIT = {
    "Present": 1.0,
    "Absent": 0.0,
    "Leave": 0.0,
    "Half-Day": 0.5,
}
