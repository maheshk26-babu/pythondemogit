# -*- coding: utf-8 -*-
# @File    : Constructor_Inheritance.py
# @Time    : 5/12/2021 5:29 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1-A working ")

    def feature2(self):
        print("feature 2 working ")

class B(A):

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("feature 1-B working ")

    def feature4(self):
        print("feature 4 working ")

a1 = B()
