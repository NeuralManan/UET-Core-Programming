num= int(input("enter the number = "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = 0
        break
    
if is_prime == True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
  