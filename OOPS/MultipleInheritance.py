# -*- coding: utf-8 -*-
# @File    : Inheritance.py
# @Time    : 4/27/2021 3:25 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# parent class
class Study(object):
    def showMarks(self, marks):
        self.marks = marks
        print(self.marks)

class Sports:
    def showSports(self, sport):
        self.sport = sport
        print(self.sport)

class StudentDetails(Study, Sports):
    def showStudentDetails(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

obj = StudentDetails()
obj.showStudentDetails('Mahesh', 30)
obj.showMarks(100)
obj.showSports('Cricket')
