def fun():
  print("Hi") # --> print is also a function "inbuilt-function"

fun()


def prt(age, name):
    print(f"{name} is {age} years old")

prt(name="Tejas", age=21)


def sum(a=1, b=5):
    return a + b

print(sum(2, 5))  # 7
print(sum(3))     # 8
print(sum(b=2))   # 3