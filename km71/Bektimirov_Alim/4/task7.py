x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
    print("YES")
elif (x1 + y1) % 2 == 1 and (x2 + y2) % 2 == 1:
    print("YES")
else:
    print("NO")
