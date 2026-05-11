
# 1. find min max function
def find_min_max(*args):
    return min(args), max(args)

print(find_min_max(3, 7, 1, 9, 2))


# 2. calculate function
def calculate(*args, operation):
    if operation == "sum":
        return sum(args)

    elif operation == "max":
        return max(args)

    elif operation == "min":
        return min(args)

    elif operation == "mult":
        result = 1
        for num in args:
            result *= num
        return result

    else:
        return "Invalid operation"



print(calculate(1, 2, 3, 4, operation="sum"))   # 10
print(calculate(1, 2, 3, 4, operation="max"))   # 4
print(calculate(1, 2, 3, 4, operation="min"))   # 1
print(calculate(1, 2, 3, 4, operation="mult"))  # 24


# 3. format_user function
def format_user(first_name, last_name, **kwargs):
    extra = []

    for key, value in kwargs.items():
        extra.append(f"{key}: {value}")

    return f"{first_name} {last_name} | " + ", ".join(extra)


print(format_user("John", "Doe", age=25, job="Developer"))
# John Doe | age: 25, job: Developer


# 4. safe_divide function
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a // b, a % b