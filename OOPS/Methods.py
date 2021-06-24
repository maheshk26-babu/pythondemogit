# -*- coding: utf-8 -*-
# @File    : Methods.py
# @Time    : 5/12/2021 4:35 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# Methods --
#     1. Instance methods --> when we want to work with instance vars
#     2. Class methods--> when we wnat to work with class vars
#     3. Static methods--> nothing to work with class/instance vars & when work with other classes & objects

# self -- instance vars
# cls -- class vars

class Student:

    school = 'CBK'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return  (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):  # getter method or accessor method
        return  self.m1

    def set_m1(self, value):  # setter method or mutator method
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print ("This is student class....")

s1 = Student(21, 32, 45)
s2 = Student(89, 74, 60)

print(s1.avg(), s2.avg())
print(s2.get_m1())

# print(Student.school)
print(Student.getSchool())
Student.info()
