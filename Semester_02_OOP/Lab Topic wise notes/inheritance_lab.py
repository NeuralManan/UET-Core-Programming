# multi level inheritence
# ....

#==========================================================================================================


# # multiple inheritence
# class AppleDevice:
#     def device_type(self):
#         print("I am an apple device")

# class Iphone:
#     def model(self):
#         print("I am an iPhone")

# class IPad(Iphone, AppleDevice):
#     def feature(self):
#         print("I am an Ipad")            


# # Demonstration
# iphone = IPad()
# iphone.feature()          # from IPad   
# iphone.model()            # from Iphone
# iphone.device_type()      #inherited from AppleDevice

# example 2

# --- BASE CLASSES (The Building Blocks) ---

# class Communication:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def phone(self, number):
#         return f"📞 Calling {number} from {self.brand} {self.model}..."

# class Camera:
#     def __init__(self, resolution_mp):
#         self.resolution_mp = resolution_mp

#     def take_photo(self):
#         return f"📸 Click! Photo captured at {self.resolution_mp}MP."

# class FitnessTracker:
#     def __init__(self, sensor_count):
#         self.sensor_count = sensor_count

#     def monitor_hr(self):
#         return f"❤️  Monitoring Heart Rate using {self.sensor_count} sensors."


# # --- DERIVED CLASSES (The Products) ---

# class SmartPhone(Communication, Camera):
#     def __init__(self, brand, model, resolution_mp, storage_gb):
#         # 1. Initialize Communication Parent
#         Communication.__init__(self, brand, model)
#         # 2. Initialize Camera Parent
#         Camera.__init__(self, resolution_mp)
#         # 3. Initialize Own Attribute
#         self.storage_gb = storage_gb

#     def stream_video(self):
#         return f"▶️ Streaming video (Storage available: {self.storage_gb}GB)"

# class SmartWatch(Communication, FitnessTracker):
#     def __init__(self, brand, model, sensor_count, battery_life_days):
#         # 1. Initialize Communication Parent
#         Communication.__init__(self, brand, model)
#         # 2. Initialize FitnessTracker Parent
#         FitnessTracker.__init__(self, sensor_count)
#         # 3. Initialize Own Attribute
#         self.battery_life_days = battery_life_days

#     def sync_data(self):
#         return f"🔄 Syncing data to cloud... (Battery life: {self.battery_life_days} days left)"


# # --- TEST CODE ---
# if __name__ == "__main__":
#     print("--- 1. Testing SmartPhone (Communication + Camera) ---")
#     iphone = SmartPhone("Apple", "iPhone 15", resolution_mp=48, storage_gb=256)
    
#     print(iphone.phone("0300-1234567"))    # From Communication
#     print(iphone.take_photo())             # From Camera
#     print(iphone.stream_video())           # Own Method

#     print("\n--- 2. Testing SmartWatch (Communication + Fitness) ---")
#     watch = SmartWatch("Samsung", "Galaxy Watch", sensor_count=5, battery_life_days=2)
    
#     print(watch.phone("0321-7654321"))     # From Communication
#     print(watch.monitor_hr())              # From FitnessTracker
#     print(watch.sync_data())               # Own Method


#===========================================================================================================


# # Hieracrchical
# class AppleDevice:
#     def device_type(self):
#         print("I am an apple device")

# class Iphone(AppleDevice):
#     def model(self):
#         print("I am an iPhone")

# class IPad(AppleDevice):
#     def feature(self):
#         print("I am an Ipad")

# class Camera(AppleDevice):
#     def feature(self):
#         print("I have a camera")                      

# # Demonstration
# iphone = Iphone()
# iPad   = IPad()
# camera = Camera()

# iphone.device_type()          # from device_type() 
# iPad.device_type()            # from device_type() 
# camera.device_type()      #inherited from AppleDevice

# EXAMPLE 2

# # --- 1. Base Class (Parent) ---
# class Person:
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number

#     def display_info(self):
#         return f"Name: {self.name}, ID: {self.id_number}"

# # --- 2. Child Class 1 (Student) ---
# class Student(Person):
#     def __init__(self, name, id_number, major):
#         # Initialize the parent attributes first
#         super().__init__(name, id_number)
#         self.major = major

#     def display_info(self):
#         # Reuse parent logic and add student specifics
#         base_info = super().display_info()
#         return f"{base_info}, Major: {self.major}"

# # --- 3. Child Class 2 (Faculty) ---
# class Faculty(Person):
#     def __init__(self, name, id_number, department):
#         super().__init__(name, id_number)
#         self.department = department

#     def display_info(self):
#         base_info = super().display_info()
#         return f"{base_info}, Department: {self.department}"

#     def assign_course(self, course_name):
#         return f"Confirmation: {self.name} has been assigned to teach {course_name}."

# # --- TEST CODE ---
# if __name__ == "__main__":
#     print("--- 1. Creating Objects ---")
#     s1 = Student("Ali", "S123", "Artificial Intelligence")
#     f1 = Faculty("Dr. Ahmed", "F987", "Computer Science")

#     print("\n--- 2. Testing Student ---")
#     print(s1.display_info()) 
#     # Output: Name: Ali, ID: S123, Major: Artificial Intelligence

#     print("\n--- 3. Testing Faculty ---")
#     print(f1.display_info())
#     # Output: Name: Dr. Ahmed, ID: F987, Department: Computer Science
    
#     print(f1.assign_course("Data Structures"))
#     # Output: Confirmation: Dr. Ahmed has been assigned to teach Data Structures.

#=====================================================================================================================================


# #child has constructor but parent has no
# class Iphone:
#     pass # no constructor

# class IPad(Iphone):
#     def __init__(self, model):
#         self.model = model
#     def feature(self):
#         print("I am an Ipad with model", self.model)

# ipad = IPad("15 Pro max")  
# ipad.feature()




# # only Parent has constructor but child has no
# class Iphone:
#     def __init__(self, model):
#         self.model = model
#     def feature(self):
#         print("I am an Iphone with model", self.model)

# class IPad(Iphone):
#     def __init__(self, model):
#         super().__init__(model)

# ipad = IPad("15 Pro max")  
# ipad.feature()
# print(ipad.model)






# class Iphone:
#     def __init__(self, model):
#         self.model = model
#     def feature(self):
#         print("I am an Iphone with model", self.model)

# class IPad(Iphone):
#     def __init__(self, model, year):
#         #Iphone.__init__(self, model) can be used instead super()
#         super().__init__(model)
#         self.year = year

#     def inyear(self):
#         print(f"I am an Iphone with model {self.model} in year {self.year}")
        

# ipad = IPad("17 pro max", 2025)  
# ipad.inyear()



O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
class A(B,C): pass
print(A.mro())



# O = object
# class X(O): pass
# class Y(O): pass
# class A(X,Y): pass
# class B(Y,X): pass
# class C(A,B): pass
# print(C.mro()) # returns list of classes defined in MRO but here it will give error bcz it does'nt resolve conflict every time



# class A: pass
# class B(A): pass
# class C(A): pass

# # D inherits from B, but ALSO explicitly from A
# class D(B, A): pass 

# class E(C): pass

# # F combines them all
# class F(D, E): pass

# print(F.mro())  #Correct MRO: [F, D, B, E, C, A, object]
