class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

# Creating an object
my_dog = Dog("Buddy", 3)
my_dog.bark()
