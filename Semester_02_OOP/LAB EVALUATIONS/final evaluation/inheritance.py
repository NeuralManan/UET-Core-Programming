
# TODO Create three classes A, B and C. You have their names in your notes. 
# Class A and Class B will be children of your fav class. See your notes to find your fav class. 
# Do not forget to import your fav class. 
# Class C will be the child of Class A and Class B. 
# All three classes will have a method identify_module that will return class_name-private_attribute. Remember you have already defined the private_attribute in the previous file. This task involves string concatenation.
# TODO You are also required to instantiate Class C without writing any constructor for it. Object name should be hybrid_obj.
# 1. Update Import to SystemManager
from sysidentitymanager import SystemManager

# 2. Inherit from SystemManager
class VMClass(SystemManager):
    def identify_module(self):
        return "VMClass-" + self.hostID
    
class ConClass(SystemManager):
    def identify_module(self):
        return "ConClass-" + self.hostID

class MixClass(VMClass, ConClass):
    def identify_module(self):
        return "MixClass-" + self.hostID
   
hybrid_obj = MixClass("Abdul Manan", "1234", "7890")   


# TODO After completing these tasks, run test_code.py. You should pass following tests.
# Test  # 11 checks your subclasses.
# Test  # 12 checks identify_module.
# Test  # 13 checks instantiation.
