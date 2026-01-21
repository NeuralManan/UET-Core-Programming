# TODO
# You are required to create a child class SystemManager of your abstract class.
# This class should have a private instance attribute.
# Create property getter/setter.
# This class should also have a class attribute.

# TODO
# Read this TODO if your color is Blue.
# Define a class method that accepts a value and decrements the class attribute by that value. 
# This child class should have a static method verify_string.
# The static method should check if its argument is a string. If it is not a string, the method should raise a TypeError. Handle that error. If error, return "Input is not a string". Otherwise, return "Input is a string".

# TODO Read this TODO if your color is Green.
# Define a class method increment_hostID that accepts a value and increments the hostID by that value. 
# This child class should have a static method verify_int.
# The static method should check if its argument is an integer. If it is not a integer, the method should raise a ValueError. Handle that error. If error, return the string "Input is not an integer". Otherwise, return the string "Input is an integer".

# TODO Now lets forget about color.
# You are required to write your abstract method.
# It should return a dictionary. Your dictionary should have four key,value pairs. keys should be "hostID", "userID", "osID", "biosID". Set the values accordingly.
from abstractClass import AbstractSystem
class SystemManager(AbstractSystem):
    userID = 100 
    def __init__(self, username, osID, biosID):
        super().__init__(osID, biosID)
        self.__hostID = username


    @property
    def hostID(self):
        return self.__hostID

    @hostID.setter
    def hostID(self, value):
        self.__hostID = value

    @classmethod
    def decrement_userID(cls, value):
        cls.userID -= value

    @staticmethod
    def verify_string(value):
        try:
            if not isinstance(value, str):
                raise TypeError
            return "Input is a string"
        except TypeError:
            return "Input is not a string"

    def get_identifiers(self):
        return {
            "hostID": self.__hostID,
            "userID": SystemManager.userID, 
            "osID": self.osID,
            "biosID": self._biosID
        }

# TODO After completing these tasks, run test_code.py. You should pass following tests.
# Test  # 2 checks your constructor.
# Test  # 3 checks your protected attribute.
# Test  # 4 checks your private attribute.
# Test  # 5 checks Getter.
# Test  # 6 checks Setter.
# Test  # 7 checks classmethod.
# Test  # 8 checks class attribute.
# Test  # 9 checks staticmethod.
# Test  # 10 checks get_identifiers method.
# TODO go to file inheritance.py
