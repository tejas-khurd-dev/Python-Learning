# Tuples are immutable --> many methods dont work here

t1 = 1,2,3,4,5

t2 = (10,20,30,40,50)

print(t2)
print(t2[1], "\n")


print(t2[::-1], "\n")

for i in t2:
  print(i)
print()

for i in range(len(t2)):
  print(t2[i])