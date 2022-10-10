
# ******************************
# Make your Code
# ******************************
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

smallestind = numbers.index(min(numbers))

print(numbers[smallestind])
print(numbers)
