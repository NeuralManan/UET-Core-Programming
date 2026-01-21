# class Student:
#     name = print("WELCOME TO UET")
#     def __init__(self, name,age,marks1, marks2):
#         self.name=name
#         self.__age=age
#         self.marks1=marks1
#         self.marks2 = marks2

#     @property
#     def get(self):
#         get_age = self.__age
#         #print(get_age)    


#      @setter.
#     def set_age(self, new):
#         self.__age = new 
#         print(self.__age)


#     def student_info(self):
#         print(f"name: {self.name}, age: {self.age}, markstotal: {self.marks1+self.marks2}") 


        


# student1 =Student("ajhsn",20,10,30)
# student1.get()
# student1.set_age(50)
# student1.student_info()

# class Circle:
#     pi = 3.14

#     def __init__(self, radius):
#         self.__radius = radius

#     @property
#     def radius(self):
#         try:
#              if self.__radius < 0:
#                  raise ValueError(print("Radius cannot be negative."))
#                  self.__radius = abs(self.__radius)
#         except:  
#             return self.__radius
     
#     @radius.setter
#     def radius(self, value):
#          try:
#              if value < 0:
#                  raise ValueError(print("Radius cannot be negative."))
#                  self.__radius = abs(value)
#          except:
#               self.__radius = value        
#     def area(self):
#         return Circle.pi * (self.__radius ** 2)
    
# cir1 = Circle(-5)
# print(cir1.area())

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    def speak(self):
        return f"{self.name} makes a sound"    

class Human(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 2)
    def speak(self):
        return f"{self.name} says Hello!"
    
animal1 = Animal("Dog", 4)
human1 = Human("Alice")
print(isinstance(human1, Human))  # True
print(isinstance(human1, Animal)) # True









          
    
        