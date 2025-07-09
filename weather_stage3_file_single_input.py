import os
import math

file_path = "input.txt"

if not os.path.exists(file_path):
    print(f"Error: '{file_path}' not found. Please place it in the same folder.")
else:
    with open(file_path, "r") as file:
        line = file.readline()
        a, b, c = map(float, line.split())

    d = b**2 - 4*a*c

    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Roots from file:", root1, root2)
    else:
        print("No real weather roots")
