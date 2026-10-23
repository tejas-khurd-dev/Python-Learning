t = 10, 2.3, True, 0, None, 2.3

idx = t.index(2.3) # find index of first occurence 2.3 and return it
print(idx)

count = t.count(2.3) # count occurence of value 2.3 and return it
print(count)


# Tuple unpacking
a, b, c, d =(10, 20, 3, 4)
print(a)
print(type(a))

a, b, c, d = 10, 20, 3, 4
print(c)
print(type(a))




a = (1)
print(type(a))

# To create a tuple with one value, add a comma after the value.
# If you don't want to unpack it, assign the tuple to a single variable.
a = (1,)
print(type(a))

a, = (1,)
print(type(a))

# (10) → integer
# (10,) → one-element tuple
# a, = (10,) → unpack the tuple into a
# a = (10,) → store the tuple in a


# a, b = 1, 2, 3, 4 --> ValueError: too many values to unpack (expected 2)