# -*- coding: utf-8 -*-
# @File    : InnerClass.py
# @Time    : 5/12/2021 5:13 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

class Student:

    def __init__(self, name , rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Mahesh', 418)
s1.show()