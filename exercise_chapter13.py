# print(" example 1: Simple assertion")
# def remaining(capacity, registered):
#     return capacity - registered 

# def test_remaining():
#     assert remaining(20,8) == 13
#     assert remaining(5,5) == 0
# print(test_remaining())
# #test_remaining()

# print(" exercise 1: Full capacity matrix")
# def validate_capacity (capacity):
#     if type(capacity) is int and 1<= capacity<=500 :
#         return capacity

# def test_capacity():
#     assert validate_capacity(5) == 5
#     assert validate_capacity(505) == 505

# print(test_capacity())

# exampl 2 use this command to run > py -m pytest file_name.py
# print("example 2: Parametrized boundaries")
# import pytest

# @pytest.mark.parametrize("value", [1, 500])
# def test_valid_capacity(value):
#     assert type(value) is int and 1<= value <=500

# print("exercise 2: Empty-list regression")
# import pytest
# def total_capacity(value):
#     return sum(value)

# @pytest.mark.parametrize("value, expected", [([], 0),([3, 7], 10), ])


# def test_total_capacity(value, expected):
#     assert total_capacity(value) == expected

# print("example 3: Isolated fixture")
# import pytest 

# @pytest.fixture
# def record():
#     return {"title": "Python", "capacity": 20}

# def test_record_capacity(record):
#     assert record["capacity"] == 20

print("exercise 3: Normalization regression")
import pytest 

def trimming_name(name):
    return name.strip()

def test_trimming_name():
    assert trimming_name(" Ada L.") == "Ada L."

print(trimming_name(" Ada L."))