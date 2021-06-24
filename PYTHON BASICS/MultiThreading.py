# -*- coding: utf-8 -*-
# @File    : MultiThreading.py
# @Time    : 5/13/2021 4:43 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

#by defualt we have main thread--> will print data in sequentailly
# if we want the data should execute in simultaneously/parallely we can use Threads concept
# when we use Thread concept we have to define function name as run which because it internally calls run function

from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

# t1.fun1()
# t2.fun2()

t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()

print("Bye") # main thread will execute this statement