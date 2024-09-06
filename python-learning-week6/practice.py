#1 
num1 = int(input('Enter 1st Num: '))
num2 = int(input('Enter 2nd Num: '))

print('Sum of two numbers is: ', num1 + num2)


#2
animal = input('What\'s your favorite animal?')
print(f'My favorite animal is also {animal}!')


#3
temp_degrees_fahrenheit = float(input('Enter temperature in Fahrenheit: '))
degrees_celsius = (temp_degrees_fahrenheit - 32) * 5.0/9.0
print(f'Temperature in Celsius is: {degrees_celsius}c')


#4
side1 = float(input('What is the length of side 1?'))
side2 = float(input('What is the length of side 2?'))
side3 = float(input('What is the length of side 3?'))
print(f"The perimeter of the triangle is: ", side1 + side2 + side3)


#5
square_num = float(input('Type a number to see its square: '))
print(f"{square_num} squared is ", square_num ** square_num)