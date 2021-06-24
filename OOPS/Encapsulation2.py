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

class Engine:
    __capacity = None
    def start(self):
        print("Starting engine....")

class Car:
    wheels = None
    E = Engine()
    def __start(self):
        self.E.start()

    def ignition(self):
        self.__start()

    def setCapacity(self, cap):
        self.E.__capacity = cap
        return  self.E.__capacity
c = Car()
# c.__start()
c.ignition()


# abstract methods are basically incomplete until implemented in sub class
# All abstract methods should implement in sub class

from abc import ABC, abstractmethod

class Hospital(ABC):

    @abstractmethod
    def operate(self):
        pass

    @abstractmethod
    def scanning(self):
        pass

    @abstractmethod
    def billing(self):
        pass

#non abstract method
    def registration(self):
        print("OP registration")

class RuralHospital(Hospital):
    def billing(self):
        print("Billing")

    def operate(self):
        print("Operate")

    def scanning(self):
        print("scanning")

obj = RuralHospital()
obj.registration()
obj.billing()