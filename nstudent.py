n = int(input("Enter number of students: "))

total = 0
highest = 0
lowest = 100
pass_count = 0
fail_count = 0
above75 = 0

for i in range(n):

    marks = int(input("Enter marks: "))

    total = total + marks

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

    if marks >= 40:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

    if marks > 75:
        above75 = above75 + 1

average = total / n

print("Average =", average)
print("Highest =", highest)
print("Lowest =", lowest)
print("Passed =", pass_count)
print("Failed =", fail_count)
print("Above 75% =", above75)
