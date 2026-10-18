# Q1. Accept two numbers and print the greatest between them.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
  print(num1, "is greatest")
elif num2 > num1:
  print(num2, "is greatest")
else:
  print("Both numbers are equal")


# Q2. Accept the gender from the user as char and print the
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)

gender = input("Enter gender (m/f): ")

if gender.lower() == "m":
  print("Good Morning Sir")
elif gender.lower() == "f":
  print("Good Morning Ma'am")
else:
  print("Invalid gender entered")


# Q3. Accept an integer and check whether it is an even number
# or odd.

num = int(input("Enter an integer: "))

if num % 2 == 0:
  print(num, "is an even number")
else:
  print(num, "is an odd number")


# Q4. Accept name and age from the user. Check if the user is a
# valid voter or not.
# Ex- “hello tejas you are a valid voter”

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
  print("hello", name, "you are a valid voter")
else:
  print("hello", name, "you are not a valid voter")


# Q5. Accept a year and check if it a leap year or not (google to
# find out what is a leap year)

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print(year, "is a leap year")
else:
  print(year, "is not a leap year")


# Q6) take the input of temperature in celsius
# Below 0°C → "Freezing Cold"
# 0°C to 10°C → "Very Cold"
# 10°C to 20°C → "Cold"
# 20°C to 30°C → "Pleasant"
# 30°C to 40°C → "Hot"
# Above 40°C → "Very Hot"
# Use if else ladder

temp = int(input("Enter temperature in Celsius: "))

if temp < 0:
  print("Freezing Cold")
else:
  if temp < 10:
    print("Very Cold")
  else:
    if temp < 20:
      print("Cold")
    else:
      if temp < 30:
        print("Pleasant")
      else:
        if temp <= 40:
          print("Hot")
        else:
          print("Very Hot")