numbers = [1, 334, 56, 3, 45]

max = numbers[0]

for number in numbers:
    if number>max:
        max = number

print(f"Greatest value: {max}")