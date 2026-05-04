n = int(input("put number: "))

while n > 0:
    print(n)
    n -= 1

print("finished")

#2 Calculating the total

total = 0

while True:
    num = int(input("put in number (0 stop): "))

    if num == 0:
        break

    total += num

print("total is:", total)

#3 Guessing

secret = 7

while True:
    guess = int(input("guess the number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break

#4 String filtering

text = input("put in the text: ")

vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        continue
    print(ch, end="")

#5 range()

# 0-დან 9-მდე
for i in range(10):
    print(i)

print("------")

# 5-დან 15-მდე
for i in range(5, 16):
    print(i)

print("------")

# 0-დან 20-მდე მხოლოდ ლუწები
for i in range(0, 21, 2):
    print(i)

print("------")

# 10-დან 1-მდე (უკუღმა)
for i in range(10, 0, -1):
    print(i)