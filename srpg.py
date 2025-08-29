import csv
import os
import sys
from datetime import datetime
from collections import defaultdict

LOG_FILE = "task_log.csv"
HEADERS = ["Customer", "Product", "Task", "Date", "Start", "End", "Minutes"]


def get_input(prompt):
    """Safely get user input."""
    return input(prompt).strip()


def ensure_file():
    """Make sure CSV file exists with headers."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)


def log_task(customer, product, task, start, end, duration):
    """Write a new task log entry to CSV."""
    ensure_file()
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                customer,
                product,
                task,
                start.strftime("%Y-%m-%d"),
                start.strftime("%H:%M:%S"),
                end.strftime("%H:%M:%S"),
                f"{duration:.2f}",
            ]
        )


def show_summary():
    """Display total minutes per customer per day."""
    summary = defaultdict(lambda: defaultdict(float))

    try:
        with open(LOG_FILE, "r") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            for row in reader:
                if len(row) < 7:
                    continue
                customer, _, _, date, _, _, mins = row
                summary[date][customer] += float(mins)
    except FileNotFoundError:
        print(" No tasks logged yet.")
        return

    if not summary:
        print(" No tasks logged yet.")
        return

    print("\n Daily Summary")
    for date, customers in sorted(summary.items()):
        print(f"\n{date}")
        for customer, minutes in customers.items():
            hrs, mins = divmod(minutes, 60)
            if hrs >= 1:
                print(f"  {customer}: {int(hrs)}h {int(mins)}m")
            else:
                print(f"  {customer}: {minutes:.2f} min")


def delete_entry():
    """Delete a logged entry by index."""
    try:
        with open(LOG_FILE, "r") as f:
            rows = list(csv.reader(f))
    except FileNotFoundError:
        print(" No tasks logged yet.")
        return

    if len(rows) <= 1:
        print(" No tasks logged yet.")
        return

    headers = rows[0]
    entries = rows[1:]

    print("\n Entries:")
    for i, row in enumerate(entries, start=1):
        print(i, row)

    try:
        choice = int(get_input("Number to delete: "))
        if 1 <= choice <= len(entries):
            deleted = entries.pop(choice - 1)
            with open(LOG_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(entries)
            print(f"✅ Deleted entry: {deleted}")
        else:
            print(" Invalid number.")
    except ValueError:
        print(" Please enter a valid number.")


def start_task():
    """Start and log a new task with timing."""
    customer = get_input("Customer name: ")
    product = get_input("Product name: ")
    task = get_input("Task description: ")

    print(" Press Enter when you finish the task...")
    start = datetime.now()
    input()  # Wait until user presses Enter
    end = datetime.now()

    duration = (end - start).total_seconds() / 60  # in minutes

    log_task(customer, product, task, start, end, duration)
    print(f" Task logged! Duration: {duration:.2f} minutes.")


def main():
    print("\n Welcome to Task Logger!")
    print("Track your time, stay organized, and manage your work better.\n")

    options = {
        "1": start_task,
        "2": show_summary,
        "3": delete_entry,
        "4": sys.exit,
    }

    while True:
        print("\n--- Task Logger ---")
        print("1. Start Task")
        print("2. Show Summary")
        print("3. Delete Entry")
        print("4. Exit")

        choice = get_input("Choose: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print(" Invalid option. Try again.")


if __name__ == "__main__":
    main()
