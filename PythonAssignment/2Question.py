class Shape:
    def __init__(self, sides):
        self.sides = sides


class Triangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def validate_triangle(self):
        # Check if the sum of any two sides is greater than the third side
        a, b, c = self.sides
        if a + b <= c or a + c <= b or b + c <= a:
            return "Invalid triangle"
        else:
            return "Valid triangle"


class Rectangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def validate_rectangle(self):
        # Check if two pairs of sides are equal and in correct order
        sides = sorted(self.sides)
        if sides[0] == sides[1] and sides[2] == sides[3]:
            return "Valid rectangle"
        else:
            return "Invalid rectangle"

# Create a Triangle object
triangle = Triangle([3, 4, 5])

# Call the validate_triangle function
triangle_result = triangle.validate_triangle()

# Print the result
print(triangle_result)

# Create a Rectangle object
rectangle = Rectangle([2, 4, 2, 4])

# Call the validate_rectangle function
rectangle_result = rectangle.validate_rectangle()

# Print the result
print(rectangle_result)
