# Exercise 3-1: Names
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(name)

# Exercise 3-2: Greetings
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(f"Hello, {name}! Hope you're doing well.")

# Exercise 3-3: Your Own List
transport_modes = ["Honda motorcycle", "Tesla car", "Yamaha bike"]
for transport in transport_modes:
    print(f"I would like to own a {transport}.")

# Exercise 3-4: Guest List
guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to dinner.")

# Exercise 3-5: Changing Guest List
print(f"Unfortunately, {guests[1]} can't make it.")
guests[1] = "Nikola Tesla"
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Exercise 3-6: More Guests
print("Great news! We found a bigger table.")
guests.insert(0, "Leonardo da Vinci")
guests.insert(2, "Galileo Galilei")
guests.append("Ada Lovelace")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Exercise 3-7: Shrinking Guest List
print("Unfortunately, we can invite only two people for dinner.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, we can't invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Removing remaining guests
del guests[0]
del guests[0]
print(f"Final guest list: {guests}")

# Exercise 3-8: Seeing the World
places = ["Paris", "Tokyo", "New York", "Berlin", "Sydney"]
print("Original list:", places)
print("Alphabetical order:", sorted(places))
print("Still original list:", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Still original list:", places)

places.reverse()
print("Reversed list:", places)
places.reverse()
print("Back to original list:", places)

places.sort()
print("Sorted alphabetically:", places)
places.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places)

# Exercise 3-9: Every Function
things = ["Mount Everest", "Amazon River", "China", "New York", "Python"]
print("Original list:", things)
print("Sorted list:", sorted(things))
things.reverse()
print("Reversed list:", things)
things.append("Java")
print("Appended list:", things)
things.insert(1, "Sahara Desert")
print("List after insert:", things)
things.pop()
print("List after pop:", things)
things.remove("New York")
print("List after removing New York:", things)
print("Final sorted list:", sorted(things))

# Exercise 3-10: Intentional Error
# print(things[10])
