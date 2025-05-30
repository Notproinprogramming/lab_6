import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка! Ділення на нуль."

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Помилка! Ділення на нуль."

def factorial(a):
    if a < 0 or int(a) != a:
        return "Помилка! Факторіал визначений тільки для цілих невід’ємних чисел."
    return math.factorial(int(a))

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Помилка! Квадратний корінь з від’ємного числа неможливий."
    return math.sqrt(a)

def calculator():
    print("Простий калькулятор")
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Модуль (залишок від ділення)")
    print("6. Факторіал")
    print("7. Степінь (a^b)")
    print("8. Квадратний корінь")

    choice = input("Введіть номер операції (1-8): ")

    try:
        if choice in ('1', '2', '3', '4', '5', '7'):
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        elif choice == '6':
            num1 = float(input("Введіть число: "))
        elif choice == '8':
            num1 = float(input("Введіть число: "))
        else:
            print("Невірний вибір операції.")
            return
    except ValueError:
        print("Помилка! Введіть коректні числа.")
        return

    if choice == '1':
        print(f"Результат: {add(num1, num2)}")
    elif choice == '2':
        print(f"Результат: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Результат: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Результат: {divide(num1, num2)}")
    elif choice == '5':
        print(f"Результат: {modulus(num1, num2)}")
    elif choice == '6':
        print(f"Результат: {factorial(num1)}")
    elif choice == '7':
        print(f"Результат: {power(num1, num2)}")
    elif choice == '8':
        print(f"Результат: {sqrt(num1)}")

if __name__ == "__main__":
    calculator()
