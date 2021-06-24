# -*- coding: utf-8 -*-
# @File    : Generator.py
# @Time    : 4/29/2021 12:30 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# A generator is a function that returns an object which we can iterate over one value at a time.
# Thus generators allow programmers to make an iterator in a fast, easy, and clean way

#  Generator versus Function
#
# -A generator uses the yield statement to send a value back to the caller whereas a function does it using the return.
# -The generator function can have one or more than one yield call.
# -The yield call pauses the execution and returns an iterator, whereas the return statement is the last one to be executed.
# -The next() method call triggers the execution of the generator function.

def squarenumbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
my_nums = squarenumbers([1, 2, 3])
print(my_nums)

#why do we have to create an empty list? Why do we have to create this complicated code?
# To simplify the things, we use generators.Look at the below code
# empty list & return tyope is removed Also, instead of append method, we are using ‘yield’.

def square_numbers(nums):
    for i in nums:
        yield i*i
my_nums = square_numbers([1, 2, 3])
print(my_nums)

# These generators are a simple way of creating the iterators, like, you see over here.
# It is a function that returns an ‘object’. If you again look at the console o/p,
# it returned us the generator object at a memory location “<generator object squareNumbers at 0x007D6F30>”

# the ‘return’ terminates the function entirely but the ‘yield’ statement first gives us the object & after
# that it continues with successive calls. Thus ‘yield’ does not terminate the function.
# Also, yield will iterate over one value at a time.We have used ‘next’ function. The next() function returns the next item in an iterator.
# The syntax of next() is: next(iterator).
# The next() function parameter 'iterator' retrieves next item from the iterator.

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

for num in my_nums:
    print(num)

list1= [1, 2, 'mahesh']
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))

def gen_func():
    yield 1
    yield 2
    yield 3
values = gen_func()
print(values)
for var in values:
    print(var)