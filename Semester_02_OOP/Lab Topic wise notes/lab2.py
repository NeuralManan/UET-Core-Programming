# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius #/self.radius = int(input("Enter the radius of the circle: "))

#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def radius(self, new_radius):
#         self.__radius = new_radius


#     def area(self):    
#         pi = 3.14
#         print("Area of circle is", pi * (self.__radius) ** 2)

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius #/self.radius = int(input("Enter the radius of the circle: "))

#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def radius(self, new_radius):
#         self.__radius = new_radius


#     def area(self):    
#         pi = 3.14
#         print("Area of circle is", pi * (self.__radius) ** 2)



#mcq:
'''
In the following `Robot` class, a private attribute `__version` is defined. How can this attribute be accessed from outside the class instance `r1`?

python
class Robot:
def __init__(self):
self.__version = "1.0.1"

r1 = Robot()

A) r1.__version
B) r1.get_version() 
C) r1._Robot__version ANSWER: Right answer: Python performs name mangling on attributes starting with `__`, prepending `_ClassName` to the attribute name, making it accessible this way.
D) r1 = Robot()
E) It cannot be accessed from outside the class.
'''



# # how to define and print dictionories
# shop = {"trouser" : 100 , "pent" : 200 , "shirt" : 50}
# print(shop["trouser"])
# print(shop.get("shirt","item not availabe"))
# print("Done")
# print(shop)
# # to convert a dictinary in list
# print(list(shop))
# # to check if a key is present in dictionary or not
# print("pent" in shop)
# print("always" in shop")


