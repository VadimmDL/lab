import math

a, b, c = map(float, input("Enter the coefficients for the equation: ").split())

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print("No roots")
