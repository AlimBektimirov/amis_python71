x = float(input("Height of Petya: "))
n = int(input("Amount of children: "))
lst = []
for i in range(n):
    a = float(input("Height of children: "))
    lst.append(a)
z = 1
for i in lst:
    if x < i:
        z +=1
print("Number of Petya: ",z)
