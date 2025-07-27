# Write a program to implement a simple calculator (add, subtract, multiply, divide).

print("1- Addition")
print("2- Subtraction")
print("3- Muiltiplication")
print("4- Division")

option = int(input("Choose an Operator: "))

result = 0

if(option in [1,2,3,4]):
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2

else:
    print("Invalid operation entered.")

print("The result of the operation is {}".format(result))