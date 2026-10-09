# print("Example 1: Return versus Print")
# def remaining(capacity, registered):
#     return capacity - registered

# value = remaining(20, 5) #need to follow the order of the parameter 
# print(value)
# print(remaining(registered=5, capacity=20))

# print("Exercise 1: Remaining Seats function")
# def remaining_seats(capacity, registered):
#     return capacity - registered

# test = remaining_seats(20, 8)
# print(f"Remaining seats if (20, 8): {test}")
# test2 = remaining_seats(5, 5)
# print(f"Remaining seats if (5, 5): {test2}")

# print("Example 2: Default Argument")
# def greeting(name, prefix='hello'):
#     return f"{prefix}, {name}"

# print(greeting("Ada"))
# print(greeting("Ada", "welcome"))

# print("Exercise 2: Normalizer")
# def normalize_email(text):
#     return text.strip().lower()

# test = normalize_email("   ALIA@GMAIL.COM  ")
# print(f"Normalized email: {test}")

# print("Example 3: Safe mutable default")
# def add_title(title, titles=None):
#     if titles is None:
#         titles = []
#     return[*titles, title]

# print(add_title("Python"))
# print(add_title("SQL"))
# print(add_title("React", ["Python"]))
# print(add_title("React", ["SQL"]))
# print(add_title("React"))

# print("Exercise 3: Independent collection")

# def with_registration(ids,participant_id):
#     if participant_id in ids:
#          return ids.copy()
#     return [*ids, participant_id]

# test = with_registration(["p1"], "p2")
# print(f" if ('p1', 'p2'): {test}")
# test2 = with_registration(["p1"], "p1")
# print(f" if ('p1', 'p1'): {test2}")
