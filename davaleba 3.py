#1 ასაკის კატეგორიზაცია
age = int(input("put your age: "))

if 0 <= age <= 12:
    print("you are: child")
elif 13 <= age <= 19:
    print("you are: teenager")
elif 20 <= age <= 64:
    print("you are: adult")
elif age >= 65:
    print("you are: old")
else:
    print("wrong age")

#2 score and attendance
score = float(input("your score: "))
attendance = float(input("attendanceattendance (%): "))

if score > 60 and attendance > 75:
    print("passed")
else:
    print("failed")

#3 discount logic

is_student = input("are you student? (yes/no): ")
is_member = input("are you member? (yes/no): ")

if is_student == "yes" and is_member == "yes":
    print("have discount")
elif is_student == "yes" or is_member == "yes":
    print("have discount")
else:
    print("does not have discount")

#4 username check

username = input("put in username: ")

if 3 <= len(username) <= 20 and username.isalnum():
    print("username is valid")
else:
    print("username is invalid")