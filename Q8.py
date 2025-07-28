# Question is Anagram = Reverse Number

num = int(input("Enter the number: "))
rev = 0
temp = num

while temp > 0:
    digit = temp%10
    rev = (rev*10)+digit
    temp //= 10

if rev == num:
    print(num,"is an Anagram")
else:
    print(num,"is not an Anagram")
    