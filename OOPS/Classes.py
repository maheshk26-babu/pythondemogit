# -*- coding: utf-8 -*-
# @File    : Classes.py
# @Time    : 4/27/2021 2:36 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# class - design/blueprint
#         Attributes    &  Behaviour
#             |                 |
#         Variables       Methods(Function)
# object - Instance
# Size of the object  depends on no.of vars & constructor will allocate size to the object
# self --> current instance of the class

class Banks:
    def __init__(self, accountbalance):
        self.accountbalance = accountbalance
        self.creditbalance = 50
        print("init function")

    def deposit(self, deposit):
        self.accountbalance = self.accountbalance + deposit
        print(self.accountbalance)

    def withdraw(self, withdraw):
        self.accountbalance = self.accountbalance - withdraw

    def checkbalance(self):
        print(self.accountbalance)

b1 = Banks(10)
print(b1.accountbalance)
b1.deposit(20)
print(b1.creditbalance)
print(b1.accountbalance)


