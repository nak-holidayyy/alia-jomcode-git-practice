# print("Example 1: Annotated function")
# def remaining(capacity: int, registered: int) -> int:
#     return capacity - registered

# print(remaining(20,8))
# print(remaining.__annotations__)

# print("Exercie 1: Annotated normalizer")
# def normalizer(input: str) -> str:
#     return input.lower()

# print(normalizer("ALIA"))
# print(normalizer.__annotations__)

# print("Example 2: Dataclass record")
# from dataclasses import dataclass
# @dataclass
# class workshop:
#     title: str
#     capacity: int

# workshop = workshop("python", 20)
# print(workshop.title, workshop.capacity)

# print("Exercise 2: Validate record factory")
# from dataclasses import dataclass
# @dataclass
# class workshop:
#     capacity: int

#     def create_workshop(capacity:int):
#         if 1<=capacity<=500:
#             print("accepted")
#         else:
#             print("rejected")

# w1 = create_workshop(500)
# if w1:
#     print(w1.capacity)

# w2 = create_workshop(501)

# print("Example 3: Injected dependency")
# class Calculator:
#     def __init__(self, operation):
#         self.operation = operation

#     def apply(self, value):
#         return self.operation(value)

# def double(value):
#     return value*2

# print(Calculator(double).apply(3))

print("Exercise 3: Composition boundary")
class CatalogueService:
    def __init__(self, workshops):
        self.workshops = workshops

    def get_workshops_ids(self):
        return [workshops["id"] for workshops in self.workshops]

workshops = [
    {"id":"w1", "name":"Python Basics"},
    {"id":"w2", "name":"Web Development"}
]
catalogue = CatalogueService(workshops)
print(catalogue.get_workshops_ids())

empty_catalogue = CatalogueService([])
print(empty_catalogue.get_workshops_ids())