# print("Example 1: Conversion recovery")
# text = "twenty"

# try:
#     capacity = int(text)
# except ValueError:
#     print("enter a whole number")
# else :
#     print(capacity)

# print("Exercise 1: Integer parser ")
# text = 50
# def parse_capacity(text):
#     value = int(text)
#     if not (1<=value <=500):
#         raise ValueError
#     return value
# try:
#     result = parse_capacity(text)
# except ValueError:
#     print("rejected. enter 1 to 500")
# else :
#     print("accepted")

print("Example 2: Domain Validation ")
def valid_capacity(value):
    if type(value) is not int or not 1<= value <=500:
        raise ValueError("capacity must be integer from 1 to 500")
    return value
print (valid_capacity(520))