# -*- coding: utf-8 -*-
# @File    : Variables.py
# @Time    : 5/12/2021 4:21 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# Variables -->
#     1. Instance Variables --> define inside __init__ function
#     2. Class(static) Variables--> define outside __init__ function or inside the class

#  namespace --> place where you create and store object/variable
#         1. Class namespace --> store all class vars
#         2. Object namespace --> store all object/instance vars

class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.brand = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels =5
# c1.wheels = 4
# c2.wheels = 3

print(c1.brand, c1.mil, c1.wheels)
print(c2.brand, c2.mil, c2.wheels)