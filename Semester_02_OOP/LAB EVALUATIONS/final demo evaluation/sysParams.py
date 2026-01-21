import uuid, subprocess, winreg

# TODO You can see three variables username, hostname and reg_id below. Currently, they have None value. I want username and hostname to be equal to the student_name and student_fathername that you defined in myData.py. I also want reg_id to be equal to student_registration_number that you defined in myData.py. Do not copy and paste data from myData.py. You are required to import those variable and put them here.

username = "None"  # This variable must be equal to student_name.
hostname = "None"  # This variable must be equal to student_fathername.
reg_id = "None"  # This variable must be equal to student_registration_number.
# TODO Write your code here.
from myData import (
    student_name,
    student_fatherName,
    student_registration_number,
)
username = student_name
hostname = student_fatherName
reg_id = student_registration_number

# TODO  Now run test_code.py. You should pass Task # 1.
# TODO: You are not required to write any further code beyond this line. Just run this file. You will get a color, season and shape in the terminal. Note them down. Now move to file abstractsysidentity.py.


def get_bios_serial_windows():
    result = subprocess.check_output(
        ["wmic", "bios", "get", "serialnumber"], universal_newlines=True
    )
    return result.split("\n")[2].strip()


def get_windows_machine_guid():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
    value, _ = winreg.QueryValueEx(key, "MachineGuid")
    return value


deterministic_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, reg_id)
os_id = "03010666061"
bios_id = "10-06-2003"
color = "Green" if username.upper().endswith(("A", "E", "I", "O", "U")) else "Blue"
season = "Winter" if sum(int(ch) for ch in os_id if ch.isdigit()) % 2 else "Summer"
shape = "Square" if sum(int(ch) for ch in bios_id if ch.isdigit()) % 2 else "Triangle"
if __name__ == "__main__":
    print(f"\n Color is {color}.\n Season is {season}. \n Shape is {shape}.")
