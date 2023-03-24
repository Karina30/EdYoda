class Calculator:
    def __init__(self, num1, num2):
        pass
        self.num1 = num1
        self.num2 = num2

    def add(self):
        pass
        return self.num1 + self.num2

    def subtract(self):
        pass    
        return abs(self.num1 - self.num2)
    

    def multiply(self):
        pass
        return self.num1 * self.num2

    def divide(self):
        pass
        return (self.num2 / self.num1)


obj = Calculator(10, 94)

print(obj.add())       
print(obj.subtract())  
print(obj.multiply())  
print(obj.divide())    