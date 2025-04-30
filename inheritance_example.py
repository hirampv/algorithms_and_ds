# Base class (also called parent class or superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (also called child class or subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another subclass
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Using the classes
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Rex barks.
print(cat.speak())  # Output: Whiskers meows.
