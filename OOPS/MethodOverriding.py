# -*- coding: utf-8 -*-
# @File    : MethodOverriding.py
# @Time    : 4/28/2021 5:11 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# A child class has a function that has the same name but with a different implementation.

class Car:
    def transmission(self):
        print("Manual transmission")


class Toyota(Car):
    def transmission(self):
        print("Automatic transmission")


obj = Toyota()
obj.transmission()


class Students:
    def show_marks(self, marks):
        self.marks = marks
        return marks


class Studentdetails(Students):
    def show_marks(self, marks):
        self.marks = marks
        return marks + 20

# class Studentdetails(Students):
#     pass

# class Studentdetails():
#     pass

obj1 = Studentdetails()
print(obj1.show_marks(100))
