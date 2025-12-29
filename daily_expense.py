#Daily Expense Data

expense = [120, 250, 80, 400, 150]
days = len(expense)

print("\n" + "=" * 40)
print("DAILY EXPENSE ANALYSIS REPORT")
print("=" * 40)

print("Daily Expence: ")
for i,amount in enumerate(expense, start=1):
    print(f"Day {i} : ₹{amount}")

# Calculate Total and Average Expense

total_expense = 0

for amount in expense:
    total_expense = total_expense + amount


average_expense = total_expense / days 

print("\nExpense Summary: ")
print(f"Total Expense         :   {total_expense}")
print(f"Number Of Days        :   {days}")
print(f"Average Daily Expense :   {average_expense}")

#Find High and Low Expense

highest_expense = expense[0]
lowest_expense = expense[0]

for amount in expense:
    if amount > highest_expense:
        highest_expense = amount
    if amount < lowest_expense:
        lowest_expense = amount

print("\nExpense Extremes: ")
print(f"Highest Expanse :  {highest_expense}")
print(f"Lowest Expanse  :  {lowest_expense}")

#Spending insight based on Avegare 

print("\nSpending Insight: ")
if average_expense > 300:
    print("Expence is High")
elif average_expense >= 150:
    print("Expense is Normal")
else:
    print("Expanse is Low")
