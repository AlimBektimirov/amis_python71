number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))
if (number1 == number2) and (number2 == number3):
    print("Amount of equal numbers: 3")
elif (number1 == number2) or (number2 == number3) or (number1 == number3):
    print("Amount of equal numbers: 2")
else:
    print("Amount of equal numbers: 0")
