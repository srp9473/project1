print("enter num1")
num1=input()
print("enter num2")
num2=input()
try:
    print("The sum of two numbers is:", int(num1)+int(num2))
except Exception as e:
    print(e)
print("This line is very imp.")
print(num1+num2)