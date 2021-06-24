"""
    *args: allow to pass multiple positional arguments to a function
        * --> unpack the number of positional arguments
        args --> arguments packed into a single tuple
    **kwargs: allow to pass multiple keyword arguments to a function
        ** --> unpack the number of keyword arguments
        kwargs --> arguments packed into a single dictionary
these are used when we dont know exact number of arguments to pass to a function
"""


def var_arguments(*args):
    print(type(args), args)


var_arguments(1, 2, 3, 4, 5)
print("********************************")


def var_arguments2(*numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)


var_arguments2(1, 2, 3, 4, 5)
print("********************************")


def var_keywords(**kwargs):
    print(type(kwargs), kwargs)


var_keywords(name="Mahesh", age=30, salary=7.5)
print("********************************")


def var_args_keywords(arg, *args, **kwargs):
    print("standard argument: ", arg)
    print("positional arguments *args: ", args)
    print("keyword arguments **kwargs: ", kwargs)


var_args_keywords(1, 2, 3, 4, 5, name="Mahesh", age=30)
