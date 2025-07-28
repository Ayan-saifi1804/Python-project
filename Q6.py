# Write a program to implement a simple calculator (add, subtract, multiply, divide).

print("1- Addition")
print("2- Subtraction")
print("3- Muiltiplication")
print("4- Division")

option = int(input("Choose an Operator: "))

result = 0
#added optionName to show in result which operation is performed
optionName = ""

if(option in [1,2,3,4]):
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    if(option == 1):
        result = num1 + num2
        optionName = "Addition"
    elif(option == 2):
        result = num1 - num2
        optionName = "Subtraction"
    elif(option == 3):
        result = num1 * num2
        optionName = "Muiltiplication"
    elif(option == 4):
        result = num1 / num2
        optionName = "Division"

else:
    print("Invalid operation entered.")

print("The result of the "+optionName+" operation is {}".format(result))
