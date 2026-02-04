# #Single or basic inheritance 

# #BASE CLASS

# class Parent: 
#     def __init__(self, name):
#         self.name = name 

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class 
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# #create an instance of child
# child = Child("Alice")
# child.greet()
# child.play()

# --------------------------------------------------------------------------------

# Multilevel Inheritance 

#Base class
# class Grandparent:
#     def __init__(self, name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} tells a story")

# #Intermediate class
# class Parent(Grandparent):

#     def work(self):
#         print(f"{self.name} is working.")

# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# #Create an instance of Child
# child = Child("Charlie")
# child.tell_story()
# child.work()
# child.play()

# --------------------------------------------------------------------------------------------------------------

#Hierarchical Inheritance 

#Base class
# class Parent: 
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# #Derived Class
# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# #Derived Class 2
# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()

# ---------------------------------------------------------------------------------------------------------

# # Multiple Inheritance (Diamond Problem)

# # Common base class
# class A: 
#     def __init__(self, name):
#         self.name = name 
    
#     def greet(self):
#         print(f"Hello from A, {self.name}")

# #Intermediate class 2
# class B(A):
    
#     def greet(self):
#         print(f"Hello from B, {self.name}")
#         super().greet()
    
# #Intermediate class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}")
#         super().greet()
    
# #Derived class
# class D(B,C):

#     def greet(self):
#         print(f"Hello from 0, {self.name}.")
#         super().greet()

# #Create an instance of D
# d = D("Frank")
# d.greet()

# ------------------------------------------------------------------------------------------------

#Hybrid Inheritance

#base class

class Animal: 
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make a sound.")

#Intermediate class 2 (multiple)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")

#intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

#intermediate class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def nocturnal(self):
        print(f"{self.name} is noctural")

#Create an instance of Bat
bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()