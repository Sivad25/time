import csv
from datetime import datetime
from collections import defaultdict

LOG_FILE = 'task_log.csv'


def get_input(prompt):
    return input(prompt).strip()


def log_task(customer, product, task, start, end, duration):
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            customer,
            product,
            task,
            start.strftime('%Y-%m-%d'),
            start.strftime('%H:%M:%S'),
            end.strftime('%H:%M:%S'),
            f"{duration:.2f}"
        ])


def start_task():
    customer = get_input("Customer name: ")
    product = get_input("Product name: ")
    task = get_input("What are you doing? ")

    start = datetime.now()
    input(f"Started at {start.strftime('%H:%M')}. Press Enter when done...")
    end = datetime.now()
    duration = (end - start).total_seconds() / 60

    log_task(customer, product, task, start, end, duration)
    print(f"Saved: {customer} - {product} - {task} ({duration:.2f} min)")


def show_summary():
    summary = defaultdict(lambda: defaultdict(float))

    try:
        with open(LOG_FILE, 'r') as f:
            for row in csv.reader(f):
                if len(row) < 7:
                    continue
                customer, _, _, date, _, _, mins = row
                summary[date][customer] += float(mins)
    except FileNotFoundError:
        print("No tasks logged yet.")
        return

    for date, customers in sorted(summary.items()):
        print(f"\n{date}")
        for customer, minutes in customers.items():
            print(f"  {customer}: {minutes:.2f} min")

def delete_entry():
    try:
        with open(LOG_FILE, 'r') as f:
            rows = list(csv.reader(f))
    except FileNotFoundError:
        print("No tasks logged yet.")
        return

    if not rows:
        print("No tasks logged yet.")
        return

    # Show entries quickly
    for i, row in enumerate(rows, start=1):
        print(i, row)

    try:
        choice = int(get_input("Number to delete: "))
        if 1 <= choice <= len(rows):
            rows.pop(choice - 1)
            with open(LOG_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print("Deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    options = {
        '1': start_task,
        '2': show_summary,
        '3': exit
    }

    while True:
        print("\n1. Start Task\n2. Show Summary\n3. Exit")
        choice = get_input("Choose: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()
