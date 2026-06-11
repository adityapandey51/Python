class Atm:

    # constructor --> special finction, also known as magic methods
    # __variblename -> makes the variable private --> the variable is then stored as _className__variableName in the memory (Private variable/method)
    __counter = 1 # This is a static variable --> which means this method belongs to the class and not to any instance of the class which is an object

    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.menu()

    @staticmethod # --> this is the decorator used to indicate that a given method is static
    def get_counter():
        return Atm.__counter # This is a static method which means this method belongs to the class and can be called using Atm.get_counter() --> syntax

    # magic method -> tells how to print the given object
    def __str__(self):
        return 'the pin is - {}\nthe balance is - {}'.format(self.__pin,self.__balance)

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def menu(self):
        number = int(input(
            '''
                Welcome to the ATM. what would you like to do:
                    1. Pin change
                    2. balance check
                    3. withdrawl
                    4. add balance
                Press a digit to start
            '''
        ))

        if number == 1:
            self.change_pin()
        elif number == 2:
            self.balance_check()
        elif number == 3:
            self.withdrawl()
        elif number == 4:
            self.add_balance()
        else:
            exit()

        # self.menu()
    
    def change_pin(self):
        old_pin = input('Enter old pin')

        if old_pin == self.pin:
            new_pin = input('Enter new pin')
            self.__pin = new_pin
            balance = int(input('Enter the balance'))
            self.__balance = balance
        else:
            print('Wrong pin')

    def balance_check(self):
        print(self.__balance)
    
    def withdrawl(self):
        if(self.__balance <= 0):
            print('gareeb')
        else:
            cash = int(input("Enter the amount"))
            if(cash > self.__balance):
                print('aukaat mein reh')
            else:
                self.__balance -= cash
                print('Withdrawl successful')
    
    def add_balance(self):

        cash = int(input('Add cash amount'))

        if(cash<1):
            print('dimaag hila hai kya')
        else:
            self.__balance += cash
            print('Balance added')

# obj = Atm()
# print(obj)

# Encapsulation
#       -> Bundling of data and the methods through which we can access or set them is known as Encapsulation
#       -> Basically giving getters and setters instead of direct data/attributes directly

# Class relationships: 
#       1. Aggregation --> Has a relationship 
#       2. Inheritance --> Is a relationship

# Aggregation:
#       -> when we pass one class as an instance variable of other class then it is known as Aggregation.
#       -> for example

class User: # --> User has an address, this is aggregation

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_address(self):
        print(self.address.get_place(), self.address.get_pin(), self.address.get_state())

class Address:

    def __init__(self, place, pin, state):
        self.__place = place
        self.__pin = pin 
        self.__state = state

    def get_place(self):
        return self.__place
    
    def get_pin(self):
        return self.__pin
    
    def get_state(self):
        return self.__state
    

addr = Address('Hyd', 501401, 'Telangana')
usr = User('Aditya',addr)
usr.display_address()

######################################################################################

# INHERITANCE
#       -> This is class relationship where the child class inherits the following from the parent class
                # 1. Constructor
                # 2. Non private data/attributes
                # 3. Non private methods

# Syntax

class Parent:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Child(Parent):

    def __init__(self, x, y, z):
        super().__init__(x, y) # To call the constructor or any method of the Parent we use the super() method which signifies the parent
        self.z  = z
    
# Inheritance Summary

        # 1. A class can inherit from other class
        # 2. Inheritance increases code reusability
        # 3. Constructors, methods and attributes get inherited to the child class
        # 4. The parent class doesn't has any access to child class
        # 5. Private methods and attributes are not accessible in child class
        # 6. Child class can override the methods and attributes of parent class and this is known as method overriding
        # 7. Super() is used to call the parent class methods from child class

# Types of Inheritance 

#     1. Single inheritance --> one parent and one Child
#     2. MultiLevel inheritance  --> grand fathers and grand sons 
#     3. Hierarchical inheritance --> multiple childs
#     4. Multiple inheritance -->  multiple parents
#     5. Hybrid inheritance --> Mix of inheritances

# POLYMORPHISM
#     --> Can be implemented in python in 3 ways
#             1. Method overriding --> already seen in inheritance
#             2. Method overloading --> not possible in pyton but can use default args to implement this
#             3. Operator overloading --> using magic methods such as __add__, __sub__, etc