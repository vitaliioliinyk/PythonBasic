import math

# Метод print() для виведення на екран.
print("Hello World!")
print("The", "quick", "brown", "fox")  # кілька аргументів
print("The", 1, True)  # кілька типів даних

# Метод input() для отримання вводу від користувача
# age = input("Введіть ваш вік: ")
age = str(34)
print("Ваш вік", age, "роки.")
print(f"Ваш вік {age} роки.") # в фігурних дужках ми візьмемо значення змінної


# Тип даних змінної
print("Type of variable", age, type(age))  # <class 'str'>
age = int(age)
print("Type of variable", age, type(age))  # <class 'int'>
age = float(age)
print("Type of variable", age, type(age))  # <class 'int'>


# Числа в Python
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


# Арифметичні оператори
#   + додавання  - бінарний та унарний
#   - віднімання - бінарний та унарний
#   * множення
#   / ділення 10 / 2 = 5.0
#   ** степінь
#   // цілочисельне ділення 10//3=3; -10//3=-4; 15.5//3=5.0
#   % залишок від ділення 10%3=1

# Розширені оператори присвоювання
#   += додавання
#   -= віднімання
#   *= множення
#   /= ділення
#   **= степінь
#   //= цілочисельне ділення
#   %= залишок від ділення
c = 1
c += 2
print("Value of c: ", c)









