# -*- coding: utf-8 -*-
# @File    : Bank.py
# @Time    : 4/27/2021 2:32 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

Balance = 1000

def deposit(amount):
    global Balance
    Balance = Balance + amount

def withdraw(amount):
    global Balance
    Balance = Balance - amount

deposit(100)
withdraw(50)
print(Balance)