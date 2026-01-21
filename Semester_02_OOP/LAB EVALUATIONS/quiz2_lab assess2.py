# class OSProcess:
#     process_count = 0
#     def __init__(self, pid, name = 0):
#         self.pid = pid
#         self.name = name

#     @classmethod
#     def increment_count(cls):
#         cls.process_count += 1
#         return cls.process_count

#     def process_type(self):
#         print("Generic OS proccess")

# class SystemProcess(OSProcess):
#     def __init__(self, pid, name, kernel_mode):
#         super().__init__(pid)
#         self.kernel_mode = kernel_mode

#     def process_type(self):
#         print(f"Kernel-level system process {self.name} times")

# obj1 = SystemProcess(123, True, "Ali")
# print(SystemProcess.increment_count()) 

# obj1.process_type()
# print(f"pid of obj1 is {obj1.pid}.")

# print("-----")


# obj2 = SystemProcess(456, False, "Ali") 
# print(SystemProcess.increment_count())
# obj2.process_type() 
# print(f"pid of obj2 is {obj2.pid}.")  

# print(f"Total Process Count: {SystemProcess.process_count}")                


class OSProcess:
    process_count = 0
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

    @classmethod
    def increment_count(cls):
        cls.process_count += 1
        return cls.process_count

    def process_type(self):
        print("Generic OS proccess")

class SystemProcess(OSProcess):
    def __init__(self, pid, kernel_mode, name):
        OSProcess.__init__(self, pid, name)
        self.kernel_mode = kernel_mode

    def process_type(self):
        print(f"Kernel-level system process completed")

obj1 = SystemProcess(123, True, "Ali")
print(SystemProcess.increment_count()) 
obj1.process_type()
print(f"pid of obj1 is {obj1.pid}.")

print("-----------------------------------------------------------------------------------------")


obj2 = SystemProcess(456, False, "Ali") 
print(SystemProcess.increment_count())
obj2.process_type() 
print(f"pid of obj2 is {obj2.pid}.")  

print(f"Total Process Count: {SystemProcess.process_count}")

   