import json
from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            with open('transactions.json', 'r') as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            self.transactions = []

    def save_data(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, type, category, amount):
        transaction = {
            'type': type,
            'category': category,
            'amount': amount,
            'date': str(datetime.now())
        }
        self.transactions.append(transaction)
        self.save_data()

    def calculate_budget(self):
        income = sum(item['amount'] for item in self.transactions if item['type'] == 'income')
        expenses = sum(item['amount'] for item in self.transactions if item['type'] == 'expense')
        return income - expenses

    def expense_analysis(self):
        categories = {}
        for item in self.transactions:
            if item['type'] == 'expense':
                if item['category'] not in categories:
                    categories[item['category']] = 0
                categories[item['category']] += item['amount']
        
        print("Expense Analysis:")
        for category, total in categories.items():
            print(f"Category: {category}, Total Spent: ${total:.2f}")

    def show_transactions(self):
        print("All Transactions:")
        for item in self.transactions:
            print(f"{item['date']} - {item['type'].capitalize()}: {item['category']} - ${item['amount']:.2f}")

def main():
    budget_tracker = BudgetTracker()
    
    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Show All Transactions")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_transaction('expense', category, amount)
        elif choice == '2':
            category = input("Enter income source: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.add_transaction('income', category, amount)
        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == '4':
            budget_tracker.expense_analysis()
        elif choice == '5':
            budget_tracker.show_transactions()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
