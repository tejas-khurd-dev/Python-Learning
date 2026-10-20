# Separate each digit of a number and print it on the new line
n = int(input("Enter n: "))
while n > 0:
  print(n % 10)
  n //= 10
print()


# Accept a number and print its reverse
n = int(input("Enter n: "))
original = n
reverse = 0
while n > 0:
  reverse = reverse * 10 + n % 10
  n //= 10
print("Reverse of", original, "=", reverse)
print()



# Accept a number and check if it is a pallindromic number (If number and its reverse are equal?)
n = int(input("Enter n: "))
original = n
reverse = 0
while n > 0:
  reverse = reverse * 10 + n % 10
  n //= 10
if original == reverse:
  print(original, "is a pallindromic number")
else:
  print(original, "is not a pallindromic number")
print()



# Create a random number guessing game with python.
import random
number = random.randint(1, 100)
# Python's random.randint(a, b) includes both the starting and ending values.
guess = 0
attempts = 0
print("Guess the number between 1 and 100")
while guess != number:
  guess = int(input("Enter your guess: "))
  attempts += 1
  if guess == number:
    print(f"Correct guess in {attempts} attempts")
    break
  elif guess < number:
    print("Too low!")
  else:
    print("Too high!")

