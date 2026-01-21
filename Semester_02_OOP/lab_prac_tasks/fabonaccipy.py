number = int(input("Enter the length of fabonacci series: "))
num1=0
num2=1
i=0
while i<number:
    i+=1                      #i=1,2,3
    num = num1+num2         #num=1,2,3
    print(num1)        # printed 0,1,1
    num1=num2             # num1=1,1,2
    num2=num              # num2=1,2,3