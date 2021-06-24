"""
    None: is a keyword to represent the absence of value
"""
numbers = [1, 2, 3, 4, 5]
len_num = len(numbers)
print(len_num)
print(min(numbers))
print(max(numbers))

return_num = print(numbers)
print(return_num)

return_list = numbers.append(6)
print(return_list)
print(numbers)
print("********************************")

num1=2
num2=4

def sum_numbers(num1, num2):
    num1 + num2
print (sum_numbers(num1, num2))

def sum_numbers_return(num1, num2):
     return num1 + num2
print (sum_numbers_return(num1, num2))
