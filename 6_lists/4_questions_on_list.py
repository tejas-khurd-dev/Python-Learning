# Print positive and negative elements of an List?
arr = [10, -5, 0, 8, -3, 2, -7]

for i in arr:
  if i > 0:
      print("Positive:", i)
  elif i < 0:
      print("Negative:", i)
print()




# Mean of List elements?
arr = [10, 20, 30, 40, 50]

total = 0

for i in arr:
  total += i

mean = total / len(arr)

print("Mean:", mean, "\n")



# Find the greatest element and print its index too?
arr = [12, 45, 7, 89, 34]

greatest = arr[0]
index = 0

for i in range(1, len(arr)):
    if arr[i] > greatest:
        greatest = arr[i]
        index = i

print("Greatest element:", greatest)
print("Index:", index, "\n")



# Find the second greatest element?
l = [12, 13, 19, 17]

largest = l[0]
sec_largest = l[0]

for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif largest > i > sec_largest:
        sec_largest = i

print(f"Second largest number is: {sec_largest} and largest number is: {largest} \n")



# Check if List is sorted or not.
arr = [10, 20, 30, 40, 50]

for i in range(len(arr) - 1):
  if arr[i] > arr[i + 1]:
      print("List is not sorted")
      break
else:
  print("List is sorted")

# If break executes, the loop's else block will NOT run.

# Loop finishes normally
# The else block executes if the loop completes without break.

# Loop encounters break
# The else block does not execute.