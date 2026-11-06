print("----------GRADING SYSTEM-----------")

name = str(input("Enter the Student Name:"))
rno = str(input("Enter the Student Roll No:"))

print("********The Grading Evaluation*********")

print("Enter the following Details:")
math = int(input("Enter Mathematics Marks:"))
phy  = int(input("Enter Physics Marks:"))
chem = int(input("Enter Chemistry Marks:"))
sans = int(input("Enter Sanskrit Marks:"))
eng = int(input("Enter English Marks:"))

sum = math+phy+chem+sans+eng
avg = (sum)/5

grade = 'NA'

if avg>=90 and avg<100:
    grade = 'A'
elif avg>=75 and avg<=89:
    grade = 'B'
elif avg>=60 and avg<=74:
    grade = 'C'
elif avg>=40 and avg<59:
    grade = 'D'
else:
    grade = 'F(Failed)'
    
    
print(f"RESULT: Student {name} bearing Roll No.{rno} has Total Marks: {sum}, Percentage: {avg}, Grade: {grade}")