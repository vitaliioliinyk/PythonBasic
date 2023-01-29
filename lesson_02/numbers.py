import math

# Метод print() для виведення на екран.
print("Hello World!")
print("The", "quick", "brown", "fox")  # кілька аргументів

# Метод input() для отримання вводу від користувача
# age = input("Введіть ваш вік: ")
age = str(34)
print("Ваш вік", age, "роки.")
print(f"Ваш вік {age} роки.") # в фігурних дужках ми візьмемо значення змінної


# Тип даних змінної
print("Type of variable", type(age)) # <class 'str'>
age = int(age)
print("Type of variable", type(age)) # <class 'int'>


# Типи даних в Python
#   Цілі числа
i = 1 # i type <class 'int'>
print("i type", type(i))
#   Довга арифметика цілих цисел, розмір int в Python 3 обмежений пам*яттю
i = 123456789012345678901234567890123456789012345678901234567890
print("Long integer sum", i+1)

#   Дійсні числа float
f = 1.2 # f type <class 'float'> Size 1.8*10**308
print("f type", type(f))

#   Точність float
a = 0.1
b = 0.2
print(f"Float {a} + {b} = {a+b}") # обчислення на f-string 0.30000000000000004
print("Equal float", math.isclose(a+b, 0.3)) # перевірити чи співпадають
#   Або використовувати тип Decimal. Інші типи Fraction i Complex




