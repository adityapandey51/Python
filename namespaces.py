# A namespace in Python is a mapping between variable names and objects. It ensures that variable names are unique and won’t clash with one another. Python organizes namespaces using the LEGB rule, which stands for:

# 1. Local Namespace — Variables defined inside a function
# 2. Enclosing Namespace — Variables in the outer function (when using nested functions)
# 3. Global Namespace — Variables defined at the top level of a script or module.
# 4. Built-in Namespace — Names provided by Python, such as print() and len()

from ast import keyword


x = "global x"  # Global variable

def outer_function():
    x = "enclosing x"  # Enclosing variable
    
    def inner_function():
        x = "local x"  # Local variable
        print("Inner: ", x)  # Accessing local x
    
    inner_function()
    print("Outer: ", x)  # Accessing enclosing x

outer_function()
print("Global: ", x)  # Accessing global x

# Modifying Global Variables
# Sometimes, you may need to modify a global variable inside a function. Python provides the global keyword:
x = "global x"

def modify_global():
    global x
    x = "modified global x"

modify_global()
print("Global: ", x)  # Accessing modified global x

# Similarly, to modify enclosing variables inside nested functions, Python provides the nonlocal keyword:

def outer():
    z = "Hello"
    
    def inner():
        nonlocal z
        z = "Hi"
    
    inner()
    print(z)  # Output: Hi

outer()