from abc import ABC, abstractmethod  
from math import sqrt
class Shape(ABC):
   @abstractmethod
   def area(self):
       pass
   @staticmethod
   def is_positive(value):
       if value > 0:
         return True
       else:
           return False 
       
class Square(Shape):
   def __init__(self, side):
      if self.is_positive(side):
         self.side = side
      else:
          print(f"Error: {side} is invalid. Defaulting to 0.")
          self.side = 0

   def area(self):
       return self.side*self.side
   
   def __add__(self, other):
        """
        Logic: sq1 + sq2
        1. Calculate Area of sq1 + Area of sq2
        2. Find the side length needed for that total area (sqrt)
        3. Create and return a NEW Square object
        """
        total_area = self.area() + other.area()
        new_side = sqrt(total_area)
        return Square(new_side)

    # --- THE FACTORY: Class Method ---
   @classmethod
   def from_area(cls, target_area):
        """
        Logic: Create a Square when you only know the Area.
        1. Calculate side from area.
        2. Return cls(side) -> equivalent to Square(side)
        """
        if cls.is_positive(target_area):
            calculated_side = sqrt(target_area)
            return cls(calculated_side)
        else:
            print("Invalid area.")
            return cls(0)
        

# --- TEST CODE ---
if __name__ == "__main__":
    print("--- 1. Creation & Validation ---")
    s1 = Square(3)  # Area = 9
    s2 = Square(4)  # Area = 16
    print(f"Square 1 Area: {s1.area()}")
    print(f"Square 2 Area: {s2.area()}")

    print("\n--- 2. Operator Overloading (The '+' Logic) ---")
    # This calls s1.__add__(s2)
    s3 = s1 + s2 
    
    # Math check: 9 + 16 = 25. Sqrt(25) = 5.
    print(f"Combined Square Side: {s3.side}") 
    print(f"Combined Square Area: {s3.area()}")

    print("\n--- 3. Class Method (Factory) ---")
    # Creating a square directly from Area 100 (should have side 10)
    s4 = Square.from_area(100)
    print(f"Factory Square Side: {s4.side}")
         

        