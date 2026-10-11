# print(" example 1: Simple assertion")
# def remaining(capacity, registered):
#     return capacity - registered 

# def test_remaining():
#     assert remaining(20,8) == 13
#     assert remaining(5,5) == 0
# # print(test_remaining())
# test_remaining()

print(" exercise 1: Full capacity matrix")
def validate_capacity (capacity):
    if type(capacity) is int and 1<= capacity<=500 :
        return capacity

def test_capacity():
    assert validate_capacity(5) == 5
    assert validate_capacity(505) == 505

print(test_capacity())

# exampl 2 use this command to run > py -m pytest file_name.py