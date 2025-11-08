import os
import json
from datetime import datetime, date
import calendar
import time

path = os.getcwd()
new_path = os.path.join(path, "expenses.json")
log_file = os.path.join(path, "app_log.txt")

# Decorator for logging and timing
def log_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        start_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = func(*args, **kwargs)

        duration = time.perf_counter() - start_time

        with open(log_file, "a") as f:
            f.write(f"{start_dt} - {func.__name__} executed in {duration:.4f}s\n")

        print(func.__name__, "completed in", f"{duration:.4f}s\n")
        return result
    return wrapper


def read_expense_data():
    try:
        with open(new_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        with open(new_path, "w") as file:
            file.write("[]")
        return []


@log_and_time
def add_expenses():
    one_expense = {}

    input_date = input("Enter Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if input_date == "":
        input_date = date.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(input_date, "%Y-%m-%d")
        except:
            print("Invalid date format")
            return

    one_expense["date"] = input_date
    one_expense["category"] = input("Enter Category: ")

    try:
        one_expense["amount"] = float(input("Enter Amount: "))
    except:
        print("Invalid Amount")
        return

    one_expense["description"] = input("Enter description: ")

    expenses = read_expense_data()
    expenses.append(one_expense)

    with open(new_path, "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense added successfully\n")


@log_and_time
def view_expenses():
    data = read_expense_data()

    if not data:
        print("No expense records found\n")
        return

    sorted_data = sorted(data, key=lambda x: x["date"])
    total = 0

    # print header using keys of first record
    for key in sorted_data[0].keys():
        print(key, end="   ")
    print()

    # print values
    for record in sorted_data:
        for value in record.values():
            print(value, end="   ")
        total += record["amount"]
        print()

    print("Total Expenditure:", total, "\n")


@log_and_time
def monthly_report():
    data = read_expense_data()
    expected_month = int(input("Enter the Month (MM): "))
    expected_year = int(input("Enter the Year (YYYY): "))

    month_wise = {}
    total = 0

    for record in data:
        dt = datetime.strptime(record["date"], "%Y-%m-%d")
        if dt.month == expected_month and dt.year == expected_year:
            cat = record["category"]
            amt = record["amount"]
            month_wise[cat] = month_wise.get(cat, 0) + amt
            total += amt

    if not month_wise:
        print("No Data Available\n")
    else:
        print("Monthly Summary for", calendar.month_name[expected_month], expected_year)
        for cat, amt in month_wise.items():
            print(cat, ":", amt)
        print("Total Expenditure:", total, "\n")


print("Smart Expense Tracker")
print("1. Add Expenses")
print("2. View Expenses")
print("3. Monthly Summary")
print("4. Exit\n")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_expenses()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        monthly_report()
    else:
        print("Exiting Program")
        break
