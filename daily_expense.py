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

#Find High and Low Expense

highest_expense = expense[0]
lowest_expense = expense[0]

for amount in expense:
    if amount > highest_expense:
        highest_expense = amount
    if amount < lowest_expense:
        lowest_expense = amount

print("\nExpense Extremes: ")
print("Highest Expanse: ", highest_expense)
print("Lowest Expanse: ", lowest_expense)

#Spending insight based on Avegare 

print("\nSpending Insight: ")
if average_expense > 300:
    print("Expence is High")
elif average_expense >= 150:
    print("Expense is Normal")
else:
    print("Expanse is Low")
