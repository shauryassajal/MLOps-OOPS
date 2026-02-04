# base class

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound")

# # derived class
# class Dog(Animal):

#     def speak(self):
#         print(f"{self.name} barks.")

# #create an instance of animal
# animal = Animal("Generic Animal") 
# animal.speak()

# dog = Dog("Buddy")
# dog.speak()


#Super keywords

#Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

#Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}.")

# Create an instance of Dog
dog = Dog("Golder Retriever")
dog.speak()