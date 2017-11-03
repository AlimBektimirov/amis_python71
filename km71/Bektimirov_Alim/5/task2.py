amount_of_elements = int(input("Amount of elements: "))
lst = []
for i in range(amount_of_elements):
    new_element = float(input("New element: "))
    lst.append(new_element)
lst.sort()
i = 1
pairs = 0
while i < amount_of_elements:
    if lst[i] == lst[i-1]:
        pairs += 1
    i += 1
print(pairs)
