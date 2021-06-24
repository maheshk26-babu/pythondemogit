# -*- coding: utf-8 -*-
# @File    : ObjectReferences.py
# @Time    : 4/28/2021 3:05 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

class Car:
    def __init__(self, model, price, wheels):
        self.model =  model
        self.price = price
        self.wheels = wheels

car1 = Car("Toyota", 3.5, 4)
print("{}, {}, {}".format(car1.model, car1.price, car1.wheels))

car2 = Car("Honda", 5.5, 4)
print("{}, {}, {}".format(car2.model, car2.price, car2.wheels))

car1 = car2
print("{}, {}, {}".format(car1.model, car1.price, car1.wheels))