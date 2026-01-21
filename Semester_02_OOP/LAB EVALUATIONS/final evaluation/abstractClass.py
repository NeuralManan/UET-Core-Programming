# TODO You are required to create an abstract class AbstractSystem. 
# This class should have a public instance attributes named osID.
# This class should have a protected instance attributes named biosID.
# Also, create an abstract method get_identifiers. 
# The abstract method should only have a pass statement.
from abc import ABC, abstractmethod
class AbstractSystem(ABC):
    def __init__(self, osID, biosID):
        self.osID = osID  
        self._biosID = biosID 

    @abstractmethod
    def get_identifiers(self):
        pass


##########################################
# TODO Run test_code.py. You should pass Test # 1.
# TODO Now, go to file sysidentitymanager.py
