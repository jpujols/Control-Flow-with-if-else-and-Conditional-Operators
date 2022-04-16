print("Welcome to 9 Flags")
height = int(input("What is your height, cm: ? "))
age = int(input("What is your current age? "))

'''
Nested if / else

if condition:
  if another condition:
    do this
  else:
    do this
else:
  do this

*****
if /elif /ese

if condition1:
  do A
elif condition2:
  do B
else:
  do this
'''

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7.")
  ''' unlimited elif checks can be added here'''
else:
    print("Please pay $12")

 