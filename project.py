import json
import csv
from datetime import datetime


EXPENSES_FILE = "expenses.json"


def main():
    print("=== Daily Expenses Manager ===")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Spent")
        print("5. Monthly Summary")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense_interactive()
        elif choice == "2":
            expenses = load_expenses()
            display_expenses(expenses)
        elif choice == "3":
            category = input("Enter category: ").strip()
            results = search_by_category(category)
            display_expenses(results)
        elif choice == "4":
            total = calculate_total()
            print(f"\n💰 Total Spent: {total}")
        elif choice == "5":
            month = input("Enter month (YYYY-MM): ").strip()
            summary = monthly_summary(month)
            print(f"\n📅 Total spent in {month}: {summary}")
        elif choice == "6":
            export_to_csv()
            print("\n📂 Expenses exported to expenses.csv")
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# ---------------- Core Functions ---------------- #

def add_expense_interactive():
    """Dynamic user input for adding expense."""
    title = input("Enter expense title: ").strip()
    category = input("Enter category : ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount, expense not added.")
        return

    add_expense(title, category, amount)


def add_expense(title: str, category: str, amount: float):
    """Save an expense entry to file."""
    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")


def load_expenses():
    """Load expenses from file."""
    try:
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    """Save expenses to file."""
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def display_expenses(expenses):
    """Display list of expenses."""
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\nExpenses:")
    for e in expenses:
        print(f"- {e['title']} | {e['category']} | {e['amount']} | {e['date']}")


def search_by_category(category: str):
    """Return expenses by category."""
    expenses = load_expenses()
    return [e for e in expenses if e["category"].lower() == category.lower()]


def calculate_total():
    """Calculate total amount spent."""
    expenses = load_expenses()
    return sum(e["amount"] for e in expenses)


# ---------------- New Extra Functions ---------------- #

def monthly_summary(month: str):
    """Calculate total spent in a given month (format YYYY-MM)."""
    expenses = load_expenses()
    total = 0
    for e in expenses:
        if e["date"].startswith(month):
            total += e["amount"]
    return total


def export_to_csv():
    """Export expenses to a CSV file."""
    expenses = load_expenses()
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "category", "amount", "date"])
        writer.writeheader()
        writer.writerows(expenses)
if __name__ == "__main__":
    main()
