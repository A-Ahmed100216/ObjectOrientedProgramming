#Getters and setters
# Why - Use cases?
# To hide the data - separation of concern
# 2 functions - one to get information and one to set information
# syntax

# create a class called student

# class Student:
#
#     def __init__(self,name,company):
#         self.name=name
#         self.company=company
#
#     def getStudent(self,value):
#         self.__name ## __ are used to hide data
#
#     def setStudent(self,value):
#         self.__name = value
#
# student_object=Student("Mina","Sparta")
# print("Student name is" + student_object.setStudent())

# Iteration 2 -

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