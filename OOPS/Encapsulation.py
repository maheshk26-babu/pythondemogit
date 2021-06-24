# -*- coding: utf-8 -*-
# @File    : Encapsulation.py
# @Time    : 4/28/2021 10:55 AM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# encapsulation is the packing of data and functions operating on that data into a single component and restricting
# the access to some of the object components. Encapsulation means that the internal representation of an object is generally hidden ' \
# 'from view outside of the object definition

# Private variable
# What if we don’t want to change the scope of the variable outside class?
# To do that, we have to change the scope of the variable from ‘public’ to ‘private’.
# The private variables are represented in python using double underscore __

# class Engine:
#     def __init__(self):
#         self.capacity = 100
#     def start(self):
#         print("Engine starting....")
#
# obj = Engine()
# print(obj.capacity)
# obj.start()

class Engine:
    def __init__(self):
        self.__capacity = 100
    def start(self):
        print("Engine starting....")
    def getCapacity(self):
        self.__capacity
        return  self.__capacity

obj = Engine()
# obj.capacity = 200
obj.__capacity = 200
print(obj.__capacity)
# obj.start()
print(obj.getCapacity())

class Car:
    wheels = None
    obj1 = Engine()
    def start(self):
        self.obj1.start()
    def setCapacity(self, cap):
        self.obj1.__capacity = cap
        return  self.obj1.__capacity
c = Car()
print(c.setCapacity(300))



# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 900
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# c = Computer()
# c.sell()
#
# # change the price
# c.__maxprice = 1000
# c.sell()
#
# # # using setter function
# c.setMaxPrice(2000)
# c.sell()