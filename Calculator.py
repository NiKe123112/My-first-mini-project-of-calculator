num1 = int(input("Enter first number: "))
operation = input("Choose an operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
   print(num1 / num2)
else:
    print("error")
    
  
