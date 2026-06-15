class MyCustomError(Exception):
    """Exception raised for custom error in the application."""

    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
    
def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    return a / b

try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Caught an error: {e}")
else:
    pass
    # give in some logic which needs to be executed if there is not exception raised
finally:
    pass
    # regardless of if there is exception or not this will be executed