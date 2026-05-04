#1 Sum of list elements

numbers = [3, 7, 2, 9, 5]

total = 0
for num in numbers:
    total += num

print("total is", total)

#2 Max and min

numbers = [3, 7, 2, 9, 5]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("maximum:", max_num)
print("minimum:", min_num)

#3 Even and odd numbers

numbers = [3, 7, 2, 9, 5, 8, 4]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("even numbers:", even_numbers)
print("odd numbers:", odd_numbers)


#4 list and tuple

numbers = [3, 7, 2, 9, 5]

numbers_tuple = tuple(numbers)

print("list:", numbers)
print("tuple:", numbers_tuple)

#5 Unique elements

numbers = [3, 7, 2, 7, 9, 3, 5, 2]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("unique elements:", unique_numbers)

