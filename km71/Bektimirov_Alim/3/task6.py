group1 = int(input("Введіть кількість учнів 1 групи: "))
group2 = int(input("Введіть кількість учнів 1 групи: "))
group3 = int(input("Введіть кількість учнів 1 групи: "))
desk1 = group1//2 + group1%2
desk2 = group2//2 + group2%2
desk3 = group3//2 + group3%2
amount = desk1 + desk2 + desk3
print("Мінімальна кількість столів, яку необхідно придбати дорівнює:",amount)
