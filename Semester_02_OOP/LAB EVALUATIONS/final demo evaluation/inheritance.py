# TODO Remember your season.
# TODO If winter: Create three classes OSModule, HardwareModule, and HybridModule. OSModule and HardwareModule will be children of SystemIdentityManager class that you have already created. HybridModule will be the child of OSModule and HardwareModule. All three class will have a method identify_module that will return class_name-os_serial. Remember os_serial is the attribute from a parent class. For example, for class OSModule, it should return OSModule-os_serial. For class HardwareModule, it should return HardwareModule-os_serial. For class HybridModule, it should return HybridModule-os_serial. Hint: This return involves concatenation of two strings.
# TODO If Summer: Create three classes VMModule, FirmwareModule, and HybridModule. VMModule and FirmwareModule will be children of SystemIdentityManager class that you have already created. HybridModule will be the child of VMModule and FirmwareModule. All three class will have a method identify_module that will return class_name-os_Serial. Remember os_serial is the attribute from a parent class. For example, for class VMModule, it should return VMModule-os_Serial. For class FirmwareModule, it should return FirmwareModule-os_Serial. For class HybridModule, it should return HybridModule-os_Serial. Hint: This return involves concatenation of two strings.
# TODO After creating the classes, you are required to store mro for HybridModule in mro_variable. You need to access mro using builtin mro method.
# TODO You are also required to instantiate HybridModule without writing any constructor for it. Object name should be hybrid_obj.


# TODO write your code here.
from sysidentitymanager import SystemIdentityManager
class OSModule(SystemIdentityManager):
    def identify_module(self):
        return "OSModule-" +self.os_serial
class HardwareModule(SystemIdentityManager):
    def identify_module(self):
         return "Hardware Module-" +self.os_serial
class HybridModule(OSModule, HardwareModule):    
    def identify_module(self):
        return "HybridModule-" +self.os_serial 
mro_variable = HybridModule.mro()
hybrid_obj = HybridModule("01","02","03")


# TODO After completing these tasks, run test_code.py. You should pass following tests.
# Test  # 11 checks your subclasses.
# Test  # 12 checks identify_module.
# Test  # 13 checks instantiation.
# Test  # 14 checks mro.

# TODO Now Go to file exceptionFunction.py

