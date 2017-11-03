x_c = []
y_c = []
element = 0
for g in range(8):
    x_c.append(int(input(" Enter coordinates of "+str(element+1)+" location (x) from 1 to 8: ")))
    y_c.append(int(input(" Enter coordinates of "+str(element+1)+" location (y) from 1 to 8: ")))
    element += 1
i = 0
b = 0
while i < 8:
    a = 0
    pairsX = 0
    while a < 8:
        if x_c[i] == x_c[a]:
            pairsX += 1
        a += 1
    i += 1
    if pairsX > 1:
        break
i = 0
while i < 8:
    a = 0
    pairsY = 0
    while a < 8:
        if y_c[i] == y_c[a]:
            pairsY += 1
        a += 1
    i += 1
    if pairsY > 1:
        break
if pairsX > 1 or pairsY > 1:
    print(" NO")
else:
    j = 0
    while j < 8:
        x1 = x_c[j]
        y1 = y_c[j]
        x2 = x_c[j]
        y2 = y_c[j]
        for d in range(8):
            x1 = x1 + 1
            y1 = y1 + 1
            x2 = x2 - 1
            y2 = y2 - 1
            t = 0
            while t < 8:
                if (x1 == x_c[t] or x2 == x_c[t]) and (y1 == y_c[t] or y2 == y_c[t]):
                    b += 1
                    break
                if x1 != x_c[t] and x2 != x_c[t]:
                    b += 0
                t += 1
        j += 1
    if b == 0:
        print(" YES")
    else:
        print(" NO")
