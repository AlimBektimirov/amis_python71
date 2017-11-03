n = int(input("n = "))
m = int(input("m = "))
k = int(input("k = "))
if n % 2 == 0:
    n = n/2
else:
    if m % 2 == 0:
        m = m/2
if n * m == k:
    print("YES")
else:
    print("NO")
