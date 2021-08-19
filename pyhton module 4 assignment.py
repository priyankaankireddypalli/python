# 1.

age = int(input("Enter the age: ")) # Creating the variable for taking age

if age<10:
    print("Children")
elif age>60:
    print("Senior Citizen")
elif (age>10) and (age<60):
    print("Normal Citizen")


#2

gender = input("Enter the Gender: ")
age = int(input("Enter age: "))

if (gender == "male"):
    if age>60:
        print("The person is a senior citizen and 70% of the fare is applicable")
    else:
        print("The person is normal citizen and 100% of the fare is applicable")
elif (gender == "female"):
    if age>60:
        print("The person is a senior citizen and 50% of the fare is applicable")
    else:
        print("The perosn is a normal citizen and 70% of the fare is applicable")


#3

num = int(input("Enter a number: "))
rem = num % 5
if (num > 0) and (rem == 0):
    print("The number is positive and divisible by 5")
elif (num > 0) and (rem != 0):
    print("The number is positive and not divisible by 5")
elif (num < 0) and (rem == 0):
    print("The number is negative and divisible by 5")
else:
    print("The number is negative and not divisible by 5")
    
        