num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))

operation = input('Enter operation (+, -, *, /):')

if operation == '+':
    print('Sum of numbers is: ', num1+num2)
elif operation == '-':
    print('Subtraction of numbers is: ', num1-num2)
elif operation == '*':
    print('Multiplication of numbers is: ', num1*num2)
elif operation == '/':
    print('Division of numbers is: ', num1/num2)
else:
    print('Invalid operation')