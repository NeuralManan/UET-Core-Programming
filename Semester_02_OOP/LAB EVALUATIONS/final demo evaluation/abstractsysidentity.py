# TODO You are required to create an abstract class AbstractSystemIdentity. Also, create an abstract method return_identifiers. The abstract method should only have a pass statement.
from abc import ABC, abstractmethod

# TODO Write your code here.
class AbstractSystemIdentity(ABC):
    
    @abstractmethod
    def return_identifiers(self):
        pass

# TODO run test_code.py. You should pass Test # 2.
# TODO Now, go to file sysidentitymanager.py
