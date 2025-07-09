import math

# Hardcoded values for a, b, c
a = 1
b = -5
c = 6

# Discriminant
d = b**2 - 4*a*c

# Check if real roots exist
if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots (Weather pattern times):", root1, root2)
else:
    print("No real solutions (unusual weather condition)")
