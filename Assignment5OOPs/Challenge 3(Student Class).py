class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def getName(self):
        pass
        return self.__name

    def setName(self, name):
        pass
        self.__name = name

    def getRollNumber(self):
        pass
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        pass
        self.__rollNumber = rollNumber

s = Student()
s.setName("Karina Mujawar")
s.setRollNumber("1212")

print(s.getName())        
print(s.getRollNumber())  

