FILE_NAME = "expenses.txt"


def load_expenses():
    expenses = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                expense = {
                    "date": parts[0],
                    "category": parts[1],
                    "description": parts[2],
                    "amount": float(parts[3])
                }
                expenses.append(expense)
        file.close()
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    file = open(FILE_NAME, "w")
    for expense in expenses:
        line = expense["date"] + "," + expense["category"] + "," + expense["description"] + "," + str(expense["amount"])
        file.write(line + "\n")
    file.close()


def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ").replace(",", " ")
    category = input("Enter category (Food, Transport, Study, Other): ").replace(",", " ")
    description = input("Enter description: ").replace(",", " ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Expense was not added.")
        return
    expense = {"date": date, "category": category, "description": description, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    for number, expense in enumerate(expenses, 1):
        print(number, "|", expense["date"], "|", expense["category"], "|", expense["description"], "|", expense["amount"])


def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print("Total spending:", total)


def category_summary(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    totals = {}
    for expense in expenses:
        category = expense["category"].lower()
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]
    for category in totals:
        print(category.title(), ":", totals[category])


def search_expenses(expenses):
    word = input("Enter a category or description to search: ").lower()
    found = False
    for expense in expenses:
        if word in expense["category"].lower() or word in expense["description"].lower():
            print(expense["date"], "|", expense["category"], "|", expense["description"], "|", expense["amount"])
            found = True
    if not found:
        print("No matching expense found.")


def main():
    expenses = load_expenses()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Spending")
        print("4. Show Spending by Category")
        print("5. Search Expenses")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            search_expenses(expenses)
        elif choice == "6":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


main()