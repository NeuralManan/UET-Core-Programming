# try:
#     result = 10/0

# except ImportError: #ZeroDivisionError:
#     print("Cannot divide by zero!") 

# print("executed.")



# try: 
#     value = int(input("Enter a number: "))
#     result = 10 / value
#     print(f"result: {result}")
# except Exception:
#     print("Exception raised!") # there may be more than one exceptions or errors by listing them, check from internet
# print(f"result: {result}")    # still codde runs if any error/exception will come 

# print("Error types: ") # there are many types of errors including syntax error(redlines before exectuion) and exception builtin & custom like ZeroDivisionError, IndexError, KeyError are builtin.   run time errors: indentation error(comes after colon usually in code, python checks just first line but all body lines must be indented), type error, value error,attribute error, import error etc.

# 
#  try:
#     result = 10/2
# except ZeroDivisionError:
#     print("Cannot divide by zero!") 
# else:
#     print("Division successful!")
#     print(f"result: {result}")
# finally:
#     print("Execution completed. Cleaning up...")   # finally block will always execute no matter what executes from try or except block but else block will execute only when try block is successful without any error/exception 


#=============================================================================================================================================
#Note! try except is fornon stop execution of code and custom exceptions are for raising our own exceptions when certain conditions are met in the code excluding built in exceptions

# custom exceptions:

# x = -5
# if x < 0:
#     raise ValueError("Negative values are not allowed.")

# class MyCustomError(Exception):
#     pass
# def check_positive(value):
#     if value < 0:
#         raise MyCustomError("Value must be positive.")
    
# try:
#     check_positive(-10)
# except MyCustomError as e:
#     print(f"Custom Exception Caught: {e}")
#=============================================================================================================================================