# -*- coding: utf-8 -*-
# @File    : variable__name__.py
# @Time    : 5/12/2021 2:58 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email


def add():
    print("Result 1", __name__)


def sub():
    print("Result 2", __name__)

def main():
    print("Total result", __name__)
    add()
    sub()

# main()
if __name__ == '__main__':
    main()

