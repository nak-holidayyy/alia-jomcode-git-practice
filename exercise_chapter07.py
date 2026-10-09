# print("Exercise 1: Indpendent Edit")
# original = ["Python","SQL"]
# copy_list = original.copy()
# copy_list.append("React")
# print(f"original: {original}")
# print(f"copy: {copy_list}")

print("Exercise 2: Safe filter")
list = [0,2,-1,4]
positive_list=[]
for value in list:
    if value > 0:
        positive_list.append(value)
print(f"Positive values: {positive_list}")

print("Exercise 3: Nested copy explaination")
# Demonstrating the problem
original = [[1, 2], [3, 4]]
copied = original.copy()  # Shallow copy!

# Modifying the inner list of copied:
copied[0].append(99)

print("Original:", original)  # [[1, 2, 99], [3, 4]] -> CHANGED!
print("Copied:  ", copied)    # [[1, 2, 99], [3, 4]] -> CHANGED!