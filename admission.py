maths = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 3

if maths >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
