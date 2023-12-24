import math

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("The equation has no real solutions.")
    elif discriminant == 0:
        root = -b / (2*a)
        print("The equation has one solution:", root)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The equation has two solutions:", root1, "and", root2)

calculate_roots(1, -3, 2)
calculate_roots(1, -2, 1)
calculate_roots(1, 0, -1)