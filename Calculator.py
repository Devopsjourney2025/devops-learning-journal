print("Welcome to the Simple Calculator!")
while True:
 num1 = float(input("Enter first number: "))
 num2= float(input("Enter second number: "))
 operation = input("Enter operation (+, -, *, /): ")
 if operation == '+':    
    result = num1 + num2    
 elif operation == '-':
    result = num1 - num2
 elif operation == '*':
    result = num1 * num2    
 elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero."
 else:
    result = "Invalid operator"  
 print("The result is: ", result)
 again=input("do you need operation again? (yes/no): ")
 if again.lower()!= "yes":
    print ("Thank you for using the calculator!")   
    break
