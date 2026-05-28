📝 Expense Tracker CLI
A simple and powerful personal finance tracker for the terminal, built with Python. This project allows you to record and monitor your expenses using direct commands, saving all information persistently in a JSON file.

✨ Features
CRUD Operations: Create, Read, and Delete expense records securely.

ID Control: Automatic generation of unique and auto-incrementing IDs for each record.

Advanced Filters: View the total historical expense or filter the financial summary by a specific month.

Automatic Dates: Automatic recording of the exact date of each transaction.

No Dependencies: You only need standard Python; it does not require installing complex external libraries.

Fault Tolerance: Built-in defensive system to handle corrupted files or invalid data in the terminal.

🚀 Installation and Use
Clone/Download: Save the expenses.py file in your project folder.

Execution: Abre una terminal en esa carpeta y usa los siguientes comandos:

Available Commands
1. Add an expense
python expenses.py add "Gym Membership" 45.00

2. List all expenses in a table
python expenses.py list

3. View the summary of the total accumulated expense
python expenses.py summary

4. View the summary of expenses filtered by a month (e.g., May)
python expenses.py summary 5

5. Delete a specific expense using its ID
python expenses.py delete 1

🛠️ Technical Highlights
Exception Handling: Try/except blocks that prevent system crashes if the user enters letters in the amounts or non-existent IDs.

Clean Persistence: Use of json.dump with structured indentation to keep the file readable for both the machine and the developer.

Table Formatting: Dynamic alignment of columns in the terminal using Python's native format operators.
