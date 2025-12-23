numbers = [10, 20, 30, 40, 50]
total = 0

for n in numbers:
    total += n

count = len(numbers)
average = total/count

max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Numbers", numbers)
print("Total", total)
print("Count", count)
print("Average", average)
print("Maximum", max_num)
print("Minimum", min_num)