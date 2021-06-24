# -*- coding: utf-8 -*-
# @File    : Inheritance.py
# @Time    : 4/27/2021 3:25 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# parent class
class SuperClass(object):
    def getValue(self, value):
        self.value = value
        print(self.value)

class SubClass(SuperClass):
    # def __init__(self):
    #     super().__init__()
    #     print("Child class")
    def SecondValue(self):
        print(self.value+5)

class AnotherSubClass(SubClass):
    def ThirdValue(self):
        print(self.value+10)

obj = AnotherSubClass()
obj.getValue(100)
obj.SecondValue()
obj.ThirdValue()
