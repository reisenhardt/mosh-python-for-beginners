numbers = [5, 6, 3, 4, 8, 5, 8, 4, 5, 8, 8, 8]

for item in numbers:
    numbers.count(item)
    if numbers.count(item) > 1:
        print(numbers)
        numbers.remove(item)
print(numbers)