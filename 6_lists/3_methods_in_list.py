l = [1, 2, 3, 4, 5, 6]

# 1. append() - Adds an element to the end
l.append(7)
print(l)

# 2. insert() - Inserts 10 at index 0
l.insert(0, 10)
print(l)

# 3. extend() - Adds multiple elements to the end
l.extend([11, 12, 13])
print(l)

# 4. remove() - Removes the first occurrence of 5
l.remove(5)
print(l)

# 5. pop() --> Removes and returns last element / pop(i) - Removes and returns the element at index 3
popped_item = l.pop(3)
print(l)
print("Popped item:", popped_item)

# 6. index() - Finds the index of 6
index = l.index(6)
print("Index of 6:", index)

# 7. count() - Counts occurrences of 5
count_5 = l.count(5)
print("Count of 5:", count_5)

# 8. sort() - Sorts the list in ascending order
l.sort()
print(l)

# 9. reverse() - Reverses the list order
l.reverse()
print(l)

# 10. copy() - Creates a copy of the list
new_list = l.copy()
print("Copied list:", new_list)

# 11. clear() - Removes all elements
l.clear()
print("Cleared list:", l)
