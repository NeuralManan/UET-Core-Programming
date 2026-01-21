import myData

username = myData.student_name
hostname = myData.student_fatherName
reg_id = myData.student_registration_number

# TODO: You are not required to write any further code beyond this line. Just run this file. You will get a color, season and shape in the terminal. Note them down. Now move to file abstractClass.py.

os_id = "1234"
bios_id = "7890"
color = "Green" if username.upper().endswith(("A", "E", "I", "O", "U")) else "Blue"
season = "Winter" if sum(int(ch) for ch in reg_id if ch.isdigit()) % 2 else "Summer"
#color = "Green"
#season = "Summer"
if __name__ == "__main__":
    print(f"\n Color is {color}.\n Season is {season}.") #uncomment if color not req
    print("\n----- You need these for sysidentitymanager.py file---\n")
    if color == "Blue":
        priv_attr = "hostID"
        class_attr = "userID"
        class_attr_def_val = 100
        class_method = "decrement_userID"
        print(f" Private Attribute is hostID.\n Class Attribute is userID and default value is 100.\n Class Method is decrement_userID.")
    else:
        priv_attr = "userID"
        class_attr = "hostID"
        class_attr_def_val = 0
        class_method = "increment_hostID"
        
        print(f" Private Attribute is userID.\n Class Attribute is hostID and default value is 0.\n Class Method is increment_hostID.")
    print("\n----- You need these for inheritance.py file---\n")
    if season == "Winter":
        class_A = "VMClass"
        class_B = "ConClass"
        class_C = "MixClass"
        
        print(f" Fav class is SystemIdentityManager. \n Class A is: VMClass. \n Class B is: ConClass. \n Class C is: MixClass")
    else:
        class_A = "OSClass"
        class_B = "FirmClass"
        class_C = "MixClass"
        
        print(f" Fav class is SystemIdentityManager. \n Class A is: OSClass. \n Class B is: FirmClass. \n Class C is: MixClass")
    