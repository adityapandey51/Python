# Understanding Decorators in Python:

# A decorator is a function that wraps another function to modify its behaviour 
# without altering its actual code. Decorators are widely used for logging, access control, memoization, 
# and performance optimization.

# Example:

def sanity_check(dataType):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if(type(args[0])==dataType):
                func(*args)
            else:
                raise TypeError('the data type of the argument is wrong')
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

square('hek')

