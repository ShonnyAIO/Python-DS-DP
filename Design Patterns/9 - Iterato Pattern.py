
"""
def count_to(count):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    yield from numbers[:count]
"""


class Car:
    pass


numbers = [Car(), Car(), Car(), Car()]

#numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight"]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
