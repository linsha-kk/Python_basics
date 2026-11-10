numbers = [12, 45, 23, 89, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
