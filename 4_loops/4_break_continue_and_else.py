for i in range(6):
  if i==3:
      break
  print(i)
print()

for i in range(8):
  if i==3:
      continue
  print(i)
print()

for i in range(6):
  print(i)
else:
   print("hii")
print()

for i in range(6):
  if i==3:
      break
  print(i)
else:
   print("hii")
print()

for i in range(6):
  if i==3:
      continue
  print(i)
else:
   print("hii")
print()


# Normal loop: else executes because the loop finishes normally.

# Loop with break: else does not execute because break terminates the loop.

# Loop with continue: else executes if the loop eventually finishes normally. continue does