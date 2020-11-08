# Object Oriented Programming in Python
### Objectives
* ***Examples***
* ***\_\_name__ and \_\_main__***
* __*Getters and Setters*__

# Example 1
### 1. Create an animal class
This will be the parent class
```python
class Animal:

    # Initialising the Animal class
    def __init__(self):
        # Creating attributes
        self.alive=True
        self.spine=True
        self.lungs=True
        self.eyes=True

    # Create behaviours as functions
    def breathe(self):
        return "Keep breathing to stay alive"

    def move(self):
        return "Left to right, up and down"

    def eat(self):
        return "Nom, nom, nom"

    def procreate(self):
        return "Find a partner"

# # Instantiate our class i.e create an object
# cat=Animal()
# # Cat as a child of Animal, inherits behaviours and attributes.
# # Abstracted the eat method from out parent class
# print(cat.eat())
```


### 2. Creating the Reptile class
* This will be the child class
* This class will inherit behaviours and attributes from the parent class, Animal. This is achieved using the ```super()``` keyword.
* First we import the class, the syntax is simply ```from <file_name> import <class_name>```
* When creating the class, we pass the Parent class in the arguments. This immediately tells us that Reptile is a child class of Animal.
```python
from animal import Animal

class Reptile(Animal):
```
* Initialize the class and create several attributes. This is followed by the creation of functions.
```python
    # First we initialise
    def __init__(self):
        # the super key word is used to inherit everything from the parent class.
        super().__init__()
        self.cold_blooded = bool
        self.tetrapod = True
        self.heart_chambers = [3,4]
        self.amniotic_eggs = False

    def seek_heat(self):
        return "Cold-blooded"

    def hunt(self):
        return "Hunter"

    def use_venom(self):
        return "Poisonous, be warned"

    def attract_mate_through_scent(self):
        return "Scent of Love"
```


### 3. Creating the Snake class 
* This will be a child class of Reptile class. 
* Once again we must import the parent class, in this case Reptile. 
* This is followed by initialisation wherein we define attributes.
* Subsequently, functions can be defined.
```python
from reptile import Reptile
class Snake(Reptile):

    # Let's initialise the class
    def __init__(self):
        super().__init__()
        self.cold_blooded=True
        self.forked_tongue=True
        self.venom = bool
        self.limbs = False

    # Creating functions for our user Snake class
    def use_tongue_to_smell(self):
        return "I use tongue to taste"
```

### 4. Creating a python class
* This will be a child class of the Snake class 
* The process is the same: import parent, initialise, inherit, attributes, and functions. 
```python
from snake import Snake
class Python(Snake):

    # Initialise the class
    def __init__(self):
        # Define attributes
        super().__init__()
        self.large = True
        self.two_lungs= True
        self.venom = False

    # Define behaviours
    def digest_large_prey(self):
        return "Hungry"

    def constrict(self):
        return "Squeeze the life"

    def climb(self):
        return "How?! I don't have legs"

    def shed_skin(self):
        return "Out with the old ..."
```
### 5. Instantiation
*The classes can all be instantaited. As Python is a child of Snake which is a child of Reptile, which is a child of Animal, Python should have inherited the behaviours and attributes of all the classes. This is shown in the following code:
```python
pip= Python()
# Inherits from Animal
print(pip.eat())
print(pip.breathe())

# Inherits from Reptile
print(pip.use_venom())
print(pip.tetrapod)

# Inherits from Snake
print(pip.forked_tongue)
print(pip.use_tongue_to_smell())

# Inherits from Python
print(pip.two_lungs)
print(pip.shed_skin())
```


# \_\_name__ and \_\_main__
These are used to check if the code is run from the current file/directory or a different one i.e one which may have been imported.
* Can also be used for debugging. 
* We will create 2 files and use \_\_name__ and \_\_main__ in both files and the outcome will show the difference:
```python
print("this is mode 1 --> " + __name__)
```
* The above print statement will return:
 ```
 this is mode 1 --> __main__
```
* This is because \_\_name__ is \_\_main__ as this is the main directory we are using.
* The ```pass``` keyword can be used if we don't want to write anything within the function just yet. It helps you pass with errors. 
```python
def main():
    return "from mode 1 function "
    pass 
```
* An if statement can be used to check whether the code is run from the current file.
```python
if __name__ =="__main__":
    main()
``` 

* In file 2 we demonstrate mode 2. Mode 1 is imported 
```python
import mode1
print("This is mode 2" + __name__)
```

# Getters and Setters
## Use cases?
* To hide the data - separation of concern, and access hidden data.
* 2 functions - one to get information and one to set information.
### Example 1
* Create a class called student and initialise so it can take a student name and the company they work at.

```python
class Student:

     def __init__(self,name,company):
         self.name=name
         self.company=company
```

* We can use the getStudent and setStudent commands. 
* __ are used to hide data. These are called 'dunder' methods i.e double underscores. 
```python
     def getStudent(self,value):
         self.__name ## __ are used to hide data

     def setStudent(self,value):
         self.__name = value
```
* We can instantiate the class, making sure to supply both arguments, student name and the company they work for.

```python
student_object=Student("Tina","Sparta")
print("Student name is" + student_object.setStudent())
```
* However, this print statement will throw an error as the data has been hidden.

### Example 2
* As with example 1, we create a class called Student and initialise with the name and company. 
* However we can use the ```@property```. This is a decorator - a callable python object that is used to modify a function or class.

```python
class Student:

    def __init__(self, name, company):
        self.name = name
        self.company = company

    @property
    def Student(self, value):
        print("This is setter method in student data")
        self.__name  ## __ are used to hide data

    @Student.setter
    def Student(self, value):
        print("Calling @student.student method")
        self.__name = value


student_object = Student("Tina","Sparta")
print("The student's name is " +student_object.name)
print("{} works in {}".format(student_object.name,student_object.company))
```

