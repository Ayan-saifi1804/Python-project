# Write a program to check if a number is a prime number.


num = int(input("Enter the value: "))

count = 0
for i in range(1,num + 1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("It is a Prime Number.")
else:
    print("It is not a Prime Number.")