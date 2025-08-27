import os
import json
import csv
import project

TEST_FILE = "test_expenses.json"
CSV_FILE = "test_expenses.csv"


def setup_function():
    """
    Run before each test.
    Override file paths and reset data.
    """
    project.EXPENSES_FILE = TEST_FILE
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    with open(TEST_FILE, "w") as f:
        json.dump([], f)


def teardown_function():
    """
    Run after each test.
    Cleanup test files.
    """
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)


def test_add_expense():
    project.add_expense("Coffee", "Food", 50.0)
    expenses = project.load_expenses()
    assert len(expenses) == 1
    assert expenses[0]["title"] == "Coffee"
    assert expenses[0]["category"] == "Food"
    assert expenses[0]["amount"] == 50.0


def test_search_by_category():
    project.add_expense("Bus Ticket", "Travel", 20.0)
    project.add_expense("Sandwich", "Food", 30.0)
    results = project.search_by_category("Food")
    assert len(results) == 1
    assert results[0]["title"] == "Sandwich"


def test_calculate_total():
    project.add_expense("Pen", "Stationery", 10.0)
    project.add_expense("Book", "Stationery", 40.0)
    total = project.calculate_total()
    assert total == 50.0


def test_monthly_summary():
    # Add two expenses in current month
    project.add_expense("Pizza", "Food", 100.0)
    project.add_expense("Taxi", "Travel", 200.0)

    # Extract current month (YYYY-MM) from first expense
    month = project.load_expenses()[0]["date"][:7]

    summary = project.monthly_summary(month)
    assert summary == 300.0


def test_export_to_csv():
    project.add_expense("Notebook", "Stationery", 60.0)
    project.add_expense("Juice", "Food", 20.0)

    # Export to test CSV file
    expenses = project.load_expenses()
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "category", "amount", "date"])
        writer.writeheader()
        writer.writerows(expenses)

    # Check CSV file created
    assert os.path.exists(CSV_FILE)

    # Read back CSV and check entries
    with open(CSV_FILE, "r") as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 2
        assert reader[0]["title"] == "Notebook"
        assert reader[1]["category"] == "Food"
