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

print("numbers", numbers)
print("total", total)
print("count", count)
print("average", average)
print("maximum", max_num)
print("Minimum", min_num)
