class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance

    @property
    def balance(self):
            return self.__balance
    def deposit(self, amount):
            #input_amount = int(input("enter the amount to deposit:"))
            if amount > 0:#if input_amount > 0:
                self.__balance += amount#input_amount
                print(f"for {self._owner}, {self.__balance} Rs amount deposited successfully...!")
            else:
                print(f"Invalid deposit...!")


    @balance.setter
    def balance(self, value):
        # Security logic: only update if value is logical
        if value < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = value
            print(f"Balance manually updated to: {self.__balance}")            

    def withdraw(self, amount):
            #output_amount = int(input("enter the amount to withdraw:"))
            if amount > self.__balance:#if output_amount > self.__balance:
                 print(f"Insufficient funds...!")   
            else:
                self.__balance -= amount
                print(f"for {self._owner}, amount {self.__balance} withdrawn successfully...!")

    def __del__(self):
            print(f"Account for {self._owner} closed.")




# --- WRITE YOUR CLASS HERE ---

# (You write the BankAccount class here)

# -----------------------------


# --- TEST CODE (Do not change this) ---
if __name__ == "__main__":
    print("--- Opening Account ---")
    # 1. Creation
    acc = BankAccount("Ali", 1000)

    # 2. Deposit Check
    acc.deposit(500)  # Should add 500
    acc.deposit(-200) # Should print "Invalid deposit"

    # 3. Withdrawal Check
    acc.withdraw(200) # Should subtract 200
    acc.withdraw(5000) # Should print "Insufficient funds"

    # 4. Security Check
    print(f"Current Balance: {acc.balance}") # Should print 1300
    
    try:
        acc.balance = 50000 # Should trigger an AttributeError (Read-only) if we comment out setter function
    except AttributeError:
        print("Security Test Passed: Cannot set balance directly.")

    # 5. Destructor Check (Will print when program ends)
    print("--- End of Logic ---")


               
               


