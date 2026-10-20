# - Accept an integer and Print hello world n times
n = int(input("Enter n: "))
for i in range(n):
  print("hello world")
print()


# - Print natural number up to n
n = int(input("Enter n: "))
for i in range(1, n+1):
  print(i)
print()


# - Reverse for loop. Print n to 1
n = int(input("Enter n: "))
for i in range(n, 0, -1):
  print(i)
print()


# - Take a number as input and print its table
n = int(input("Enter n: "))
for i in range(1, 11):
  print(n, "x", i, "=", n*i)
print()



# - Sum up to n terms
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
  total += i
print("Sum =", total)
print()



# - Factorial of a number
n = int(input("Enter n: "))
fact = 1
for i in range(1, n+1):
  fact *= i
print("Factorial =", fact)


# - Print the sum of all even & odd numbers in a range separately
n = int(input("Enter n: "))
even_sum = 0
odd_sum = 0
for i in range(n+1):
  if i%2 == 0:
    even_sum += i
  else:
    odd_sum += i
print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)
print()



# - Print all the factors of a number
n = int(input("Enter n: "))
for i in range(1, n+1):
  if n%i == 0:
    print(i) 


# - Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself
n = int(input("Enter n: "))
total = 0
for i in range(1, n):
  if n%i == 0:
    total += i
  
if total == n:
  print(n, "is a perfect number")
else:
  print(n, "is not a perfect number")


# - Check wether the number is prime or not
n = int(input("Enter n: "))
if n < 2:
  print(n, "is not prime")

flag = 0
for i in range(2, n):
  if n%i == 0:
    flag = 1
    break

if flag == 0:
  print(n, "is prime")
else:
  print(n, "is not prime")
print()


# - Reverse a string without using in build functions.4
str = input("Enter string: ")
reversed_s = ""
for i in range(len(str)-1, -1, -1):
  reversed_s += str[i]
print("Reversed:", reversed_s)
print()



# - Check string is Pallindrome or not
str = input("Enter string: ")
reversed_s = ""
for i in range(len(str)-1, -1, -1):
  reversed_s += str[i]
if str == reversed_s:
  print(str, "is a palindrome")
else:
  print(str, "is not a palindrome")
print()



# - Count all letters, digits, and special symbols from a given
# string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4
str1 = "P@#yn26at^&i5ve"
letters = 0
digits = 0
symbols = 0
for i in str1:
  if i.isalpha():
    letters += 1
  elif i.isdigit():
    digits += 1
  else:
    symbols += 1
print("Chars =", letters)
print("Digits =", digits)
print("Symbol =", symbols)
