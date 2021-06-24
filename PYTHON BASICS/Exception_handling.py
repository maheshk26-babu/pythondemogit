# -*- coding: utf-8 -*-
# @File    : Exception_handling.py
# @Time    : 5/12/2021 9:43 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

# Errors-->
#     compile time
#     Logical
#     Runtime
import traceback

a = 5
b = 2

try:
    print("Session start...")
    print(a/b)
    k = int(input("enter the number: "))
# except ZeroDivisionError as e:
#     print("zero division error", e)
# except ValueError as e:
#     print("input error", e)
except Exception as e:
    print("Some other error", e)
    traceback.print_exc()

finally:
    print("Session end...")