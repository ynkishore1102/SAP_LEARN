num = int(input("Enter any number:"))

if(num > 0):
    print("the number is positive")
    if(num%2 == 0):
        print("The number is even")
    else:
        print("the number is odd")
elif(num < 0):
    print("the number is negative")
    if(num%2 == 0):
        print("the number is even")
    else:
        print("the number is odd")
else:
    print("number is zero")
    print("number is even")            

'''
if(num > 0):
    print("the number is positive")
elif(num < 0):
    print("the number is negative")
else:
    print("the number is zero")
if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")
    
'''

