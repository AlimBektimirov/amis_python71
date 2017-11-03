x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
if y2 == y1+1 or y2 == y1-1 and x2 == x1+2 or x2 == x1-2:
    print("YES")
else:
    print("NO")
