import random as rm
symbols = "!@#$%^&*()?{}"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
password = upper + lower + number + symbols
length = int(input("Enter the length of the password:"))
output = ''.join(rm.sample(password,length))
print("The password is:", output)
