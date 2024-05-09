#Ralph Cyrel B. Ronda
#BSCPE 1-2
#Program #5: Simple App Calculator

while True:
#This will ask the user to input his/her operator
    operator = input("Please enter an operator (+, -, *, /):")
#This will ask the user to input his/her number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
#This will run the program in choose if the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 * num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
    # This will check if the second number is not zero
        if num2 != 0:
            result = num1 / num2
        else:
            print("Division by zero is prohibited")
            continue
    else:
        print("Invalid operator")
        continue 
#This will display the result
#Will ask the user if they want to try again
#Exit the program if the user doesn't want to try again