# Daily Expenses Manager
#### Video Demo: https://youtu.be/IgqvMpy7Vac
#### Description:

The **Daily Expenses Manager** is my final project for **CS50’s Introduction to Programming with Python (CS50P)**.
This program allows users to record, search, and analyze their daily spending. It is designed to be **interactive, modular, and user-friendly** with persistent storage.

---

## Features

1. **Dynamic Expense Entry**
   - The program guides the user step by step when adding an expense.
   - First, it asks for the **title** (e.g., "Coffee"), then the **category** (e.g., "Food"), and finally the **amount**.
   - This dynamic flow is easier to use compared to asking all details in one line, making it feel like filling a small form interactively.

2. **View Expenses**
   - Displays all expenses stored in the system with their **title, category, amount, and date**.

3. **Search by Category**
   - Users can search for expenses within a specific category (e.g., "Food" or "Travel").
   - The search is case-insensitive for convenience.

4. **Total Spent**
   - Quickly calculates and displays the **total money spent across all categories**.

5. **Monthly Summary (New Feature)**
   - Users can input a month in `YYYY-MM` format (e.g., `2025-08`) and see the **total spent in that month**.
   - Useful for tracking spending habits over time.

6. **Export to CSV (New Feature)**
   - All expenses can be exported into a file called **expenses.csv**.
   - This makes it possible to open the data in **Excel, Google Sheets, or any spreadsheet tool** for further analysis.

7. **Persistent Storage**
   - All expenses are stored in a **JSON file** (`expenses.json`).
   - The data is automatically saved and reloaded whenever the program runs.

---

## Files in This Project

- **project.py**
  Contains the main program and all required functions.
  Functions include:
  - `main()` → Runs the interactive menu.
  - `add_expense_interactive()` → Dynamic user input for adding expenses.
  - `add_expense(title, category, amount)` → Saves expense entry.
  - `load_expenses()` / `save_expenses()` → Handles data persistence.
  - `display_expenses(expenses)` → Nicely formats expense output.
  - `search_by_category(category)` → Returns expenses in a given category.
  - `calculate_total()` → Calculates total money spent.
  - `monthly_summary(month)` → Returns total spent in a given month.
  - `export_to_csv()` → Exports all expenses to a CSV file.

- **test_project.py**
  Contains unit tests for the above functions using `pytest`.
  Tests cover:
  - Adding expenses
  - Searching by category
  - Calculating total
  - Monthly summary
  - CSV export

- **requirements.txt**
  Lists dependencies required for running the project.
  Only `pytest` is included, since the project otherwise relies on Python’s built-in libraries.

- **expenses.json**
  A data file automatically created and maintained by the program to store user expenses.

- **expenses.csv**
  A file generated when the user chooses the CSV export feature.

---

## How to Run

1. Clone or download the project folder.
2. Ensure Python 3 is installed.
3. Run the program:
   ```bash
   python project.py
