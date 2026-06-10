# not > and > or --> precedence

# logical operator mainly use as connection between comparison operator
print(12 > 0 and  5==5)
print(12 <= 0 and  5==5)
print(True and bool(0))

print(12 <= 0 or  5==5)

print(not 5==5)

print(12 <= 0 and 12 == 4 or  5==5)


print(12 <= 0 or  5!=5, not  6==5)


# logical operator ('and' and 'or') not always give true or false

# and operator
print(3 and 4)      # 4
print(10 and 3)     # 3
print(0 and 4)      # 0
print(3 and 0)      # 0
print('' and 5)     # ''
print(None and 5)   # None
print(None and 0, "\n\n")  # None

# or operator
print(3 or 4)       # 3
print(0 or 4)       # 4
print(0 or 0)       # 0
print(None or 0)    # 0
print(0 or None, "\n\n") # None

# not operator --> always give true or false
print(not 0)      # True
print(not 1)      # False
print(not "")     # True
print(not "hi")   # False
print(not None, "\n\n") # True