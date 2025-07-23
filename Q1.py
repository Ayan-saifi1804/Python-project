# Write a program to check if a string is a palindrome.

text = input("Enter thr value: ")

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
