#Unique values Analyzer 

values = [10, 20, 10, 30, 20, 40, 50, 30]

print("Orignal Values:")
print(values)

unique_values = set(values)

print("\nUnique Values:")
print(unique_values)

#Count Total and Unique values 

total_count = len(values)
unique_values_count = len(unique_values)

print("\nCounts:")
print("Total Count:", total_count)
print("Total Unique Count:", unique_values)

#Find Duplicate Values

duplicate = []

for value in unique_values:
    if values.count(value) > 1:
        duplicate.append(value)

print("\nDuplicate Values")
print(duplicate)