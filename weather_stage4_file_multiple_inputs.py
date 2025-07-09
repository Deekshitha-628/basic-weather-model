import math

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file, open(output_file, "w") as out:
    for line_num, line in enumerate(file, start=1):
        if not line.strip():
            continue  # Skip blank lines
        try:
            a, b, c = map(float, line.split())
            d = b**2 - 4*a*c
            out.write(f"\nEquation {line_num}: a={a}, b={b}, c={c}\n")
            if d >= 0:
                root1 = (-b + math.sqrt(d)) / (2*a)
                root2 = (-b - math.sqrt(d)) / (2*a)
                result = f"Roots: {root1:.2f}, {root2:.2f}\n"
            else:
                result = "No real roots (weather anomaly)\n"
            out.write(result)
            print(result.strip())  # Also show in terminal
        except ValueError:
            error = f"Invalid data on line {line_num}: {line.strip()}\n"
            out.write(error)
            print(error.strip())
