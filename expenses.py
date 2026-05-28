import json
import os
import sys
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: The data file is corrupted or empty. Starting with an empty list.")
        return []

def save_expenses(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(description, amount):
    expenses = load_expenses()
    new_id = expenses[-1]["id"] + 1 if expenses else 1

    try:
        expense = {
            "id": new_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "description": description,
            "amount": float(amount)  # Explicit conversion to validate input
        }
        expenses.append(expense)
        save_expenses(expenses)
        print(f"Expense added successfully (ID {new_id})")
    except ValueError:
        print("Error: Amount must be a valid number.")

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return []
    
    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10}")
    print("-" * 50)
    for e in expenses:
        print(f"{e['id']:<5} {e['date']:<12} {e['description']:<20} ${e['amount']:<10.2f}")

def delete_expense(expense_id):
    try:
        expenses = load_expenses()
        original_count = len(expenses)

        # Filter out the expense with the given ID
        expenses = [e for e in expenses if e['id'] != int(expense_id)]

        if len(expenses) < original_count:
            save_expenses(expenses)
            print(f"Expense ID {expense_id} deleted.")
        else:
            print(f"Could not find expense with ID {expense_id}.")
    except ValueError:
        print("Error: ID must be a valid integer.")

def show_summary(month=None):
    expenses = load_expenses()
    if month:
        total = sum(e['amount'] for e in expenses if datetime.strptime(e['date'], "%Y-%m-%d").month == month)
        print(f"Summary for month {month}: ${total:.2f}")
    else:
        total = sum(e['amount'] for e in expenses)
        print(f"Total expenses: ${total:.2f}")

# --- Command Line Interface (CLI) Logic ---

if len(sys.argv) < 2:
    print("\nUsage: python expenses.py [command]")
    print("Commands: add, list, summary, delete")
    sys.exit()

command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 4:
        print("Error: Missing description or amount. Usage: add [description] [amount]")
    else:
        add_expense(sys.argv[2], sys.argv[3])

elif command == "list":
    list_expenses()

elif command == "summary":
    if len(sys.argv) > 2:
        try:
            show_summary(month=int(sys.argv[2]))
        except ValueError:
            print("Error: Month must be a number between 1 and 12.")
        except Exception:
            print("Error: Invalid date format found in records during summary processing.")
    else:
        show_summary()

elif command == "delete":
    if len(sys.argv) < 3:
        print("Error: Please provide the ID to delete.")
    else:
        delete_expense(sys.argv[2])

else:
    print("Unknown command. Try: add, list, summary, or delete.")