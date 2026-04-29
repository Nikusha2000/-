## შექმენი 4 სხვადასხვა ტიპის ცვლადი. თითოეულისთვის
## დაბეჭდე მნიშვნელობაც და მისი ტიპიც type() ფუნქციის
## გამოყენებით. გამოიყენე აღწერითი snake_case სტილის სახელები
#4 სხვადასხვა ტიპის ცვლადი
from operator import truediv

age = 26
height = 1.75
student = True
first_name = "nikoloz"
print(type(age))
print(type(height))
print(type(student))
print(type(first_name))

## 2მომხმარებელს ჰკითხე მისი დაბადების წელი input() ფუნქციის გამოყენებით.
# გადაიყვანე ის int ტიპში, გამოაკელი 2025-ს და დაბეჭდე მისი დაახლოებით ასაკი.


num1 = input('input birthday: ')
num2 = input('input age: ')
print(num1)
print(num2)
print('num1: ', num1)
print('num2: ', num2)
num1 = int(num1)
num2 = int(num2)
print(num2-num1)


# 3. მომხმარებლისგან მიიღე რიცხვი. დაბეჭდე არის თუ არა ის დადებითი,
# უარყოფითი თუ ნული, და ასევე არის თუ არა ლუწი თუ კენტი.
# output მაგალითი: Negative: False Positive: True Zero: False

num = int(input('customer number: '))
print(num)
is_positive = num > 0
print(is_positive)
is_negative = num < 0
print(is_negative)
is_zero = num == 0
print(is_zero)
is_even = num % 2 == 0
print(is_even)





