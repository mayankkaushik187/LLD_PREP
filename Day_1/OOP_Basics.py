class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak():
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self): 
        """ 
        This is polymorphism, 
        we have overridden a method and extended 
        to provide unique behaviour for each subclass
        """
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Jimmy")
cat = Cat("Boba")

print(dog.speak())
print(cat.speak())