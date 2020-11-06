# Object Oriented Programming in Python
### Objectives
* **Examples**

# Example 1
## 1. Create an animal class
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


## 2. Creating the Reptile class
* This will be the child class
* This class will inherit behaviours and attributes from the parent class, Animal.
* Abstract
## 3. Creating the Snake class 
* This will be a child class of Reptile class. 

## 4. Creating a python class
* This will be a child class of the Snake class 

# __name__ and __main__
These are used to check if the code is run from the current file/directory or a diffrenet one i.e one which may have been imported.
* Can also be used for debugging. 
* We will create 2 files and use __name__ and __main__ in both files and the outcome will show the difference 

# Getters and Setters
## Why - Use cases?
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
As with example 1, we create a class called Student and initialise with the name and company. 

```python
class Student:

    def __init__(self, name, company):
        self.name = name
        self.company = company


    # @property This is a decorator in python which is a callable python object that is used to modify a function or class
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

