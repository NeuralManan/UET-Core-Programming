# TODO
# You are required to create a child class SystemIdentityManager of your abstract class.
# This child class should have a static method confirm_user_age.
# The static method should return True if age is above 18 otherwise it should return False.
# This child class should have two instance attributes named os_serial, and bios_serial.
# TODO
# Read this TODO if your color is Green otherwise move to next TODO.
# This child class should have a third private instance attribute hostname.
# Create property getter/setter for hostname.
# This class should also have a class attribute username. Default value of username should be None.
# Define a class method set_username to set the username.
# TODO Read this TODO if your color is Blue.
# This child class should have a third private instance attribute username.
# Create property getter/setter for username.
# This class should also have a class attribute hostname. Default value of hostname should be None.
# Define a class method set_hostname to set the hostname.
# TODO Now lets forget about color.
# You are required to write your abstract method.
# It should return a dictionary. Your dictionary should have four key,value pairs. keys should be "HostName", "UserName", "OS_SERIAL", "BIOS_SERIAL". Set the values accordingly.
# TODO After completing these tasks, run test_code.py. You should pass following tests.
# Test  # 3 checks your constructor.
# Test  # 4 checks your private attribute.
# Test  # 5 checks Getter.
# Test  # 6 checks Setter.
# Test  # 7 checks classmethod.
# Test  # 8 checks class attribute.
# Test  # 9 checks staticmethod.
# Test  # 10 checks return_identifiers method.


# TODO: Write your code here.
from abstractsysidentity import AbstractSystemIdentity
class SystemIdentityManager(AbstractSystemIdentity):
    hostname = None 
    def __init__(self, name, os_serial, bios_serial):
        self.os_serial = os_serial
        self.bios_serial = bios_serial
        self.__username = name

    @staticmethod
    def confirm_user_age(age):
        if age>18:
            return True
        else:
            return False
        
    @property
    def username(self):
      return self.__username
    
    @username.setter
    def username(self, value):
      self.__username = value

    @classmethod
    def set_hostname(cls, hostname):
        cls.hostname = hostname

    def return_identifiers(self):
        return {
            "HostName": self.hostname,
            "UserName": self.__username,
            "OS_Serial": self.os_serial,
            "BIOS_Serial": self.bios_serial
        }      
    



# TODO go to file inheritance.py
