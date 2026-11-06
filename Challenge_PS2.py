e1 = input("Enter the name of employee 1:")
se1 = float(input("Enter the salary of employee 1:"))

e2 = input("Enter the name of employee 2:")
se2 = float(input("Enter the salary of employee 2:"))

e3 = input("Enter the name of employee 3:")
se3 = float(input("Enter the salary of employee 3:"))

if se1>=se2 and se1>=se3:
    print("Highest salary is:", se1)
    if se1==se2:
        print(f"{e1} and {e2} have same salary")
    elif se1==se3:
        print(f"{e1} and  {e3} have the same salary")
elif se2>=se3 and se2>se1:
    print("highest salary is: ", se2)
    if se2==se3:
            print(f"{e2} and {e3} have same salary")
    elif se2==se1:
        print(f"{e2} and  {e1} have the same salary")
else:
    print("Highest salary is: ", se3)
    if se3==se1:
        print(f"{e3} and {e1} have same salary")
    elif se3==se2:
        print(f"{e3} and  {e2} have the same salary")
    
