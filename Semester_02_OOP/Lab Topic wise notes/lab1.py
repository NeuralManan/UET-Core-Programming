# import lab2 as module
# from lab2 import *
from lab2 import Circle 

cir1 = Circle(2)
cir1.radius = 10
cir1.area()

#has attribute function
print(hasattr(cir1,"radius"))
print(isinstance(cir1,Circle))

# iin python every variable is just like an object so it will can also e traeted with is instance like upper
name = "pakistan"
found = 1947
print(isinstance(name,str))
print(isinstance(name,int))
print(isinstance(found,int))



























# # Class definition
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart      # Attribute for the real part
#         self.i = imagpart      # Attribute for the imaginary part
#         print("Object created.")

#     def __del__(self):
#         print("Object destroyed.")
#         # Creating an object (instance) of the class
# x = Complex(3.0, -4.5)
# # Printing values
# print(f"Real part is: {x.r}")
# print(f"Imaginary part is: {x.i}")
# x.r = 5.0
# # Printing values
# print(f"Real part is: {x.r}")
# print(f"Imaginary part is: {x.i}")
# print(x.__dict__)
# # Deleting the object
# del x
# # Printing values will result an error bcz x has been deleted
# #print(f"Real part is: {x.r}")
# #print(f"Imaginary part is: {x.i}")
