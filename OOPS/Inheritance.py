# -*- coding: utf-8 -*-
# @File    : Inheritance.py
# @Time    : 4/27/2021 3:25 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# parent class
class Person(object):
    def __init__(self):
        print("Parent class")

    def person_details(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print("Show parent class")

#child class
class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Child class")
    def employee_details(self, employeeId):
        self.employeeId = employeeId
    def show(self):
        super().show()
        print('{} {} {}'.format(self.firstname, self.lastname, self.employeeId))

emp = Employee()
emp.person_details('admin', 'admin')
emp.employee_details(123456)
emp.show()
