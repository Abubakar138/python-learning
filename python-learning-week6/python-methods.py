# 1. append()
# Description: Adds a single element to the end of the list.
# Syntax: list.append(element)
# Return Type: None
my_list = [1, 2, 3]
my_list.append(4)
print("append:", my_list)  # Output: [1, 2, 3, 4]

# 2. extend()
# Description: Extends the list by appending all elements from an iterable.
# Syntax: list.extend(iterable)
# Return Type: None
my_list.extend([5, 6])
print("extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 3. insert()
# Description: Inserts an element at a specified position.
# Syntax: list.insert(index, element)
# Return Type: None
my_list.insert(2, 'inserted')
print("insert:", my_list)  # Output: [1, 2, 'inserted', 3, 4, 5, 6]

# 4. remove()
# Description: Removes the first occurrence of a specified element.
# Syntax: list.remove(element)
# Return Type: None
my_list.remove('inserted')
print("remove:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 5. pop()
# Description: Removes and returns the element at a specified index.
# Syntax: list.pop([index])
# Return Type: The removed element
popped_element = my_list.pop(3)
print("pop:", my_list, "Popped element:", popped_element)  # Output: [1, 2, 3, 5, 6] Popped element: 4

# 6. clear()
# Description: Removes all elements from the list.
# Syntax: list.clear()
# Return Type: None
my_list.clear()
print("clear:", my_list)  # Output: []

# 7. index()
# Description: Returns the index of the first occurrence of a specified element.
# Syntax: list.index(element, [start, [end]])
# Return Type: Integer
my_list = [1, 2, 3, 4, 2]
index_of_2 = my_list.index(2)
print("index:", index_of_2)  # Output: 1

# 8. count()
# Description: Returns the number of occurrences of a specified element in the list.
# Syntax: list.count(element)
# Return Type: Integer
count_of_2 = my_list.count(2)
print("count:", count_of_2)  # Output: 2

# 9. sort()
# Description: Sorts the elements of the list in ascending order (by default).
# Syntax: list.sort(key=None, reverse=False)
# Return Type: None
my_list = [3, 1, 4, 2]
my_list.sort()
print("sort:", my_list)  # Output: [1, 2, 3, 4]

# 10. reverse()
# Description: Reverses the order of elements in the list.
# Syntax: list.reverse()
# Return Type: None
my_list.reverse()
print("reverse:", my_list)  # Output: [4, 3, 2, 1]

# 11. copy()
# Description: Returns a shallow copy of the list.
# Syntax: list.copy()
# Return Type: A new list
copied_list = my_list.copy()
print("copy:", copied_list)  # Output: [4, 3, 2, 1]