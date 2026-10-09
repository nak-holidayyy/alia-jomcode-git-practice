print("Example 1: type in python)")
capacity = 20
price = 12.5
title = "Python Programming"
is_open = True
cancelled_at = None
print(type(capacity).__name__)
print(type(price).__name__)
print(type(title).__name__)
print(type(is_open).__name__)
print(type(cancelled_at).__name__)
print(is_open, cancelled_at)

print("")
print("Example 2:Seat Arithmetic)")
capacity = 18
registered = 7
remaining = capacity - registered
print(remaining)
print(18 / 4)
print(capacity / 4) #output: 4.5, normal division
print(18 // 4)      #output: 4, floor division
print(18 % 4 )      #output: 2, remainder
print("Exercise 2:Group and Leftovers")
attendees = 23
group_size = 5
groups= attendees // group_size
leftovers = attendees % group_size
print(f"Groups: {groups}, Leftovers: {leftovers}")

print("")
print("Example 3:Precedence and reassignment )")
total = 2+3*4
print(total)
total = (2+3)*4
print(total)
registered = 4
registered += 1
print(registered)
print("Exercise 3:Remaining Seats")
capacity = 24
registered = 9
remaining = capacity - registered
print(f"Remaining Seats: {remaining}")
print(f"remaining seat type is: {type(remaining).__name__}")