print("Умова: Напишіть програму, яка отримує довжини двох катетів прямокутного\nтрикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.\nВхідні дані: 2 дійсних числа.  Кожне число користувач вводить в окремому рядку.\nВихідні дані: вивести площу трикутника на екран")
# Програма для знаходження площі прямокутного трикутника
# Ввід катетів трикутника
a = int(input("Введіть довжину першого катета: "))
b = int(input("Введіть довжину другого катета: "))
S = a * b / 2
# Вивід площи трикутника
print("Площа трикутника дорівнює: " + str(S))
