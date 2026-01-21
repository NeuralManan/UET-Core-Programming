# TODO if shape is Square: Inside the given function, try to call the static function you have created. Pass arg1 to the static function. There will be an exception TypeError if arg1 is string. Handle that exception. If there is no exception, you should make result = "possible". If there is an exception you should make result = "Not possible". At the end (exception or no exception), you should return result.


# TODO if shape is Triangle: Inside the function, create an object of your SystemIdentityManager class and call return_identifiers method. Try to access arg1 key in the dict return by return_identifiers. If key does not exists, there will be an exception KeyError. Handle that exception. If there is no exception, you should make result = "possible". If there is an exception you should make result = "Not possible". At the end (exception or no exception), you should return result.


# TODO Write your code here.
from sysidentitymanager import SystemIdentityManager
def exception_function(arg1):
 object = SystemIdentityManager("01", "02", "03")
 identifier = object.return_identifiers()
 try:
    check = identifier[arg1]
 except KeyError:
    result = "Not Possible"
 else:
    result = "Possible"   
 return result  

# NOTE: After completing, run test_code.py. You should pass Tests # 15 & 16.
# NOTE: END OF ASSIGNMENT
