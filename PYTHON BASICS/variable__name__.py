# -*- coding: utf-8 -*-
# @File    : variable__name__.py
# @Time    : 5/12/2021 2:58 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email


from variable2__name__ import *

def fun1():
    add()
    print("From fun1",__name__ )

def fun2():
    print("From fun2", __name__)

def main():
    print("From main", __name__)
    fun1()
    fun2()

main()

