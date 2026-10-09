print("Exercise 1: Strict Capacity")
value = "say"
valid = type(value) is int and 1<= value <=500
if valid:
    print("valid")
else:
    print("invalid")

print("Exercise 2: Authorization Decision")
role = "organizer"
isOwner = False

if role == "organizer" and isOwner == True:
    print("access granted")
elif role == "participant" and isOwner == True:
    print("access denied")
else:
    print("access denied")

print("Exercise 3: Attendance message")
capacity = 3
count = [2,3,5]
for count in count:
    if count < capacity:
        print(f"{capacity, count} Available")
    elif count == capacity:
        print(f"{capacity, count } Full")
    else:
        print(f"{capacity, count} Invalid")