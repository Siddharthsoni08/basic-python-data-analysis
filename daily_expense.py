#Daily Expense Data

expense = [120, 250, 80, 400, 150]

print("Daily Expence: ")
print(expense)

# Calculate Total and Average Expense

total_expense = 0

for amount in expense:
    total_expense = total_expense + amount

days = len(expense)

average_expense = total_expense / days 

print("\nExpense Summary: ")
print("Total Expense: ", total_expense)
print("Number Of Days: ", days)
print("Average Daily Expense: ", average_expense)

