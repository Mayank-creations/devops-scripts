#Making a simple Calculator
print("--DevOps  Calculator--")

num1 = float(input("What is the first number?"))
num2 = float(input("What is the second number?"))
operation = input("What Operation you would choose (+,-,/,*)")

if (operation == '+'):
	print(f"Result : {num1 + num2}")
elif (operation == '-'):
	print(f"Result : {num1 - num2}")
elif (operation == '*'):
	print(f"Result : {num1 * num2}")
elif (operation == '/'):
	print(f"result : {num1 / num2}")
else:
	print("Invalid Operation")
