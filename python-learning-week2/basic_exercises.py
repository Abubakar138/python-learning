# 1. Simple Message
message = "Hello World!"
print(message)

# 2. Simple Messages
message = "Simple Message."
print(message)
message = "Python"
print(message)

# 3. Personal Message
name = "Abubakar"
print(f"Hello {name}, would you like to learn some Python today?")

# 4. Name Cases
name = "Abubakar"
print(name.lower())
print(name.upper())
print(name.title())

# 5. Famous Quote
quote = "We may already be in the middle of a revolution, the consequences of which we cannot yet foresee."
author = "Alan Turing"
print(f"{author} once said, \"{quote}\"")

# 6. Famous Quote 2
famous_person = "Albert Einstein"
message = f"{famous_person} once said, \"We may already be in the middle of a revolution, the consequences of which we cannot yet foresee.\""
print(message)

# 7. Stripping Names
name = "\t  Abubakar  \n"
print(f"Original name with whitespace: '{name}'")
print(f"Left stripped: '{name.lstrip()}'")
print(f"Right stripped: '{name.rstrip()}'")
print(f"Fully stripped: '{name.strip()}'")

# 8. Variable Sum
x, y, z = 5, 10, 15
print(f"Sum of x, y, and z: {x + y + z}")

# 9. Variable Swap
a, b = 5, 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# 10. Favorite Color
favorite_color = "Blue"
print(favorite_color)
favorite_color_new_name = favorite_color
print(favorite_color_new_name)

# 11. Changing Pet Name
pet_name = "Buddy"
print(f"Pet's name: {pet_name}")
pet_name = "Max"
print(f"Pet's new name: {pet_name}")

# 12. Observing Name Error
variable_name = "Sunshine"
print(variable_name)
# print(sunsine)

# 13. Reassigning Score
score = 100
print(f"Initial score: {score}")
score = 200
print(f"Updated score: {score}")

# 14. City Name
city = "New York"
print(f"City name: {city}")

# 15. Title Case Text
text = "python programming"
print(text.title())

# 16. Lowercase Conversion
mixed_case_string = "Python ProGraMMing"
print(mixed_case_string.lower())

# 17. Uppercase Conversion
mixed_case_string = "Python ProGraMMing"
print(mixed_case_string.upper())

# 18. Current Temperature
temperature = 25
print(f"The current temperature is {temperature} degrees.")

# 19. Printing a Poem
poem = """Roses are red,
Violets are blue,
Python is fun,
And so are you."""
print(poem)
