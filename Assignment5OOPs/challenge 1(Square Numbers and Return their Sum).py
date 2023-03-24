class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        pass
        squared_numbers = [self.x**2, self.y**2, self.z**2]
        return sum(squared_numbers)

sq_sum = Point(1, 3, 5)
print(sq_sum.sqSum()) # Output: 35
