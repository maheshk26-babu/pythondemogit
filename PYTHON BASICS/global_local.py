# -*- coding: utf-8 -*-
# @File    : global_local.py
# @Time    : 5/14/2021 10:22 AM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

a = 10


def something():
    # global a
    x = globals()['a']
    print("globals function", id(x), x)
    a = 20
    print("inside function", id(a), a)
    globals()['a'] = 30
    print("globals function new value", a, globals()['a'])


something()

print("outside function", id(a), a)
