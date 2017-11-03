amount_of_elements = int(input("Amount of elements: "))
lst = []
for i in range(amount_of_elements):
    new_element = float(input("New element: "))
    lst.append(new_element)
b = 0
answer = []
while b < amount_of_elements:
    a = 0
    pairs = 0
    while a < amount_of_elements:
        if lst[b] == lst[a]:
            pairs += 1
        a += 1
    if pairs == 1:
        answer.append(lst[b])
    b += 1
print(answer)
