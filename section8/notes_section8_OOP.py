#  OOP
#  OOP allows us to create classes and objects. It is a way to organize our code and make it more reusable.
#  A class is a blueprint for creating objects. It defines the properties and methods that an object will have.
#  An object is an instance of a class. It is a specific implementation of the class.

class name_of_class:
    # constructor method
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    # other methods
    def method1(self):
      # code for method1
      pass

    def method2(self):
      # code for method2
      pass


#  In the above code, we have defined a class called name_of_class. The __init__ method is a special method that is called when an object is created. It is used to initialize the properties of the object. The self parameter is a reference to the current instance of the class. It is used to access the properties and methods of the class.

class dog:
    species = "Mammal"  # class variable

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name} and I am a {self.breed}.")

#  In the above code, we have defined a class called dog. The __init__ method initializes the name and breed properties of the dog. The bark method is a simple method that prints "Woof!".
#  We can create an object of the dog class and call its methods.
my_dog = dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
my_dog.bark()  # Output: Woof!
# notice that bark needs to be called with parentheses because it is a method, while name and breed are properties and do not need parentheses.



class circle:
  pi = 3.14  # class variable

  def __init__(self, radius):
    self.radius = radius

  def circumference(self):
    return 2 * self.pi * self.radius
  
  def area(self):
    return self.pi * (self.radius ** 2)
  # return circle.pi * (self.radius ** 2) # this also works because pi is a class variable, but using self.pi is more common and allows for easier access to the variable within the class.
  
my_circle = circle(5)
print(my_circle.area())  # Output: 78.5
print(my_circle.circumference())  # Output: 31.4
print(circle.pi)  # Output: 3.14


# Inheritance
# Inheritance allows us to create a new class that is a modified version of an existing class. The new class is called a child class or subclass, and the existing class is called a parent class or superclass. The child class inherits all the properties and methods of the parent class, and can also have its own properties and methods.

class animal:
    def __init__(self):
       print("Animal created")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class dog(animal):
    def __init__(self):
        super().__init__()  # call the constructor of the parent class
        print("Dog created")
    
    def who_am_i(self):
        print("I am a dog")
my_dog = dog()  # Output: Animal created
                 #         Dog created
my_dog.who_am_i()  # Output: I am a dog
my_dog.eat()  # Output: I am eating


# Polymorphism
# Polymorphism allows us to use the same method name for different classes. The method will behave differently depending on the class that it is called on.

class Dog(animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
    
    def speak(self):
        print("I am a dog")

class Cat(animal):
    def __init__(self):
        super().__init__()
        print("Cat created")
    
    def speak(self):
        print("I am a cat")

my_dog = Dog()  # Output: Animal created
                 #         Dog created
my_cat = Cat()  # Output: Animal created
                 #         Cat created
my_dog.speak()  # Output: I am a dog
my_cat.speak()  # Output: I am a cat
# In the above code, we have defined two classes, Dog and Cat, that both inherit from the Animal class. Both classes have a speak method that behaves differently depending on the class that it is called on. This is an example of polymorphism.



# Special Methods

class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title)
    def __del__(self):
        print(f"{self.title} has been deleted from memory.")
        
b = book("The Great Gatsby", "F. Scott Fitzgerald")
print(b)  # Output: The Great Gatsby by F. Scott Fitzgerald
print(len(b))  # Output: 16
del b  # deletes the object b from memory
