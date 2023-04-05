# Define the Dog class
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Define the description() method to print the name and age of the dog
    def description(self):
        print(f"{self.name} is {self.age} years old.")

    # Define the get_info() method to print the coat color of the dog
    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")

# Define the JackRussellTerrier class, which is a child class of Dog
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    # Define a method specific to JackRussellTerrier
    def hunt(self):
        print(f"{self.name} is hunting!")

# Define the Bulldog class, which is a child class of Dog
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    # Define a method specific to Bulldog
    def guard(self):
        print(f"{self.name} is guarding the house!")

# Create objects of Dog, JackRussellTerrier, and Bulldog classes and implement the functionalities
dog = Dog("Buddy", 3, "brown")
dog.description()
dog.get_info()

jrt = JackRussellTerrier("Jack", 2, "white and brown")
jrt.description()
jrt.get_info()
jrt.hunt()

bulldog = Bulldog("Rocky", 4, "white")
bulldog.description()
bulldog.get_info()
bulldog.guard()
