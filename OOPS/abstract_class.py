# -*- coding: utf-8 -*-
# @File    : abstract_class.py
# @Time    : 5/12/2021 8:10 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# ABC -->Abstract Base Class & abstract methods
# class which has declaration & not implementation

from abc import  ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("Running")

# com = Computer()
# com.process()
com1  = Laptop()
com1.process()