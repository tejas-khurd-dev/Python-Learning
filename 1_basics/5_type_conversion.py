# Explicit type conversion
a = 5
print(a)

print(f'{float(a)} is a {type(float(a))} \n')

a = float(a)
print(type(a), "\n")

a = str(a)
print(type(a), "\n")

a = bool(a)
print(a)
print(type(a), "\n")

# Falsy values => total (7) = false, 0, 0.0, '',  [], {}, ()
# Rest all are truthy values

a = 0 
a = bool(a)
print(a, "\n")


# Implincit type conversion

a = 15/5
print(a)