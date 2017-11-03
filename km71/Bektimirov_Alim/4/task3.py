a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if c<a and c<b:
    print(c,"is the smallest number")
elif a<c and a<b:
    print(a,"is the smallest number")
elif b<c and b<a:
    print(b,"is the smallest number")
else:
    print("There isn't the smallest number")
