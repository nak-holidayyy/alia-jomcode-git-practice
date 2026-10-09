# print("Example 1: Record Lookup")
# workshop = {"id": "w1", "title": "Python", "capacity": 20}
# print(workshop["id"])
# print(workshop.get("venue", "TBC"))
# print("capacity" in workshop)

# print("Exercise 1: Default venue ")
# workshop = {"id": "w1", "title": "Python", "capacity": 20}

# print("Example 2: Duplicate Identifiers")
# participants_ids = ["u2", "u1", "u3", "u2"]
# unique_ids = set(participants_ids)
# print(sorted(unique_ids))
# print("u1" in unique_ids)
# print(unique_ids & {"u1", "u3"})

# print("Exercise 2: Registration uniqueness")
# list = ["p3", "p1", "p3","p2"]
# unique_list = set(list)
# print(sorted(unique_list))
# print("p1" in unique_list)

# print("Example 3: Filter records")
# workshop = [
#     {
#         "id": "w1", 
#         "capacity": 0
#     },
#     {
#         "id": "w2", 
#         "capacity": 5
#     },
#     {
#         "id": "w3", 
#         "capacity": 20
#     }
#     ] #ada 3 library here
# open_ids = [row["id"] for row in workshop if row["capacity"] > 0]
# print(f"Open workshops: {open_ids}")

print("Exercise 3: Aggregate capacities")
workshop = [
    {
        "id": "w1", 
        "capacity": 0
    },
    {
        "id": "w2", 
        "capacity": 5
    },
    {
        "id": "w3", 
        "capacity": 20
    }
    ] 
total_capacity = [row["capacity"] for row in workshop if row["capacity"]>0]
print(f"capacity: {total_capacity}")
print(f"Total capacity: {sum(total_capacity)}")