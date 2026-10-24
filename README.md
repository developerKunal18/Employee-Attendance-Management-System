# Employee Attendance Management System

A beginner-friendly Python console application for maintaining employee records, recording daily attendance, and generating monthly attendance reports.

## Features

- Register employees with unique employee codes
- View and search employee records
- Activate or deactivate employees
- Mark attendance as Present, Absent, Leave, or Half-Day
- Prevent duplicate attendance records for an employee on the same date
- Edit previously recorded attendance
- View daily attendance
- Generate monthly attendance summaries
- View individual employee attendance history
- Calculate attendance percentages
- Store records using JSON files

## Technologies Used

- Python
- JSON
- Python standard library

## Project Structure

```text
EmployeeAttendanceManagementSystem/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── employee_manager.py
├── attendance_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    ├── employees.json
    └── attendance.json
```

## Requirements

- Python 3.10 or newer recommended
- Visual Studio Code or another Python editor

No external packages are required.

## Installation

Clone your GitHub repository:

```bash
git clone https://github.com/YOUR_USERNAME/EmployeeAttendanceManagementSystem.git
```

Open the project folder in your terminal.

Start the application:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## How to Use

1. Register employees with unique employee codes.
2. Select Mark Attendance.
3. Choose the date or press Enter to use today's date.
4. Enter the employee ID.
5. Select Present, Absent, Leave, or Half-Day.
6. Use View Daily Attendance to review the records.
7. Use Monthly Attendance Report to summarize attendance for a month.
8. Use Individual Employee Attendance to view a person's history.

## Attendance Percentage

The application calculates attendance percentage as:

Attendance Percentage = (Present Days + 0.5 × Half-Days) / Recorded Attendance Days × 100

For example, if an employee has 18 Present days, 2 Half-Days, and 2 Absent days:

- Attendance credit = 18 + (2 × 0.5) = 19 days
- Recorded attendance days = 22
- Attendance percentage = 19 / 22 × 100 = 86.36%

Leave days are included in recorded attendance days but receive zero attendance credit in this demonstration. Organizations can change this rule to match their attendance policy.

## Data Storage

The application stores records in:

- `data/employees.json`
- `data/attendance.json`

The program creates these files automatically if they do not exist.

Back up the data folder regularly. Do not manually edit JSON files while the program is running.

## Testing Checklist

- Register two or more employees.
- Try registering a duplicate employee code.
- Mark an employee Present.
- Try marking the same employee twice on the same date.
- Edit an existing attendance record.
- Mark Absent, Leave, and Half-Day statuses.
- View daily attendance for different dates.
- Generate a monthly report.
- View an individual employee's attendance history.
- Deactivate an employee and verify they cannot receive new attendance entries.
- Restart the application and verify that the records persist.

## Limitations

This is an educational console application. It does not include biometric attendance, GPS verification, automatic payroll calculation, login authentication, simultaneous-user support, or production-grade database transactions.

The attendance percentage is based on recorded attendance entries, not an independently calculated official working-day calendar.

## Future Improvements

- Add a graphical interface using Tkinter.
- Import employee records from CSV.
- Export attendance reports to Excel or CSV.
- Generate printable attendance sheets.
- Add leave approval workflows.
- Integrate payroll calculations.
- Add SQLite or MySQL storage.
- Add user login and role-based permissions.

## License

This project is intended for educational and personal practice.
