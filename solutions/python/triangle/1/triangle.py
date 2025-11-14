def is_valid_triangle(sides):
    """Check if the given sides can form a valid triangle."""
    a, b, c = sorted(sides)  # Sort sides to simplify triangle inequality check
    return all(sides) and (a + b >= c)

def equilateral(sides):
    """Returns True if the triangle is equilateral, otherwise False."""
    return is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    """Returns True if the triangle is isosceles, otherwise False."""
    return is_valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])

def scalene(sides):
    """Returns True if the triangle is scalene, otherwise False."""
    return is_valid_triangle(sides) and len(set(sides)) == 3