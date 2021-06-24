# -*- coding: utf-8 -*-
# @File    : MethodOverloading.py
# @Time    : 4/29/2021 11:18 AM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# we cannot have the functions having the same name inside a single class.
# So method overloading is not possible in python.

class Study:
    def show_marks(self, marks):
        self.marks = marks
        return marks
    def show_marks(self, marks, percentage):
        self.marks = marks
        self.percentage = percentage
        return marks, percentage

obj = Study()
# obj.marks =50
# print(obj.show_marks(100))
print(obj.show_marks(100, 95)) # Overload methods using latest defined method