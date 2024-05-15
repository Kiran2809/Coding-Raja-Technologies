import os
import json
from datetime import datetime

# Define constants for file paths
DATA_FILE = "budget_data.json"

# Define the data structure for budget tracking
class BudgetTracker:
    def __init__(self):
        # Load data from the file if it exists, otherwise create a new empty list
        self.transactions = self.load_transactions()

    def load_transactions(self):
        # Load transactions from a file, if available
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return []

    def save_transactions(self):
        # Save transactions to the file
        with open(DATA_FILE, 'w') as f:
            json.dump(self.transactions, f, indent=4)

    def add_income(self, category, amount):
        # Add income transaction
        transaction = {
            'type': 'income',
            'category': category,
            'amount': amount,
            'date': str(datetime.now())
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def add_expense(self, category, amount):
        # Add expense transaction
        transaction = {
            'type': 'expense',
            'category': category,
            'amount': amount,
            'date': str(datetime.now())
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def calculate_budget(self):
        # Calculate the budget based on income and expenses
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return income - expenses

    def analyze_expenses(self):
        # Provide insights into expense categories
        expense_categories = {}
        for t in self.transactions:
            if t['type'] == 'expense':
                category = t['category']
                if category in expense_categories:
                    expense_categories[category] += t['amount']
                else:
                    expense_categories[category] = t['amount']
        return expense_categories


# User interface for the console-based application
def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nConsole Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.add_income(category, amount)
            print("Income added.")

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_expense(category, amount)
            print("Expense added.")

        elif choice == "3":
            budget = budget_tracker.calculate_budget()
            print(f"Current budget: {budget}")

        elif choice == "4":
            analysis = budget_tracker.analyze_expenses()
            print("Expense Analysis:")
            for category, amount in analysis.items():
                print(f"{category}: {amount}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option, please try again.")


# Run the application
if __name__ == "__main__":
    main()
