def is_palindrome(str):
    rev_s = str[::-1]
    if (str == rev_s):
        print("True")
    else :
        print("False")
        
str = input("enter the string: ")
is_palindrome(str)
    
