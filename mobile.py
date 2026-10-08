data = float(input("Enter data used in GB: "))

if data <= 2:
    bill = 100
elif data <= 5:
    bill = 200
elif data <= 10:
    bill = 400
else:
    bill = 600

print("Bill =", bill)
