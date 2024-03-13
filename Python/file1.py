
# name = input("What is your name?\n")  # Input
# print(f"Hello {name}!")  # Formatted Strings
# print("Hello " + name + "!")  # String Concatenation

import math

toPrint = sum(math.factorial(i + 3) / (math.factorial(3) * math.factorial(i)) for i in range(101))
print(f"{toPrint}")

# from math import comb

# total_solutions = 0
# for i in range(101):
#     total_solutions += comb(i + 3, 3)

# print(total_solutions)
from math import comb

solutions_x0y0 = 0
for i in range(101):
    solutions_x0y0 += comb(i + 1, 1)

print("Solutions where x=0, y=0:", solutions_x0y0)

solutions_x1y1 = 0
for i in range(100):
    solutions_x1y1 += comb(i + 1, 1)

print("Solutions where x=1, y=1:", solutions_x1y1)

solutions_x0y1 = 0
for i in range(100):
    solutions_x0y1 += comb(i + 1, 1)

print("Solutions where x=0, y=1:", solutions_x0y1)

solutions_x1y0 = 0
for i in range(99):
    solutions_x1y0 += comb(i + 1, 1)

print("Solutions where x=1, y=0:", solutions_x1y0)
